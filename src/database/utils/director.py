import sqlite3

import src.database.utils.connection as db
from src.classes.director import PyDirector


class DirectorError(Exception):
    """
    Exception raised for errors related to the Director entity.

    Parameters:
    -----------
    error : str
        A string representing the error type or code.
    message : str
        A detailed message describing the error.

    Raises:
    -------
    DirectorError
        If there is an error related to the Director entity.
    """

    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def insert(firstname: str, lastname: str) -> None:
    """
    Insert a new director into the database.

    Parameters:
    -----------
    firstname : str
        The first name of the director.
    lastname : str
        The last name of the director.

    Raises:
    -------
    DirectorError
        If there is an operational error during the insertion process.
    """

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


def get_all() -> list[PyDirector]:
    """
    Retrieve all directors from the database.

    Returns:
    --------
    list[Director]
        A list of all directors in the database.
    """

    conn = db.open_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT id, firstname, lastname FROM director;
        """
    )

    directors = cursor.fetchall()
    conn.close()

    return [
        PyDirector(
            id=director[0],
            firstname=director[1],
            lastname=director[2]
        )
        for director in directors
    ]
