# 📊 AI Churn Predictor

Este proyecto es una aplicación **Full-Stack** diseñada para predecir la probabilidad de fuga de clientes (*churn*) utilizando Inteligencia Artificial. El sistema permite procesar datos de usuarios y obtener una predicción basada en un modelo de **Machine Learning** de clasificación.



## 🚀 Arquitectura del Sistema

El proyecto está desplegado en **Railway** utilizando una arquitectura de microservicios en un monorepo:

* **Frontend**: Interfaz de usuario reactiva construida con **Next.js** y **Tailwind CSS**.
* **Backend (API)**: Servicio de alto rendimiento desarrollado con **FastAPI** (Python) que sirve el modelo de IA.
* **Base de Datos**: Instancia de **PostgreSQL** para el almacenamiento persistente de registros.
* **Modelo de IA**: Clasificador basado en **Random Forest** serializado en formato `.pkl`.

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Rol |
| :--- | :--- | :--- |
| **Frontend** | Next.js, React, Tailwind CSS | Interfaz y Dashboard |
| **Backend** | FastAPI, Python 3.x, Uvicorn | Lógica de la API y ML |
| **IA / ML** | Scikit-learn, Pandas, Joblib | Entrenamiento y Predicción |
| **Base de Datos** | PostgreSQL | Persistencia de datos |
| **Infraestructura** | Railway | Hosting y CI/CD |

---

## 🧠 Detalles del Modelo de IA

El núcleo del predictor es un modelo entrenado con un dataset de **Kaggle** enfocado en el comportamiento de clientes.

* **Algoritmo**: Random Forest Classifier.
* **Rendimiento**: Se alcanzó una precisión del **75.76%** en el conjunto de prueba.

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN} \approx 0.7576$$



---

## 🔧 Configuración para Desarrollo Local

Para ejecutar este proyecto, tienes dos opciones: usar Docker para levantar todo automáticamente de forma orquestada (recomendado) o levantar cada servicio manualmente.

### Opción A: Usando Docker (Recomendado)

El proyecto cuenta con un archivo `docker-compose.yml` que orquesta los tres microservicios: la base de datos PostgreSQL, el backend en FastAPI y el frontend interactivo en Next.js.

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/YesithValdes/ai-churn-predictor.git
    cd ai-churn-predictor
    ```

2.  **Levantar los microservicios**:
    Asegúrate de tener Docker Desktop instalado y corriendo. Luego, simplemente ejecuta en la raíz del proyecto:
    ```bash
    docker-compose up -d --build
    ```
    
    Esto construirá y enlazará en red internamente los siguientes servicios de manera automática:
    - **Base de Datos (PostgreSQL)**: Expuesta en el puerto `5432`
    - **Backend API (FastAPI)**: Disponible en `http://localhost:8000` (Docs en `http://localhost:8000/docs`)
    - **Frontend interactivo (Next.js)**: Disponible en `http://localhost:3000`

    *Nota: Para detener los contenedores y apagarlos, puedes usar `docker-compose down`.*

### Opción B: Manualmente (Terminal por Terminal)

Si no deseas utilizar Docker, puedes correrlos individualmente:

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/YesithValdes/ai-churn-predictor.git
    cd ai-churn-predictor
    ```

2.  **Levantar el Backend (Microservicio API)**:
    Se recomienda usar un entorno virtual para aislar las dependencias de Python. (Asume que ya tienes un PostgreSQL local instalado corriendo por tu cuenta).
    ```bash
    # Crear y activar entorno virtual (Windows)
    python -m venv venv
    venv\Scripts\activate
    
    # Instalar dependencias
    pip install -r requirements.txt
    
    # Iniciar la API
    uvicorn app.main:app --reload
    ```
    La API estará disponible en `http://localhost:8000` y su documentación en `http://localhost:8000/docs`.

3.  **Levantar el Frontend (Microservicio Cliente)**:
    Abre una nueva terminal, mantén el backend corriendo, y desde la raíz del proyecto viaja al frontend:
    ```bash
    cd frontend
    
    # Instalar dependencias
    npm install
    
    # Crea un archivo .env en la carpeta frontend y añade:
    # NEXT_PUBLIC_API_URL=http://localhost:8000
    
    # Iniciar la aplicación en modo desarrollo
    npm run dev
    ```
    El frontend estará disponible interactivo en `http://localhost:3000`.

---

## 🌐 API Endpoints

La API cuenta con documentación interactiva en la ruta `/docs` tras iniciar el servicio.



* `POST /predict/`: Recibe los datos del cliente y devuelve la probabilidad de churn.

---

## 🤝 Contribuciones y Licencia

¡Las contribuciones de compañeros de la **Universidad del Cauca** son bienvenidas!.
1.  Haz un *Fork* del proyecto.
2.  Crea una rama para tu mejora (`git checkout -b feature/nueva-funcionalidad`).
3.  Abre un *Pull Request*.

Este proyecto está bajo la **Licencia MIT**. Eres libre de usarlo para fines académicos o personales.

---

**Autor:** [Alexis Valdez ](https://github.com/YesithValdes)  
**Ubicación:** Popayán, Cauca, Colombia  
**Institución:** Estudiante en la Universidad del Cauca