import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 1. Conexión a la base de datos de Docker
DB_URL = "postgresql://alexi:password123@localhost:5432/churn_db"
engine = create_engine(DB_URL)

def generate_insights():
    print("Extrayendo datos de PostgreSQL...")
    # Traemos los datos a un DataFrame de Pandas
    df = pd.read_sql("SELECT * FROM customers", engine)

    # Configuración de estilo
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 6))

    # 2. Gráfico: Distribución de la Antigüedad (Tenure)
    # Esto nos dice si tenemos más clientes nuevos o antiguos
    plt.subplot(1, 2, 1)
    sns.histplot(df['tenure'], kde=True, color="skyblue")
    plt.title('Distribución de Antigüedad (Meses)')
    plt.xlabel('Meses en la empresa')

    # 3. Gráfico: Relación entre Cargos Mensuales y Antigüedad
    plt.subplot(1, 2, 2)
    sns.scatterplot(data=df, x='tenure', y='monthly_charges', alpha=0.3, color="coral")
    plt.title('Cargos Mensuales vs. Antigüedad')
    plt.xlabel('Meses')
    plt.ylabel('Cargos Mensuales ($)')

    # Guardar la imagen
    plt.tight_layout()
    plt.savefig('data/insights_clientes.png')
    print("¡Gráficos generados con éxito! Revisa la carpeta /data/insights_clientes.png")
    plt.show()

if __name__ == "__main__":
    generate_insights()