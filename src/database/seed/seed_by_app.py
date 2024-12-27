import src.database.utils.connection as db
from src.database.config import SEED_PATH


def seed_database():
    # Connect to the SQLite database
    conn = db.open_connection()
    cursor = conn.cursor()

    # Read the SQL seed file
    with open(SEED_PATH / 'seed.sql', 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    cursor.executescript(sql_script)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
