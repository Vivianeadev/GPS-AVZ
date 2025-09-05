import requests
from datetime import datetime

def pegar_gps():
    try:
        resposta = requests.get('http://ip-api.com/json/')
        dados = resposta.json()
        latitude = dados['lat']
        longitude = dados['lon']
        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        registro = f"{hora} | Latitude: {latitude}, Longitude: {longitude}\n"
        print("GPS registrado:", registro)
        
        with open('dados_gps.txt', 'a') as arquivo:
            arquivo.write(registro)
    except Exception as e:
        print("Erro ao capturar GPS:", e)

if __name__ == "__main__":
    pegar_gps()

