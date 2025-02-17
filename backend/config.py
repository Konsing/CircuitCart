import os
from pathlib import Path
from dotenv import load_dotenv

# Set the base directory to the /backend folder.
BASE_DIR = Path(__file__).resolve().parent

# Get the current environment; default to development.
env_name = os.environ.get("DJANGO_ENV", "development")

if env_name != "production":
    # For non-production environments, load the appropriate .env file.
    env_file = BASE_DIR / (".env.prod" if env_name == "production" else ".env.dev")
    if not env_file.exists():
        raise FileNotFoundError(f"Environment file {env_file} not found.")
    load_dotenv(dotenv_path=env_file)
else:
    # In production, we assume environment variables are provided externally.
    print("Production environment detected. Skipping .env file load.")

def get_env_variable(name: str) -> str:
    value = os.environ.get(name)
    if value is None:
        raise Exception(f"Environment variable '{name}' is not set. Please check your environment configuration.")
    return value

# Load required configuration variables.
DJANGO_SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "t")
ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS").split(',')
DATABASE_URL = get_env_variable("DATABASE_URL")
CORS_ALLOWED_ORIGINS = get_env_variable("CORS_ALLOWED_ORIGINS")