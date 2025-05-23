# supervision_de_composants
 

# pour tester l'interface:
    1- Démarer à l'aide de la commande: ''node serveur.js'' sur bash
    2- Cliquer à l'aide de control sur le lien localhost généré dans le terminal

# pour utiliser le code client Python

    1- Installer l'environnement virtuel: `python -m venv ./{nom_fichier_venv}`
    2- Activer l'environement virtuel: `source {nom_fichier_venv}/bin/activate`
    3- Installer les packages python: `pip install -r requirements.txt`
    4- Entrer dans le dossier "Projets_raps": `cd Projets_raps`
    5- Ajouter l'IP du serveur dans le fichier "communication.py" où il est écrit '<VOTRE_ADDRESSE_IP>'
    6- Lancer le fichier "interface.py": `python interface.py`

# arborescence
/
    -serveur.js (fichier du serveur)

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
        -JSON-LED-STATE.json (suggestion pour demander état des leds)
        -JSON-MESURES.json (suggestion pour mesures temp/humidité)

    --public
        -index.css (copie du fichier CSS)
        -index.html (tableau de bord)
        -page1.html (données)
        -page2.html (États des LEDs)
        -page3.html (Contrôles des LEDs)
        P.S. CSS intégré au code HTML