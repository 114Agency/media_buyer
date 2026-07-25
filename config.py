from dotenv import load_dotenv
from dynaconf import Dynaconf

# Charge le fichier .env dans l'environnement global (Indispensable pour le SDK Langfuse)
load_dotenv()

# Initialise Dynaconf
settings = Dynaconf(
    envvar_prefix="MEDIA_BUYER",
    settings_files=['settings.toml'],
)