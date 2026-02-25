import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# 1. Conexión a Docker
DB_URL = "postgresql://alexi:password123@localhost:5432/churn_db"
engine = create_engine(DB_URL)

def train():
    print("🧠 Extrayendo datos para entrenamiento...")
    # NOTA: Asegúrate de que tu tabla tenga la columna 'churn_label'
    df = pd.read_sql("SELECT tenure, monthly_charges, total_charges, churn_label FROM customers", engine)
    
    # 2. Preprocesamiento (Convertir Yes/No a 1/0)
    df['churn_label'] = df['churn_label'].map({'Yes': 1, 'No': 0})
    df = df.dropna()

    X = df[['tenure', 'monthly_charges', 'total_charges']] # Lo que la IA mira
    y = df['churn_label'] # Lo que la IA debe adivinar

    # 3. Dividir datos: 80% para aprender, 20% para examen
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Entrenar el modelo (Random Forest)
    print("🔥 Entrenando el modelo en tu Ryzen 3...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 5. Evaluación
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"✅ ¡Entrenamiento completo! Precisión: {acc:.2%}")

    # 6. Guardar el "cerebro"
    if not os.path.exists('models'): os.makedirs('models')
    joblib.dump(model, 'models/churn_model.pkl')
    print("💾 Modelo guardado en models/churn_model.pkl")

if __name__ == "__main__":
    train()