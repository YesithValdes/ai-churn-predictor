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

Para ejecutar este proyecto en tu propia máquina (como en un **Aspire A515-45**):

1.  **Clonar el repositorio**:
    ```bash
    git clone [https://github.com/YesithValdes/ai-churn-predictor.git](https://github.com/YesithValdes/ai-churn-predictor.git)
    ```
2.  **Configurar Backend**:
    * Instalar dependencias: `pip install -r requirements.txt`.
    * Iniciar API: `uvicorn app.main:app --reload`.
3.  **Configurar Frontend**:
    * Instalar dependencias: `cd frontend && npm install`.
    * Configurar `.env` con `NEXT_PUBLIC_API_URL=http://localhost:8000`.
    * Iniciar: `npm run dev`.

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