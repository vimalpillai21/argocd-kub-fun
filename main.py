"""FastAPI inference server for churn prediction"""
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

with open("models/churn_model.pkl","rb") as f:
    model = pickle.load(f)

class CustomerData(BaseModel):
    age: int
    tenure_months: int
    monthly_charges: int
    total_charges: int
    num_support_calls: int

@app.get("/health")
def health():
    return {"status": "health"}

@app.post("/predict")
def predict(data: CustomerData):
    features = np.array([[
        data.age,
        data.tenure_months,
        data.monthly_charges,
        data.total_charges,
        data.num_support_calls
    ]])

    prediction = model.predict(features)[0]
    pred_probability = model.predict_proba(features)[0][1]
    print(prediction)
    print(pred_probability)
    return {
        "churn": int(prediction),
        "churn_proabability": float(pred_probability)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)