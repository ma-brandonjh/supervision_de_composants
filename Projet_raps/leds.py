from gpiozero import LED


leds = {
    "chambre": LED(17),
    "salon": LED(27),
    "cuisine": LED(22)
}

def appliquer_ordres(ordres):
    for nom, etat in ordres.items():
        led = leds.get(nom)
        if led:
            if etat == "ON":
                led.on()
            else:
                led.off()
