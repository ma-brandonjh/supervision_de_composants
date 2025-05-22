import pygame
import sys
from capteurs import generer_mesures
from communication import envoyer_mesures, recuperer_ordres_leds
from led import appliquer_ordres

pygame.init()
largeur, hauteur = 700, 400
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Client Simulation - Pygame")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS = (200, 200, 200)
BLEU = (0, 0, 255)
GRIS_FONCE = (160, 160, 160)

# Polices
font = pygame.font.SysFont(None, 36)
petite_font = pygame.font.SysFont(None, 28)

# etats
etat_leds = {"chambre": "OFF", "salon": "OFF", "cuisine": "OFF"}
derniere_mesure = ""

# Boutons
bouton_envoyer = pygame.Rect(50, 50, 120, 40)
bouton_recevoir = pygame.Rect(200, 50, 120, 40)

def dessiner_interface():
    fenetre.fill(BLANC)

   
    souris_pos = pygame.mouse.get_pos()

    # Bouton Envoyer
    couleur_envoyer = GRIS_FONCE if bouton_envoyer.collidepoint(souris_pos) else GRIS
    pygame.draw.rect(fenetre, couleur_envoyer, bouton_envoyer)
    fenetre.blit(font.render("Envoyer", True, NOIR), (60, 55))

    # Bouton Recevoir
    couleur_recevoir = GRIS_FONCE if bouton_recevoir.collidepoint(souris_pos) else GRIS
    pygame.draw.rect(fenetre, couleur_recevoir, bouton_recevoir)
    fenetre.blit(font.render("Recevoir", True, NOIR), (210, 55))


    
    y_base = 120
    for i, (nom, etat) in enumerate(etat_leds.items()):
        texte = f"{nom.capitalize()} : {etat}"
        fenetre.blit(font.render(texte, True, NOIR), (50, y_base + i * 40))

    
    if derniere_mesure:
        temp = derniere_mesure.get("temperature", "--")
        hum = derniere_mesure.get("humidite", "--")
        date = derniere_mesure.get("date", "")
        
        texte_mesure = petite_font.render(f"Temperature : {temp} C | Humidite : {hum} %", True, BLEU)
        texte_date = petite_font.render(f"Date : {date}", True, NOIR)

        fenetre.blit(texte_mesure, (50, 280))
        fenetre.blit(texte_date, (50, 310))


    pygame.display.flip()

def boucle_principale():
    global etat_leds, derniere_mesure

    clock = pygame.time.Clock()
    compteur_temps = 0  

    while True:
        dt = clock.tick(30)  
        compteur_temps += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_envoyer.collidepoint(event.pos):
                    mesure = generer_mesures()
                    envoyer_mesures(mesure)
                    derniere_mesure = mesure

                if bouton_recevoir.collidepoint(event.pos):
                    ordres = recuperer_ordres_leds()
                    if ordres:
                        etat_leds = ordres
                        appliquer_ordres(ordres)

        
        if compteur_temps >= 5000:
            compteur_temps = 0
            mesure = generer_mesures()
            envoyer_mesures(mesure)
            derniere_mesure = mesure

            ordres = recuperer_ordres_leds()
            if ordres:
                etat_leds = ordres
                appliquer_ordres(ordres)

        dessiner_interface()
        clock.tick(30)

if __name__ == "__main__":
    boucle_principale()
