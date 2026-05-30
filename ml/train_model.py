import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_and_save_model():
    file_path = 'data/datatraining.txt' 
    df = pd.read_csv(file_path)
    if 'date' in df.columns:
        df = df.drop(columns=['date'])

    X = df.drop(columns=['Occupancy'])
    y = df['Occupancy']

    print("Model eğitiliyor...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    if not os.path.exists('ml'):
        os.makedirs('ml')
    
    joblib.dump(model, 'ml/model.pkl')
    print("Model başarıyla 'ml/model.pkl' olarak kaydedildi.")

if __name__ == "__main__":
    train_and_save_model()