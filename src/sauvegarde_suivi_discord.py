from datetime import datetime
import json
import requests
from src.config import DISCORD_WEBHOOK_URL, FICHIER_SAUVEGARDE

def sauvegarder_suivi(donnees):
    with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)

def envoyer_discord(manga_nom, chapitres):
    if not chapitres:
        return
    
    if len(chapitres) == 1:
        desc = f"Le **{chapitres[0]['nom']}** est disponible !"
        lien = chapitres[0]['lien']
    else:
        desc = f" **{len(chapitres)} chapitres sortis !**\n"
        for chap in reversed(chapitres):
            desc += f"- {chap['nom']}\n"
        lien = chapitres[0]['lien']

    embed = {
        "title": f"Nouveau sur {manga_nom} !",
        "description": desc,
        "url": lien,
        "color": 5814783,
        "footer": {"text": "Japscan Bot • " + datetime.now().strftime("%H:%M")},
        "thumbnail": {"url": "https://www.japscan.vip/imgs/japscan_logo_new.png"} 
    }

    data = {
        "username": "Japscan Bot",
        "embeds": [embed]
    }

    try:
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Erreur envoi Discord : {e}")