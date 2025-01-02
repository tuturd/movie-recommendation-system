from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from src.UI.new_rate import NewRate

if TYPE_CHECKING:
    from src.classes.user_movie import UserMovie
    from src.UI.app import App
    from src.UI.components.category_frame import CategoryFrame


class MovieFrame(ttk.Frame):
    """
    A class representing a frame for displaying movie information in the Movie Recommendation System.

    Attributes:
    -----------
    parent : CategoryFrame
        The parent frame to which this frame belongs.
    _app : App
        The main application instance.
    user_movie : UserMovie
        The user-specific movie data to be displayed.
    label_title : ttk.Label
        A label widget to display the movie title.
    label_director : ttk.Label
        A label widget to display the movie director.
    label_rate : ttk.Label
        A label widget to display the average rating of the movie.
    label_date_and_price : ttk.Label
        A label widget to display the release date and price of the movie.
    button_rate : ttk.Button
        A button widget to initiate the rating process for the movie.

    Methods:
    --------
    __init__(parent: CategoryFrame, app: App, user_movie: UserMovie, **kwargs):
        Initializes the movie frame with the given parent, app, and user_movie data.
    create_widgets():
        Creates and arranges the widgets in the movie frame.
    __new_rate_process():
        Initiates the process for rating the movie.
    __on_new_rate_destroy():
        Callback function to handle the destruction of the rating window.
    disable() -> None:
        Disables the rate button.
    """

    def __init__(self, parent: CategoryFrame, app: App, user_movie: UserMovie, **kwargs):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
        )
        self.grid(
            row=kwargs.get('row', 2),
            column=kwargs.get('column', 0),
            padx=kwargs.get('padx', 5),
            pady=kwargs.get('pady', (0, 5)),
            sticky='nsew'
        )
        self.parent = parent
        self._app = app
        self.user_movie = user_movie
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the movie frame."""

        self.label_title = ttk.Label(
            self,
            text=f'{self.user_movie.movie.title}',
            anchor=tk.W,
            justify=tk.LEFT
        )
        self.label_title.grid(
            row=0,
            column=0,
            sticky=tk.W
        )

        self.label_director = ttk.Label(
            self,
            text=self.user_movie.movie.director,
            anchor=tk.W,
            justify=tk.LEFT
        )
        self.label_director.grid(
            row=1,
            column=0,
            sticky=tk.W
        )

        self.label_rate = ttk.Label(
            self,
            text=f'Note moyenne : {self.user_movie.rating}/5',
            anchor=tk.W,
            justify=tk.LEFT
        )
        self.label_rate.grid(
            row=2,
            column=0,
            sticky=tk.W
        )

        self.label_date_and_price = ttk.Label(
            self,
            text=f'{self.user_movie.movie.release_date} - {self.user_movie.movie.price}€',
            anchor=tk.W,
            justify=tk.LEFT
        )
        self.label_date_and_price.grid(
            row=3,
            column=0,
            sticky=tk.W
        )

        self.button_rate = ttk.Button(
            self,
            text='Noter',
            command=self.__new_rate_process
        )
        self.button_rate.grid(
            row=0,
            column=1,
            rowspan=4,
            padx=5
        )

    def __new_rate_process(self):
        """Initiate the process for rating the movie."""

        self._app.disable()
        self.new_rate = NewRate(self._app, self.__on_new_rate_destroy, self.user_movie.movie.id)
        self._app.wait_window(self.new_rate)

    def __on_new_rate_destroy(self):
        """Callback function to handle the destruction of the rating window."""

        self._app.create_widgets()

    def disable(self) -> None:
        """Disables the rate button."""

        self.button_rate['state'] = 'disable'
