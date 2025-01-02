from __future__ import annotations

import tkinter as tk
from datetime import datetime
from tkinter import ttk
from typing import TYPE_CHECKING

import src.database.utils.movie as MovieUtils
import src.database.utils.user_movie as UserMovieUtils
from src.classes.movie import EmptyMovie, Movie
from src.classes.user_movie import UserMovie
from src.utils.logging import get_logger

if TYPE_CHECKING:
    from src.UI.app import App

logger = get_logger(__name__)


class NewRate(tk.Toplevel):
    """
    A class to create a new rating window for the Movie Recommendation System.

    Attributes:
    -----------
    parent : App
        The parent application instance.
    on_destroy : function
        The callback function to be called when the window is closed.
    movie_id : int, optional
        The ID of the movie to be rated (default is None).
    movie : Movie or EmptyMovie
        The movie instance to be rated.
    _all_movies : list
        A list of all unrated movies for the user.

    Methods:
    --------
    __init__(parent: App, on_destroy, movie_id: int = None):
        Initializes the NewRate window.
    create_widgets():
        Creates and arranges the widgets in the window.
    on_submit(e=None) -> None:
        Handles the submission of the rating.
    close() -> None:
        Closes the window and calls the on_destroy callback.
    __get_movie(movie_id) -> Movie | EmptyMovie:
        Retrieves the movie instance based on the movie_id.
    __movie_update(e=None) -> None:
        Enables the submit button when a movie is selected from the combobox.
    """

    def __init__(self, parent: App, on_destroy, movie_id: int = None):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Nouvelle note - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)

        self.parent = parent
        self.movie = self.__get_movie(movie_id)
        self._all_movies = MovieUtils.get_unrated_movies(self.parent.user)

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the window."""

        self.label = ttk.Label(
            self,
            text=(
                f'Ajouter une note à {self.movie.title}'
                if isinstance(self.movie, Movie)
                else 'Choisir un film ci-dessous'
            )
        )
        self.label.grid(
            row=0,
            column=0,
            columnspan=6,
            pady=20
        )

        self.movie_combo = ttk.Combobox(
            self,
            values=[
                f'{movie.title} - {movie.director}'
                for movie in self._all_movies
            ]
        )
        self.movie_combo.grid(
            row=1,
            column=0,
            columnspan=6,
            padx=10,
            pady=10,
            sticky='nsew'
        )
        self.movie_combo.bind('<<ComboboxSelected>>', self.__movie_update)

        self.label = ttk.Label(
            self,
            text='Note :'
        )
        self.label.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        self._rate = tk.IntVar()
        self._rate.set(3)

        self.c0 = tk.Checkbutton(
            self,
            text='0',
            variable=self._rate,
            onvalue=0
        )
        self.c1 = tk.Checkbutton(
            self,
            text='1',
            variable=self._rate,
            onvalue=1
        )
        self.c2 = tk.Checkbutton(
            self,
            text='2',
            variable=self._rate,
            onvalue=2
        )
        self.c3 = tk.Checkbutton(
            self,
            text='3',
            variable=self._rate,
            onvalue=3
        )
        self.c4 = tk.Checkbutton(
            self,
            text='4',
            variable=self._rate,
            onvalue=4
        )
        self.c5 = tk.Checkbutton(
            self,
            text='5',
            variable=self._rate,
            onvalue=5
        )

        self.c0.grid(row=3, column=0, padx=10, pady=10)
        self.c1.grid(row=3, column=1, padx=10, pady=10)
        self.c2.grid(row=3, column=2, padx=10, pady=10)
        self.c3.grid(row=3, column=3, padx=10, pady=10)
        self.c4.grid(row=3, column=4, padx=10, pady=10)
        self.c5.grid(row=3, column=5, padx=10, pady=10)

        self.button = ttk.Button(
            self,
            text='Valider',
            state='disable',
            command=self.on_submit
        )
        self.button.grid(
            row=4,
            column=0,
            columnspan=6,
            pady=10,
            sticky='ew'
        )

        if isinstance(self.movie, Movie):
            self.movie_combo.set(f'{self.movie.title} - {self.movie.director}')
            self.movie_combo['state'] = 'disable'
            self.button['state'] = 'normal'

    def on_submit(self, e=None) -> None:
        """Handle the submission of the rating."""

        UserMovieUtils.insert(UserMovie(
            user_id=self.parent.user.id,
            movie_id=self._all_movies[self.movie_combo.current()].id,
            rating=self._rate.get(),
            sold=True,
            sale_date=int(datetime.now().timestamp())
        ))
        self.close()

    def close(self) -> None:
        """Close the window and call the on_destroy callback."""

        self.destroy()
        self.on_destroy()

    def __get_movie(self, movie_id) -> Movie | EmptyMovie:
        """Retrieve the movie instance based on the movie_id."""

        if movie_id:
            return MovieUtils.get(movie_id)
        return EmptyMovie()

    def __movie_update(self, e=None) -> None:
        """Enable the submit button when a movie is selected from the combobox."""

        self.button.config(state='normal')
