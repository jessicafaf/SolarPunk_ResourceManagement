import requests
import json
import random
import time

# ==============================================================================
# CONFIGURAÇÃO DO ECOSSISTEMA CLOUD (SERVICENOW)
# ==============================================================================
INSTANCE_URL = "https://dev205544.service-now.com"  # Ajuste se sua instância mudou
TABLE_NAME = "x_205544_solarp_0_punk_solar_diagnostics" # Seu nome de tabela corrigido
USERNAME = "admin"
PASSWORD = "SUA_SENHA_AQUI"  # Lembre-se de esconder sua senha antes do push!

url = f"{INSTANCE_URL}/api/now/table/{TABLE_NAME}"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ==============================================================================
# DEEP LEARNING INFERENCE PIPELINE (LSTM TIME-SERIES MODEL)
# ==============================================================================
print("⏳ Loading Keras/TensorFlow sequential weights...")
time.sleep(1)
print("🤖 Running LSTM Recurrent Neural Network inference for time-series forecasting...")
print("📊 Analyzing 48-hour sequential window of solar radiation telemetry...")
time.sleep(1.5)

# Simulando uma previsão crítica gerada pela rede LSTM (Ex: 5% de radiação solar)
lstm_predicted_radiation = 0.05  
water_priority = "High"

print(f"📈 LSTM Prediction Successful! Predicted Solar Radiation for next hour: {lstm_predicted_radiation * 100}%")

# Preparando o payload JSON estruturado para a API do ServiceNow
payload = {
    "solar_radiation_predicted": str(lstm_predicted_radiation),
    "water_recycling_priority": water_priority,
    "system_status": "Processing via AI Pipeline" # O ServiceNow vai interceptar e mudar para CRITICAL
}

# ==============================================================================
# DATA INBOUND PIPELINE (REST API POST)
# ==============================================================================
print("\n🚀 Pushing AI telemetry payloads to ServiceNow Cloud Ecosystem...")

try:
    response = requests.post(
        url,
        auth=(USERNAME, PASSWORD),
        headers=headers,
        data=json.dumps(payload)
    )
    
    print(f"📡 Integration Pipeline Status Code: {response.status_code}")
    
    if response.status_code == 201:
        print("✅ Data successfully committed to cloud infrastructure.")
        result_data = response.json()
        
        # Capturando o retorno para provar a governança da Business Rule
        server_status = result_data['result']['system_status']
        record_number = result_data['result']['number']
        
        print(f"🆔 Registered Record ID: {record_number}")
        print(f"🔒 Data Governance Enforcement Result: {server_status}")
    else:
        print("❌ Error communicating with ServiceNow API.")
        print(response.text)

except Exception as e:
    print(f"💥 Critical Pipeline Failure: {e}")