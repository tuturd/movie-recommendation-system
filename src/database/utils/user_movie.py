import sqlite3
import src.database.utils.connection as db
from src.classes.user_movie import UserMovie


class UserMovieError(Exception):
    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def insert(user_movie: UserMovie) -> None:
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
