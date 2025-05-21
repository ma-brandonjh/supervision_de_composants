# supervision_de_composants
 

# pour tester l'interface:
    1-démarer à l'aide de la commande: ''node serveur.js'' sur bash
    2-cliquer à l'aide de control sur le lien localhost généré dans le terminal

# arborescence
/
    -serveur.js (fichier du serveur)
    -index.css (copie du fichier CSS)

    --Projet_rasp
        -capteurs.py (génération aléatoire des données) ***temp et humidité en string causeront problème???***
        -communication.py (communication avec serveur)
        -interface.py (interface pygame)
        -leds_rpi.py (gestion des GPIOs)
        -leds.py (exécution des commandes)

    --outils
        --module_DHT11
            -DHT11.py (code pour module température et humidité)
            -DHT11.txt (informations sur branchements et bibliothèques)

    --Template_JSON
        -JSON-DHT11 (suggestion pour transmettre informations module temperature-humidité)
        -JSON-LED-CMD.json (suggestion pour commandes des leds)
        -JSON-LED-STATE.json (suggestion pour demander état des leds)
        -JSON-MESURES.json (suggestion pour mesures temp/humidité)

    --public
        -index.html (tableau de bord)
        -page1.html (données)
        -page2.html (États des LEDs)
        -page3.html (Contrôles des LEDs)
        P.S. CSS intégré au code HTML