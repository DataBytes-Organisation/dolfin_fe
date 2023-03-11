import os
from os.path import join, dirname
from dotenv import load_dotenv

os.environ["ENVIRONMENT_FILE"] = ".env.development"

dotenv_path = os.path.join(dirname(__file__), os.getenv("ENVIRONMENT_FILE"))

load_dotenv(dotenv_path=dotenv_path, override=True)

application_HOST = os.environ.get("HOST")
application_PORT = int(os.environ.get("PORT"))
application_DEBUG = bool(os.environ.get("DEBUG"))
DEV_TOOLS_PROPS_CHECK = bool(os.environ.get("DEV_TOOLS_PROPS_CHECK"))
base_api_url = os.environ.get("BASE_API_URL")