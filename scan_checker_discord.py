import requests
from bs4 import BeautifulSoup
import json
import os
import time
from datetime import datetime
from src.charger_suivi import charger_suivi
from src.sauvegarde_suivi_discord import sauvegarder_suivi
from src.verifier_manga import verifier_manga
from src.config import FICHIER_LISTE
from src.envoyer_discord import envoyer_discord

def main():
    print(f"[{datetime.now().strftime('%d/%m %H:%M')}] Lancement du scan...")
    
    if not os.path.exists(FICHIER_LISTE):
        print("Fichier de liste introuvable.")
        return

    with open(FICHIER_LISTE, "r") as f:
        mangas = [line.strip() for line in f if line.strip()]

    suivi = charger_suivi()
    sauvegarde_necessaire = False

    for url in mangas:
        nom_manga = url.strip('/').split('/')[-1].replace('-', ' ').title()
        dernier_lu = suivi.get(url)
        
        nouveautes = verifier_manga(url, dernier_lu)

        if nouveautes:
            print(f"--> Nouveautés pour {nom_manga} ({len(nouveautes)})")
            
            # Envoi de la notif Discord
            envoyer_discord(nom_manga, nouveautes)
            
            # Mise à jour du suivi (on prend le plus récent qui est à l'index 0)
            suivi[url] = nouveautes[0]['nom']
            sauvegarde_necessaire = True
        else:
            # Si c'est la première fois qu'on lance le script pour ce manga
            # on initialise sans envoyer de notif pour ne pas spammer
            if url not in suivi:
                # On fait une requete rapide pour choper le dernier
                init = verifier_manga(url, "FORCE_INIT")
                if init:
                    suivi[url] = init[0]['nom']
                    sauvegarde_necessaire = True
                    print(f"--> {nom_manga} ajouté à la base de données.")

    if sauvegarde_necessaire:
        sauvegarder_suivi(suivi)
        print("Base de données mise à jour.")
    else:
        print("Rien de nouveau.")

if __name__ == "__main__":
    main()