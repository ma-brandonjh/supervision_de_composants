
import RPi.GPIO as GPIO
import atexit


GPIO.setmode(GPIO.BCM)


leds = {
    "chambre": 12,
    "salon": 20,
    "cuisine": 21
}


for pin in leds.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def appliquer_ordres(ordres):
    for nom, etat in ordres.items():
        pin = leds.get(nom)
        if pin is not None:
            GPIO.output(pin, GPIO.HIGH if etat == "on" else GPIO.LOW)

def eteindre_toutes_les_leds():
    for pin in leds.values():
        GPIO.output(pin, GPIO.LOW)

def fermer_gpio():
    eteindre_toutes_les_leds()
    GPIO.cleanup()
    print("GPIO libere proprement.")


atexit.register(fermer_gpio)
