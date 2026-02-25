from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models, schemas
import joblib 
import os

# CREACIÓN AUTOMÁTICA: Si la tabla no existe en Postgres, FastAPI la crea ahora
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Churn Prediction API")

# Cargar el modelo al iniciar la API
MODEL_PATH = "models/churn_model.pkl"
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None
    print("⚠️ Advertencia: No se encontró el modelo en models/churn_model.pkl")


# Permite que Next.js se comunique con FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check-db")
def check_connection(db: Session = Depends(get_db)):
    # Si esto responde, la conexión con Docker es perfecta
    return {"status": "Conectado a PostgreSQL", "database": "churn_db"}

# Endpoint para crear un nuevo cliente
@app.post("/customers/", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    # 1. Verificar si el customer_id ya existe
    db_customer = db.query(models.Customer).filter(models.Customer.customer_id == customer.customer_id).first()
    if db_customer:
        raise HTTPException(status_code=400, detail="El ID del cliente ya está registrado")
    
    # 2. Convertir el esquema de Pydantic a un modelo de SQLAlchemy
    new_customer = models.Customer(
        customer_id=customer.customer_id,
        tenure=customer.tenure,
        monthly_charges=customer.monthly_charges,
        total_charges=customer.total_charges
    )
    
    # 3. Guardar en Postgres (Docker)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    
    return new_customer


@app.get("/customers/", response_model=list[schemas.CustomerResponse])
def get_all_customers(db: Session = Depends(get_db)):
    # Esta línea busca todos los registros en la tabla
    customers = db.query(models.Customer).all()
    return customers

@app.post("/predict", response_model=dict)
def predict_churn(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    if model is None:
        raise HTTPException(status_code=503, detail="Modelo de IA no disponible")
    
    # 1. Preparar datos y predecir
    input_data = [[customer.tenure, customer.monthly_charges, customer.total_charges]]
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    risk_score = float(round(probability * 100, 2))
    
    # 2. GUARDAR EN EL HISTORIAL (Nuevo paso)
    history_entry = models.PredictionHistory(
        customer_id=customer.customer_id,
        tenure=customer.tenure,
        monthly_charges=customer.monthly_charges,
        total_charges=customer.total_charges,
        prediction="Yes" if prediction == 1 else "No",
        risk_score=risk_score
    )
    db.add(history_entry)
    db.commit() # Envía los datos al contenedor de Docker
    
    # 3. Explicabilidad
    importances = model.feature_importances_
    features = ["antigüedad", "cargo_mensual", "cargo_total"]
    explanation = {features[i]: round(importances[i] * 100, 2) for i in range(len(features))}
    
    return {
        "customer_id": customer.customer_id,
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "risk_score": risk_score,
        "explanation_pct": explanation,
        "message": "Guardado en historial de base de datos"
    }