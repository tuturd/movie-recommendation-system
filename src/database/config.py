from pathlib import Path

__current_path = Path(__file__).parent

DB_PATH = __current_path / 'app.db'
SEED_PATH = __current_path / 'seed'

EXAMPLE_DATA_TABLES = [
    'user',
    'director',
    'genre',
    'movie',
    'userMovie',
]
