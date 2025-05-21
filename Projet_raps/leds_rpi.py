import RPi.GPIO as GPIO
import atexit

GPIO.setmode(GPIO.BCM)

leds = {
    "chambre": 17,
    "salon": 27,
    "cuisine": 22
}


for pin in leds.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  

def appliquer_ordres(ordres):
    for nom, etat in ordres.items():
        pin = leds.get(nom)
        if pin is not None:
            if etat == "ON":
                GPIO.output(pin, GPIO.HIGH)
            else:
                GPIO.output(pin, GPIO.LOW)

def eteindre_toutes_les_leds():
    for pin in leds.values():
        GPIO.output(pin, GPIO.LOW)

def fermer_gpio():
    eteindre_toutes_les_leds()
    GPIO.cleanup()
    print(" GPIO nettoye et LEDs eteintes.")

# Nettoyage auto  la fin du programme
atexit.register(fermer_gpio)
