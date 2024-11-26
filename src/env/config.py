from dotenv import load_dotenv
load_dotenv()
import os
from pathlib import Path

APP_PATH = Path(__file__).parent.parent.parent
DB_PATH = APP_PATH / os.environ.get('DB_PATH')
SEED_PATH = APP_PATH / os.environ.get('SEED_PATH')
