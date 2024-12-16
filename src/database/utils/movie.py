from __future__ import annotations
from typing import TYPE_CHECKING
import sqlite3
import src.database.utils.connection as db
from src.classes.movie import Movie, MovieTitleAndDirector
from src.database.utils.user import User
from src.database.utils.user_movie import UserMovie

if TYPE_CHECKING:
    from src.database.utils.jaccard import ResultatSimilarite


class MovieError(Exception):
    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def get(id: int) -> Movie:
    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                SELECT movie.id, movie.title, movie.releaseDate, movie.price, director.firstname, director.lastname, genre.name FROM movie
                JOIN director ON movie.directorId = director.id
                JOIN genre ON movie.genreId = genre.id
                WHERE movie.id = ?
            """,
            (id,)
        )

        data = cursor.fetchone()

        result = Movie(
            id=data[0],
            title=data[1],
            release_date=data[2],
            price=data[3],
            director=f'{data[4]} {data[5]}',
            genre=data[6],
        )

        conn.commit_and_close()

        return result

    except sqlite3.OperationalError as e:
        raise MovieError(e, 'Erreur lors de la récupération du film')


def get_all() -> list[MovieTitleAndDirector]:
    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                SELECT movie.id, movie.title, director.firstname, director.lastname FROM movie
                JOIN director ON movie.directorId = director.id
            """
        )

        data = cursor.fetchall()

        conn.commit_and_close()

        return [
            MovieTitleAndDirector(
                id=movie[0],
                title=movie[1],
                director=f'{movie[2]} {movie[3]}'
            )
            for movie in data
        ]

    except sqlite3.OperationalError as e:
        raise MovieError(e, 'Erreur lors de la récupération des films')


def get_unrated_movies(user: User) -> list[MovieTitleAndDirector]:
    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                SELECT movie.id, movie.title, director.firstname, director.lastname FROM movie
                JOIN director ON movie.directorId = director.id
                WHERE movie.id NOT IN (
                    SELECT movieId FROM userMovie WHERE userId = ?
                )
            """,
            (user.id,)
        )

        data = cursor.fetchall()

        conn.commit_and_close()

        return [
            MovieTitleAndDirector(
                id=movie[0],
                title=movie[1],
                director=f'{movie[2]} {movie[3]}'
            )
            for movie in data
        ]

    except sqlite3.OperationalError as e:
        raise MovieError(e, 'Erreur lors de la récupération des films non notés')


def update(movie: Movie) -> None:
    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                UPDATE movie
                SET title, releaseDate, price FROM movie
                WHERE id
            """,
            (movie.title, movie.release_date, movie.price)
        )

        data = cursor.fetchall()

        conn.commit_and_close()

        return [
            MovieTitleAndDirector(
                id=movie[0],
                title=movie[1],
                director=f'{movie[2]} {movie[3]}'
            )
            for movie in data
        ]

    except sqlite3.OperationalError as e:
        raise MovieError(e, 'Erreur lors de la récupération des films')


def get_movies_to_recommend(nearest_users: list[ResultatSimilarite], user: User) -> list[UserMovie]:
    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            f"""
            SELECT userMovie.id, userMovie.userId, userMovie.movieId, userMovie.rating, userMovie.sold, userMovie.saleDate, movie.id, movie.title, movie.releaseDate, movie.price, director.firstname, director.lastname, genre.name FROM userMovie
            JOIN movie ON userMovie.movieId = movie.id
            JOIN director ON movie.directorId = director.id
            JOIN genre ON movie.genreId = genre.id
            WHERE userMovie.userId IN ({','.join('?' for _ in nearest_users)})
            AND userMovie.userId != ?
            AND NOT EXISTS (
                SELECT 1 FROM userMovie um
                WHERE um.movieId = userMovie.movieId
                AND um.userId = ?
            )
            """,
            (
                *[
                    user.user_id
                    for user in nearest_users
                ],
                user.id,
                user.id,
            )
        )

        data = cursor.fetchall()

        conn.commit_and_close()

        return [
            UserMovie(
                id=movie[0],
                user_id=movie[1],
                movie_id=movie[2],
                rating=movie[3],
                sold=movie[4],
                sale_date=movie[5],
                movie=Movie(
                    id=movie[6],
                    title=movie[7],
                    release_date=movie[8],
                    price=movie[9],
                    director=f'{movie[10]} {movie[11]}',
                    genre=movie[12],
                )
            )
            for movie in data
        ]

    except sqlite3.OperationalError as e:
        raise MovieError(e, 'Erreur lors de la récupération du film')
