import joblib
import os
model_path = os.path.join('ml', 'model.pkl') 
model = joblib.load(model_path)
print(f"Model Tipi: {type(model)}")
print(f"Sınıflandırıcı mı?: {hasattr(model, 'predict_proba')}")
