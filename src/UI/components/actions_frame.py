from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from src.UI.new_director import NewDirector
from src.UI.new_movie import NewMovie
from src.UI.new_rate import NewRate

if TYPE_CHECKING:
    from src.UI.app import App


class ActionsFrame(ttk.LabelFrame):
    """
    A class representing the actions frame for the Movie Recommendation System.

    Attributes:
    -----------
    app : App
        The main application instance.
    button_new_movie : ttk.Button
        Button to add a new movie.
    button_new_director : ttk.Button
        Button to add a new director.
    button_new_rate : ttk.Button
        Button to rate a movie.

    Methods:
    --------
    __init__(parent: ttk.Frame, app: App):
        Initializes the actions frame with the given parent and app.
    create_widgets():
        Creates and arranges the widgets in the actions frame.
    disable():
        Disables all buttons in the actions frame.
    __new_director_process():
        Initiates the process to add a new director.
    __on_new_director_destroy():
        Callback function to handle the destruction of the new director window.
    __new_movie_process():
        Initiates the process to add a new movie.
    __on_new_movie_destroy():
        Callback function to handle the destruction of the new movie window.
    __new_rate_process():
        Initiates the process to rate a movie.
    __on_new_rate_destroy():
        Callback function to handle the destruction of the new rate window.
    """

    def __init__(self, parent: ttk.Frame, app: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Actions',
        )
        self.grid(
            row=0,
            column=0,
            padx=10,
        )
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the actions frame."""

        self.button_new_movie = ttk.Button(
            self,
            text='Ajouter un film',
            command=self.__new_movie_process
        )
        self.button_new_movie.grid(
            row=0,
            column=0,
            pady=5,
            padx=5
        )

        self.button_new_director = ttk.Button(
            self,
            text='Ajouter un réalisateur',
            command=self.__new_director_process
        )
        self.button_new_director.grid(
            row=0,
            column=1,
            padx=5
        )

        self.button_new_rate = ttk.Button(
            self,
            text='Noter un film',
            command=self.__new_rate_process
        )
        self.button_new_rate.grid(
            row=0,
            column=2,
            padx=5
        )

    def disable(self):
        """Disables all buttons in the actions frame."""

        self.button_new_movie['state'] = 'disable'
        self.button_new_director['state'] = 'disable'
        self.button_new_rate['state'] = 'disable'

    def __new_director_process(self):
        """Initiates the process to add a new director."""

        self.app.disable()
        self.new_director = NewDirector(self.app, self.__on_new_director_destroy)
        self.app.wait_window(self.new_director)

    def __on_new_director_destroy(self):
        """Callback function to handle the destruction of the new director window."""

        self.app.create_widgets()
        self.app.refresh_movies()

    def __new_movie_process(self):
        """Initiates the process to add a new movie."""

        self.app.disable()
        self.new_movie = NewMovie(self.app, self.__on_new_movie_destroy)
        self.app.wait_window(self.new_movie)

    def __on_new_movie_destroy(self):
        """Callback function to handle the destruction of the new movie window."""

        self.app.create_widgets()
        self.app.refresh_movies()

    def __new_rate_process(self):
        """Initiates the process to rate a movie."""

        self.app.disable()
        self.new_rate = NewRate(self.app, self.__on_new_rate_destroy)
        self.app.wait_window(self.new_rate)

    def __on_new_rate_destroy(self):
        """Callback function to handle the destruction of the new rate window."""

        self.app.create_widgets()
        self.app.refresh_movies()
