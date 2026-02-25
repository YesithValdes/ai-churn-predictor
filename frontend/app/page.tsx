"use client";
import { useState } from "react";

export default function ChurnDashboard() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    
    const formData = new FormData(e.currentTarget);
    const payload = {
      customer_id: `CUST-${Math.floor(Math.random() * 1000)}`,
      tenure: Number(formData.get("tenure")),
      monthly_charges: Number(formData.get("monthly_charges")),
      total_charges: Number(formData.get("total_charges")),
    };

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
      
      const response = await fetch(`${apiUrl}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error conectando con la IA:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100 p-8 font-sans">
      <header className="max-w-4xl mx-auto mb-12">
        <h1 className="text-4xl font-extrabold text-blue-500 mb-2">AI Churn Predictor</h1>
        <p className="text-zinc-400">Análisis de fuga de clientes basado en Random Forest (Precisión: 75.76%)</p>
      </header>

      <main className="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12">
        {/* Formulario de Entrada */}
        <section className="bg-zinc-900 p-6 rounded-xl border border-zinc-800 shadow-xl">
          <h2 className="text-xl font-semibold mb-6">Datos del Cliente</h2>
          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="block text-sm font-medium mb-2 text-zinc-400">Antiguedad (Meses)</label>
              <input name="tenure" type="number" required className="w-full bg-zinc-800 border-zinc-700 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 outline-none" placeholder="Ej: 12" />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2 text-zinc-400">Cargo Mensual ($)</label>
              <input name="monthly_charges" type="number" step="0.01" required className="w-full bg-zinc-800 border-zinc-700 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 outline-none" placeholder="Ej: 70.50" />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2 text-zinc-400">Cargos Totales ($)</label>
              <input name="total_charges" type="number" step="0.01" required className="w-full bg-zinc-800 border-zinc-700 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 outline-none" placeholder="Ej: 846.00" />
            </div>
            <button type="submit" disabled={loading} className="w-full bg-blue-600 hover:bg-blue-700 py-3 rounded-lg font-bold transition-all disabled:opacity-50">
              {loading ? "Procesando..." : "Calcular Riesgo"}
            </button>
          </form>
        </section>

        {/* Panel de Resultados */}
        <section className="flex flex-col justify-center">
          {!result ? (
            <div className="text-center p-10 border-2 border-dashed border-zinc-800 rounded-xl text-zinc-600">
              Ingresa los datos para ver la predicción de la IA
            </div>
          ) : (
            <div className={`p-8 rounded-xl border-l-8 shadow-2xl ${result.churn_prediction === 'Yes' ? 'bg-red-950/20 border-red-600' : 'bg-green-950/20 border-green-600'}`}>
              <h3 className="text-2xl font-bold mb-2">Resultado: {result.churn_prediction === 'Yes' ? '🚨 Riesgo de Fuga' : '✅ Cliente Estable'}</h3>
              <div className="text-5xl font-black mb-6">{result.risk_score}% <span className="text-lg font-normal text-zinc-400">de probabilidad</span></div>
              
              <div className="space-y-2 border-t border-zinc-800 pt-4">
                <p className="text-sm text-zinc-400 uppercase tracking-widest font-bold">Explicación del Modelo (XAI):</p>
                <p className="text-sm">La <span className="text-blue-400">antigüedad</span> influyó un {result.explanation_pct.antigüedad}% en esta decisión.</p>
                <p className="text-xs text-zinc-500 mt-4 italic">Registro guardado en PostgreSQL (Docker Desktop)</p>
              </div>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}
