from pydantic import BaseModel
from typing import Optional

# Lo que el usuario nos envía cuando crea un cliente
class CustomerCreate(BaseModel):
    customer_id: str
    tenure: int
    monthly_charges: float
    total_charges: float
    churn_label: Optional[str] = None

# Lo que la API responde (incluye el ID de la base de datos)
class CustomerResponse(CustomerCreate):
    id: int
    churn_risk_score: Optional[float] = None

    class Config:
        from_attributes = True