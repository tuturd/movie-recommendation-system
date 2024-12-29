import sqlite3
import src.database.utils.connection as db


class LoginError(Exception):
    """
    Exception raised for errors during login.

    Parameters:
    -----------
    error : str
        A string representing the error type.
    message : str
        A detailed message explaining the error.

    Raises:
    -------
    LoginError
        If there is an error during the login process.
    """

    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def login(username: str) -> bool:
    """
    Authenticates a user by their username.

    Parameters:
    -----------
    username : str
        The username of the user attempting to log in.

    Returns:
    --------
    bool
        True if the username exists in the database, False otherwise.

    Raises:
    -------
    LoginError
        If there is an operational error during the retrieval process.
    """

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
