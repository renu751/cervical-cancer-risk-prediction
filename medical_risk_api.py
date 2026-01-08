from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI(title="Cervical Cancer Risk Prediction API")

# Load balanced model
model = joblib.load("cervical_cancer_risk_model_balanced.pkl")

@app.get("/")
def home():
    return {"message": "Cervical Cancer Risk Prediction API is running"}

@app.post("/predict")
def predict_risk(features: dict):
    """
    Input: patient medical features as JSON
    Output: cancer risk prediction (0 or 1)
    """
    input_data = np.array([list(features.values())])
    prediction = model.predict(input_data)
    return {"cancer_risk": int(prediction[0])}
