import requests

# Adresse du serveur (modifie l'IP et port selon ton reseau)
SERVER_URL = "http://192.168.1.100:3000"

def envoyer_mesures(mesures):
    try:
        response = requests.post(f"{SERVER_URL}/donnees", json=mesures)
        print("Donnees envoyees :", mesures)
        print(" Recompense serveur :", response.status_code, response.text)
    except Exception as e:
        print(" Erreur d'envoi :", e)

def recuperer_ordres_leds():
    try:
        response = requests.get(f"{SERVER_URL}/ordre-leds")
        if response.status_code == 200:
            return response.json()
        else:
            print(" Erreur lors de la recuperation :", response.status_code)
            return None
    except Exception as e:
        print(" Erreur de communication :", e)
        return None
