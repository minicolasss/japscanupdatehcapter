import os


# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FICHIER_LISTE = os.path.join(BASE_DIR, "data", "mes_mangas.txt")
FICHIER_SAUVEGARDE = os.path.join(BASE_DIR, "data", "suivi_chapitres.json")
FLARESOLVERR_URL = "http://localhost:8191/v1" # URL de FlareSolverr
DISCORD_WEBHOOK_URL = "fed"


# --- COULEURS TERMINAL ---
VERT = "\033[92m"
JAUNE = "\033[93m"
ROUGE = "\033[91m"
BLEU = "\033[94m"
RESET = "\033[0m"