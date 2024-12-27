import sqlite3
from config import DB_PATH, SEED_PATH, EXAMPLE_DATA_TABLES


def import_example_data():
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Read the SQL seed file
    for table in EXAMPLE_DATA_TABLES:
        # Read the SQL seed file
        with open(SEED_PATH / f'{table}.sql', 'r') as file:
            sql_script = file.read()

        # Execute the SQL script
        cursor.executescript(sql_script)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
