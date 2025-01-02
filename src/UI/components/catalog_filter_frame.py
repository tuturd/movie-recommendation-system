from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

import src.database.utils.director as DirectorUtils
import src.database.utils.genre as GenreUtils
import src.database.utils.movie as MovieUtils

if TYPE_CHECKING:
    from src.UI.app import App
    from src.UI.catalog import Catalog


class CatalogFilterFrame(ttk.LabelFrame):
    """
    A class representing the filter frame for the Movie Recommendation System.

    Attributes:
    -----------
    app : App
        The main application instance.
    parent : Catalog
        The parent catalog instance.
    _all_directors : list
        List of all directors from the database.
    _all_genres : list
        List of all genres from the database.
    _all_movies : list
        List of all movies from the database.
    combo_genre : ttk.Combobox
        Combobox widget for selecting genres.
    combo_director : ttk.Combobox
        Combobox widget for selecting directors.
    button_submit : ttk.Button
        Button widget to submit the filters.

    Methods:
    --------
    __init__(parent: Catalog, app: App):
        Initializes the filter frame with the given parent and app instance.
    create_widgets():
        Creates and arranges the widgets in the filter frame.
    on_submit():
        Handles the submission of the filters and performs the necessary actions.
    """

    def __init__(self, parent: Catalog, app: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Filtres',
        )
        self.grid(
            row=0,
            column=2,
            padx=5
        )
        self.app = app
        self.parent = parent
        self._all_directors = DirectorUtils.get_all()
        self._all_genres = GenreUtils.get_all()
        self._all_movies = MovieUtils.get_all()

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the filter frame."""

        self.combo_genre = ttk.Combobox(
            self,
            values=[
                'Tous',
                *[
                    genre.name
                    for genre in self._all_genres
                ]
            ]
        )
        self.combo_genre.grid(
            row=0,
            column=0,
            padx=10,
        )

        self.combo_director = ttk.Combobox(
            self,
            values=[
                'Tous',
                *[
                    f'{director.firstname} {director.lastname}'
                    for director in self._all_directors
                ]
            ]
        )
        self.combo_director.grid(
            row=0,
            column=1,
            padx=10,
        )

        self.button_submit = ttk.Button(
            self,
            text='Rafraichir',
            command=self.on_submit,
        )
        self.button_submit.grid(
            row=0,
            column=2,
            padx=10
        )

        self.parent.movies_to_display = self._all_movies

    def on_submit(self):
        """Handle the submission of the filters and perform the necessary actions."""

        # Add 1 because of 'Tous' element at the begin of the lists
        genre_id: int = self.combo_genre.current() - 1
        director_id: int = self.combo_director.current() - 1

        movie_to_display = self._all_movies

        if genre_id not in [-2, -1]:  # To exclude the blank and 'Tous' answers
            movie_to_display = [
                movie
                for movie in movie_to_display
                if movie.genre_id == self._all_genres[genre_id].id
            ]

        if director_id not in [-2, -1]:  # To exclude the blank and 'Tous' answers
            movie_to_display = [
                movie
                for movie in movie_to_display
                if movie.director_id == self._all_directors[director_id].id
            ]

        self.parent.movies_to_display = movie_to_display
        self.parent.refresh_movies()
