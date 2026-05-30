import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import json
import pandas as pd
import joblib
from fastapi import FastAPI, WebSocket
from backend.decision_engine import evaluate_risk

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, 'ml', 'model.pkl'))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'datatest2.txt')

@app.websocket("/ws/sensors")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    df = pd.read_csv(DATA_PATH)
    
    for _, row in df.iterrows():
        sensor_data = {
            "Temperature": float(row['Temperature']),
            "Humidity": float(row['Humidity']),
            "Light": float(row['Light']),
            "CO2": float(row['CO2']),
            "HumidityRatio": float(row['HumidityRatio']) 
        }
        
        input_df = pd.DataFrame([sensor_data])
        prediction = int(model.predict(input_df)[0])
        
        alert, score = evaluate_risk(sensor_data, prediction)
        
        payload = {
            "time": str(row['date']),
            **sensor_data,
            "predicted_occupancy": prediction,
            "alert_type": alert,
            "risk_score": score
        }
        
        await websocket.send_json(payload)
        await asyncio.sleep(1)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)