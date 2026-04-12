import kagglehub
import pandas as pd
from sqlalchemy import create_engine
import os
import glob
from dotenv import load_dotenv

# 1. INITIALIZATION: Load environment variables from the .env file
# This prevents hardcoding sensitive credentials in the source code.
load_dotenv()

"""
Kaggle Data Pipeline & Ingestion Script
Author: Alexis Valdez
Target: University of Cauca - Thesis Project
Description: Automates the Telco Churn dataset download and PostgreSQL upload.
"""

# 2. KAGGLE AUTOMATION: Download the latest version of the dataset
print("Downloading dataset from Kaggle...")
download_path = kagglehub.dataset_download("palashfendarkar/wa-fnusec-telcocustomerchurn")
print(f"Dataset stored at: {download_path}")

# 3. FILE SYSTEM: Search for any CSV file in the dynamic download path
csv_files = glob.glob(os.path.join(download_path, "*.csv"))
if not csv_files:
    raise FileNotFoundError("Critical Error: No CSV file found in the download path.")

# 4. DATABASE SECURITY: Retrieve the connection string from Environment Variables
# The variable 'DATABASE_URL' must be defined in your .env file.
# Format: postgresql://user:password@localhost:5432/dbname
DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise ValueError("Security Error: DATABASE_URL not found in environment variables.")

# Create the SQLAlchemy engine for PostgreSQL communication
engine = create_engine(DB_URL)

def process_and_upload():
    """
    Main execution logic: Cleaning, mapping, and database ingestion.
    """
    # Load the first detected CSV into a Pandas DataFrame
    df = pd.read_csv(csv_files[0])
    
    # DATA CLEANING: Essential to avoid PostgreSQL data type conflicts
    # 'TotalCharges' often contains empty strings; coerce them to numeric (NaN)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()
    
    # SELECTION: Filter specific columns required for the churn model
    df_to_db = df[['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']].copy()
    
    # MAPPING: Rename columns to match the PostgreSQL schema (snake_case)
    df_to_db.columns = ['customer_id', 'tenure', 'monthly_charges', 'total_charges', 'churn_label']
    
    # UPLOAD: Use 'replace' to refresh the table or 'append' to keep history
    try:
        df_to_db.to_sql('customers', engine, if_exists='replace', index=False)
        print(f"Task Completed: {len(df_to_db)} records synchronized with PostgreSQL.")
    except Exception as e:
        print(f"Critical Database Failure: {e}")

def preprocess():
    """
    Optional preprocessing steps before the main upload.
    This can include additional data transformations or validations.
    """

    df = pd.read_csv(csv_files[0])
    print(df.head())  # Display the first few rows for verification

    print(df.info())  # Check data types and non-null counts

    
    #print("Preprocessing data before upload...")
    # Placeholder for any future preprocessing logic
    #process_and_upload()

if __name__ == "__main__":
    preprocess()