# 🩺 Cervical Cancer Risk Prediction API
## 🌐 Live Demo
The API is deployed live on the cloud using Render.

🔗 **Live URL:**  
https://cervical-cancer-risk-prediction.onrender.com/docs


An end-to-end **medical risk prediction system** built using machine learning, FastAPI, and Docker.  
The project focuses on **early cervical cancer risk screening**, with special emphasis on **reducing false negatives**, which is critical in healthcare applications.

---

## 📌 Problem Statement
Cervical cancer is one of the most preventable cancers if detected early.  
The goal of this project is to build a **clinical decision-support system** that predicts cervical cancer risk based on patient medical and lifestyle factors.

---

## 🎯 Key Objectives
- Clean and preprocess real-world medical data
- Handle hidden missing values and class imbalance
- Optimize the model for **high recall**
- Deploy the model as a **REST API**
- Containerize the solution using **Docker**

---

## 🧠 Machine Learning Approach
- **Dataset:** Cervical Cancer Risk Factors (Kaggle)
- **Target Variable:** `Biopsy` (0 = No risk, 1 = High risk)
- **Model Used:** Logistic Regression
- **Optimization:** Class imbalance handled using `class_weight='balanced'`
- **Metric Focus:** Recall (to minimize missed cancer cases)

### 📊 Model Performance (Balanced Model)
- Recall (Cancer Class): **79%**
- False Negatives reduced from **5 → 3**
- Suitable for **screening and risk assessment**

---

## 🩺 Medical Importance
In healthcare screening systems:
- **False negatives are dangerous**
- **False positives are acceptable**

This project prioritizes **patient safety** by maximizing recall.

---

## 🚀 Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **FastAPI**
- **Docker**
- **Git & GitHub**

---

## 🔧 Project Structure

---

## ▶️ How to Run the Project (Using Docker)

### 1️⃣ Build Docker Image
```bash
docker build -t cervical-cancer-risk-api .
2️⃣ Run the Container
docker run -p 8000:8000 cervical-cancer-risk-api
3️⃣ Access API
Open your browser:
http://127.0.0.1:8000/docs
API Endpoints
GET /

Health check endpoint.

POST /predict

Predicts cervical cancer risk based on patient medical data.

Sample Response:
{
  "cancer_risk": 1
}
