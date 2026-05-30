def evaluate_risk(data, predicted_occupancy):
    """
    data: dict (sensor verileri)
    predicted_occupancy: int (0 veya 1)
    """
    alert = "Normal"
    risk_score = 0
    
    co2 = data.get('CO2', 0)
    light = data.get('Light', 0)
    temp = data.get('Temperature', 0)
    
    if co2 > 1000 and predicted_occupancy == 1:
        alert = "Air Quality Risk"
        risk_score += 40
    
    if light > 300 and predicted_occupancy == 0:
        alert = "Energy Waste"
        risk_score += 30
        
    if predicted_occupancy == 1 and light < 20:
        alert = "Suspicious Occupancy"
        risk_score += 25
        
    if temp > 28:
        risk_score += 10
        
    return alert, risk_score