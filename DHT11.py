# 15 mai 2025 MVL
# voir fichier DHT11.txt pour s'assurer d'avoir le même modèle bleu sans pcb
# voir les branchements à faire et bibliothèques requises
import time
import board
import adafruit_dht
from datetime import datetime

dht = adafruit_dht.DHT11(board.D24)  # ##utiliser le bon GPIO

while True:
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = dht.temperature
        humidity = dht.humidity

        json_dht11 = {"time":now, "temperature":temperature, "humidity":humidity} #gabarit possible JSON pour POST
        print(json_dht11)

        print(f"Température: {temperature}°C  Humidité: {humidity}%")  #valider que ça fonctionne
    except RuntimeError as e:
        print(f"Erreur : {e.args[0]}")
    time.sleep(5)