import sqlite3
from config import DB_PATH, SEED_PATH


def seed_database():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Read the SQL seed file
    with open(SEED_PATH / 'seed.sql', 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    cursor.executescript(sql_script)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
