from sqlalchemy import Column, Integer, String, Float, Boolean
from .database import Base

# app/models.py (Fragmento actualizado)
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, unique=True)
    tenure = Column(Integer)
    contract_type = Column(String)  # Nuevo: Mes a mes, Anual, etc.
    monthly_charges = Column(Float)
    total_charges = Column(Float)
    internet_service = Column(String) # Nuevo: DSL, Fiber, No
    churn_label = Column(String, nullable=True) # Lo que dice Kaggle (Yes/No)
    prediction_score = Column(Float, nullable=True) # Lo que dirá TU modelo

class PredictionHistory(Base):
    __tablename__ = "predictions_history"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String)
    tenure = Column(Integer)
    monthly_charges = Column(Float)
    total_charges = Column(Float)
    prediction = Column(String)  # "Yes" o "No"
    risk_score = Column(Float)   # El porcentaje de riesgo