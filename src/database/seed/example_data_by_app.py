import src.database.utils.connection as db
from src.database.config import SEED_PATH, EXAMPLE_DATA_TABLES


def import_example_data():
    # Connect to the SQLite database
    conn = db.open_connection()
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
