from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk
from src.UI.new_rate import NewRate


if TYPE_CHECKING:
    from src.UI.components.category_frame import CategoryFrame
    from src.classes.user_movie import UserMovie
    from src.UI.app import App


class MovieFrame(ttk.Frame):
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
        self._app.disable()
        self.new_rate = NewRate(self._app, self.__on_new_rate_destroy, self.user_movie.movie.id)
        self._app.wait_window(self.new_rate)

    def __on_new_rate_destroy(self):
        self._app.create_widgets()

    def disable(self) -> None:
        self.button_rate['state'] = 'disable'
