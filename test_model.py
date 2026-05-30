import joblib
import os

# model.pkl dosyasının bulunduğu yolu yaz
model_path = os.path.join('ml', 'model.pkl') 
model = joblib.load(model_path)

print(f"Model Tipi: {type(model)}")
# Eğer model içinde predict_proba varsa, bu genellikle bir Classifier'dır
print(f"Sınıflandırıcı mı?: {hasattr(model, 'predict_proba')}")