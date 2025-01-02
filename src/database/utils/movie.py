from __future__ import annotations

import sqlite3
from typing import TYPE_CHECKING

import src.database.utils.connection as db
from src.classes.movie import Movie, MovieTitleAndDirector
from src.classes.user import User
from src.classes.user_movie import UserMovie

if TYPE_CHECKING:
    from src.database.utils.jaccard import ResultatSimilarite


class MovieError(Exception):
    """
    Attributes:
    -----------
    message : str
        Detailed error message describing the cause of the exception.

    Methods:
    --------
    __init__(error: str, message: str):
        Initializes the MovieError with the given error code and message.
    """

    def __init__(self, error: str, message: str):
        self.message = message
        super().__init__(error)


def insert(movie: Movie) -> None:
    """
    Insert a new movie into the database.

    Parameters:
    -----------
    movie : Movie
        The movie object containing the details of the movie to be inserted.

    Raises:
    -------
    MovieError
        If there is an operational error during the insertion process.
    """

    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                INSERT INTO movie(title, releaseDate, price, directorId, genreId)
                VALUES (?, ?, ?, ?, ?);
            """,
            (
                movie.title,
                movie.release_date,
                movie.price,
                movie.director_id,
                movie.genre_id,
            )
        )

        conn.commit_and_close()

    except sqlite3.OperationalError as e:
        raise MovieError(e, 'Erreur lors de la création du film')


def get(id: int) -> Movie:
    """
    Retrieves a movie from the database by its ID.

    Parameters:
    -----------
    id : int
        The ID of the movie to retrieve.

    Returns:
    --------
    Movie
        An instance of the Movie class containing the movie details.

    Raises:
    -------
    MovieError
        If there is an operational error during the retrieval of the movie.
    """

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


def get_all() -> list[Movie]:
    """
    Retrieves all movies along with their directors from the database.

    Methods:
    --------
    get_all():
        Fetches all movies and their corresponding directors from the database.
        Returns a list of Movie objects.

    Returns:
    --------
    list[Movie]
        A list of Movie objects containing the movie details.

    Raises:
    -------
    MovieError
        If there is an operational error during the retrieval of movies.
    """

    conn = db.open_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
                SELECT movie.id, movie.title, movie.releaseDate, movie.price, movie.genreId, movie.directorId, director.firstname, director.lastname FROM movie
                JOIN director ON movie.directorId = director.id
            """
        )

        data = cursor.fetchall()

        conn.commit_and_close()

        return [
            Movie(
                id=movie[0],
                title=movie[1],
                release_date=movie[2],
                price=movie[3],
                genre_id=movie[4],
                director_id=movie[5],
                director=f'{movie[6]} {movie[7]}',
            )
            for movie in data
        ]

    except sqlite3.OperationalError as e:
        raise MovieError(e, 'Erreur lors de la récupération des films')


def get_unrated_movies(user: User) -> list[MovieTitleAndDirector]:
    """
    Retrieves a list of movies that the given user has not rated yet.

    Parameters:
    -----------
    user : User
        The user for whom to retrieve the unrated movies.

    Returns:
    --------
    list[MovieTitleAndDirector]
        A list of MovieTitleAndDirector objects representing the movies that the user has not rated.
    """

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
    """
    Updates the details of a movie in the database.

    Parameters:
    -----------
    movie : Movie
        The movie object containing updated details.

    Raises:
    -------
    MovieError
        If there is an operational error during the update process.
    """

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
    """
    Retrieves a list of movies to recommend to a user based on the preferences of the nearest users.

    Parameters:
    -----------
    nearest_users : list[ResultatSimilarite]
        A list of users who have similar preferences to the target user.
    user : User
        The target user for whom the recommendations are being generated.

    Returns:
    --------
    list[UserMovie]
        A list of UserMovie objects representing the recommended movies.

    Raises:
    -------
    MovieError
        If there is an error during the retrieval of the movies from the database.
    """

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
