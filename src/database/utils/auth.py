import sqlite3
import src.database.utils.connection as db


class LoginError(Exception):
    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def login(username: str) -> bool:
    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            'SELECT username FROM user WHERE username = ?',
            (username,)
        )

        result = cursor.fetchone() is not None

        conn.commit_and_close()

        return result

    except sqlite3.OperationalError as e:
        raise LoginError(e, "Erreur lors de la récupération de l'utilisateur")
