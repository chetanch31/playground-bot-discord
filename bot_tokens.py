import imp
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

discord_bot_token = os.environ['CLIENT_KEY']
google_api_key = os.environ['GOOGLE_API']
google_cse_key = os.environ['GOOGLE_CSE']
weather_api_key = os.environ['WEATHER_API']
reddit_client_id = os.environ['REDDIT_CLIENT']
reddit_client_secret = os.environ['REDDIT_CLIENT_SECRET']
