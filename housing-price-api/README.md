# 🏡 California Housing Price Prediction API

A production-ready Machine Learning service that predicts median housing prices in California districts based on census data. This project demonstrates an end-to-end **MLOps** workflow: from model training to deployment as a containerized REST API.

---

## 🚀 Key Features
* **Random Forest Regressor**: Trained on the standard California Housing dataset.
* **REST API**: Built with **FastAPI** for high performance and automatic documentation.
* **Containerized**: Fully Dockerized for consistent deployment across any environment.
* **Input Validation**: Uses **Pydantic** models to ensure data integrity.

## 🛠️ Tech Stack
* **Language**: Python 3.9+
* **Framework**: FastAPI, Uvicorn
* **ML Libraries**: Scikit-Learn, Pandas, Joblib
* **Containerization**: Docker

---

## 📦 Installation & Setup

You can run this project either locally with Python or as a Docker container.

### Option 1: Run with Docker (Recommended)
Build the image and run the container in two simple steps:

```bash
# 1. Build the Docker image
docker build -t housing-price-api .

# 2. Run the container
docker run -p 8000:8000 housing-price-api
```
### Option 2: Run Locally
If you prefer to run it without Docker:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train the model (creates the .joblib file)
python train.py

# 3. Start the API server
uvicorn main:app --reload
```
## 📡 API Usage
Once the server is running, you can interact with the API endpoints.

### 📖 Interactive Documentation
Visit http://localhost:8000/docs to see the Swagger UI. You can test the endpoints directly from your browser!

### 🔮 Prediction Endpoint
POST /predict

Send a JSON body with the following features:

```bash
{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.9841,
  "AveBedrms": 1.0238,
  "Population": 322.0
}
```

Response:

```bash
{
  "predicted_median_house_value": 4.152
}
```

### 📂 Project Structure

```
housing-price-api/
├── Dockerfile          
├── main.py             
├── train.py            
├── requirements.txt    
└── README.md           
```
