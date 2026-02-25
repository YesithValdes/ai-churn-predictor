from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Esto intenta leer la variable de Docker, si no existe, usa 'db' como nombre del host
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://alexi:password123@db:5432/churn_db")

engine = create_engine(DATABASE_URL)

# Cada vez que alguien pida algo a la API, crearemos una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la que heredarán nuestras tablas
Base = declarative_base()

# Función para cerrar la conexión automáticamente después de cada uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()