import json
from src.config import FICHIER_SAUVEGARDE


def sauvegarder_suivi(donnees):
    with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=4, ensure_ascii=False)