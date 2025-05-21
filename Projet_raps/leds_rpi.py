import lgpio
import atexit  # Pour executer automatiquement a la fermeture

# Ouvre le chip GPIO 0
chip = lgpio.gpiochip_open(0)


leds = {
    "chambre": 17,
    "salon": 27,
    "cuisine": 22
}

# Configure chaque pin comme sortie
for pin in leds.values():
    lgpio.gpio_claim_output(chip, pin)

def appliquer_ordres(ordres):
    for nom, etat in ordres.items():
        pin = leds.get(nom)
        if pin is not None:
            if etat == "ON":
                lgpio.gpio_write(chip, pin, 1)
            else:
                lgpio.gpio_write(chip, pin, 0)

def eteindre_toutes_les_leds():
    for pin in leds.values():
        lgpio.gpio_write(chip, pin, 0)

def fermer_gpio():
    eteindre_toutes_les_leds()  
    lgpio.gpiochip_close(chip)
    print("?? Connexion GPIO fermre proprement.")

# Enregistre la fonction de fermeture a excuter automatiquement a la fin
atexit.register(fermer_gpio)
