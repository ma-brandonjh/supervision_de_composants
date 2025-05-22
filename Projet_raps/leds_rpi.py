import RPi.GPIO as GPIO

class LED_RPi():
    leds = {
        "chambre": 17,
        "salon": 27,
        "cuisine": 22
    }

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
    
    def setup(self):
        for pin in self.leds.values():
            GPIO.setup(pin, GPIO.OUT)

    def appliquer_ordres(self, ordres):
        for nom, etat in ordres.items():
            pin = self.leds.get(nom)
            if pin is not None:
                if etat == "on":
                    GPIO.output(pin, GPIO.HIGH)
                else:
                    GPIO.output(pin, GPIO.LOW)

    def eteindre_toutes_les_leds(self):
        for pin in self.leds.values():
            GPIO.output(pin, GPIO.LOW)

    def fermer_gpio(self):
        self.eteindre_toutes_les_leds()
        GPIO.cleanup()
        print(" GPIO nettoye et LEDs eteintes.")
