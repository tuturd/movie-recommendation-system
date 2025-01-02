import src.database.utils.connection as db
from src.classes.genre import PyGenre


class GenreError(Exception):
    """
    Exception raised for errors related to the Genre entity.

    Parameters:
    -----------
    error : str
        A string representing the error type or code.
    message : str
        A detailed message describing the error.

    Raises:
    -------
    GenreError
        If there is an error related to the Genre entity.
    """

    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def get_all() -> list[PyGenre]:
    """
    Retrieve all genres from the database.

    Returns:
    --------
    list[PyGenre]
        A list of all genres in the database.
    """

    conn = db.open_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT id, name FROM genre;
        """
    )

    genres = cursor.fetchall()
    conn.close()

    return [
        PyGenre(
            id=genre[0],
            name=genre[1]
        )
        for genre in genres
    ]
