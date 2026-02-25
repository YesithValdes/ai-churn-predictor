import kagglehub
import pandas as pd
from sqlalchemy import create_engine
import os
import glob

# 1. Descarga automática desde Kaggle
print("Descargando dataset desde Kaggle...")
download_path = kagglehub.dataset_download("palashfendarkar/wa-fnusec-telcocustomerchurn")
print(f"Dataset descargado en: {download_path}")

# 2. Buscar el archivo CSV dentro de la carpeta descargada
csv_files = glob.glob(os.path.join(download_path, "*.csv"))
if not csv_files:
    raise FileNotFoundError("No se encontró ningún archivo CSV en la descarga.")

# 3. Configuración de la base de datos (Docker)
DB_URL = "postgresql://alexi:password123@localhost:5432/churn_db"
engine = create_engine(DB_URL)

def process_and_upload():
    # Leer el primer CSV encontrado
    df = pd.read_csv(csv_files[0])
    
    # Limpieza rápida (Esencial para que Postgres no dé error)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()
    
    # Seleccionamos las columnas que definimos en tu models.py
    df_to_db = df[['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']].copy()
    df_to_db.columns = ['customer_id', 'tenure', 'monthly_charges', 'total_charges', 'churn_label']
    
    # Subir a la base de datos
    df_to_db.to_sql('customers', engine, if_exists='replace', index=False)
    print(f"¡Éxito! {len(df_to_db)} clientes de Kaggle han sido guardados en PostgreSQL.")

if __name__ == "__main__":
    process_and_upload()