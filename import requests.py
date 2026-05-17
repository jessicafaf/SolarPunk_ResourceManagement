import requests
import json

# ==============================================================================
# CONFIGURAÇÕES DO SEU SERVICENOW (PREENCHA AQUI)
# ==============================================================================
INSTANCE_URL = "https://dev279451.service-now.com"  
USERNAME = "admin"
PASSWORD = "PASSWORD HERE" 
# ==============================================================================

TABLE_NAME = "x_2055449_solarp_0_solar_diagnostics" 

endpoint_url = f"{INSTANCE_URL}/api/now/table/{TABLE_NAME}"

# Simulando o resultado de uma Inteligência Artificial (Média de Radiação Baixa)
ai_predicted_data = {
    "solar_radiation_predicted": "0.05", # 5% de radiation 
    "water_recycling_priority": "High"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

print("🤖 Simulando previsão da IA e enviando para o ServiceNow...")

# Fazendo a chamada REST POST (Enviando dados para a nuvem)
response = requests.post(
    endpoint_url,
    auth=(USERNAME, PASSWORD),
    headers=headers,
    data=json.dumps(ai_predicted_data)
)

# Verificando se deu certo
if response.status_code == 201:
    print("✅ Sucesso! Dado inserido no ServiceNow.")
    result = response.json()
    # Mostra o status que a nossa Business Rule calculou nos bastidores!
    system_status = result['result']['system_status']
    print(f"📊 Status retornado pelo ServiceNow: {system_status}")
else:
    print(f"❌ Erro na integração. Status Code: {response.status_code}")
    print(response.text)