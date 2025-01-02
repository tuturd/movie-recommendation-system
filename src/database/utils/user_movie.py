import sqlite3

import src.database.utils.connection as db
from src.classes.user_movie import UserMovie


class UserMovieError(Exception):
    """
    Exception raised for errors related to user-movie interactions.

    Parameters:
    -----------
    error : str
        The error code or identifier.
    message : str
        A detailed description of the error.
    """

    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def insert(user_movie: UserMovie) -> None:
    """
    Inserts a UserMovie record into the database.

    Parameters:
    -----------
    user_movie : UserMovie
        An instance of UserMovie containing the details to be inserted.

    Raises
    -------
    UserMovieError
        If there is an operational error during the insertion process.
    """

    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                INSERT INTO userMovie(userId, movieId, rating, sold, saleDate)
                VALUES (?, ?, ?, ?, ?);
            """,
            (
                user_movie.user_id,
                user_movie.movie_id,
                user_movie.rating,
                user_movie.sold,
                user_movie.sale_date
            )
        )

        conn.commit_and_close()

    except sqlite3.OperationalError as e:
        raise UserMovieError(e, 'Erreur lors de la récupération du film')


def get_len(user_id: int) -> int:
    """
    Get the number of UserMovie records for a specific user.

    Parameters:
    -----------
    user_id : int
        The ID of the user.

    Returns:
    --------
    int
        The number of UserMovie records for the specified user.
    """

    conn = db.open_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT COUNT(*)
            FROM userMovie
            WHERE userId = ?;
        """,
        (user_id,)
    )

    count = cursor.fetchone()[0]
    conn.close()

    return count
