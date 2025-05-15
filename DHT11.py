# 15 mai 2025 MVL
# voir fichier DHT11.txt pour s'assurer d'avoir le même modèle bleu sans pcb
# voir les branchements et bibliothèques requis
import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D24)  # ##utiliser le bon GPIO

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        print(f"Température: {temperature}°C  Humidité: {humidity}%")
    except RuntimeError as e:
        print(f"Erreur : {e.args[0]}")
    time.sleep(5)