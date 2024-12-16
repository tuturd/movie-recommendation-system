import sqlite3
import src.database.utils.connection as db


class DirectorError(Exception):
    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def insert(firstname: str, lastname: str) -> None:
    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                INSERT INTO director(firstname, lastname)
                VALUES (?, ?);
            """,
            (
                firstname,
                lastname,
            )
        )

        conn.commit_and_close()

    except sqlite3.OperationalError as e:
        raise DirectorError(e, 'Erreur lors de la création du réalisateur')
