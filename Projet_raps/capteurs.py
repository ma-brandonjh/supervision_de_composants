import random
from datetime import datetime

def generer_mesures():
    temperature = round(random.uniform(20.0, 30.0), 1)
    humidite = random.randint(20, 70)
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "time": horodatage,
        "temperature": temperature,
        "humidity": humidite
    }
