from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from tkinter import ttk
from src.UI.new_director import NewDirector
from src.UI.new_movie import NewMovie
from src.UI.new_rate import NewRate

if TYPE_CHECKING:
    from src.UI.app import App


class ActionsFrame(ttk.LabelFrame):
    def __init__(self, parent: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Actions'
        )
        self.grid(
            row=1,
            column=0,
            padx=5
        )
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.button_new_movie = ttk.Button(
            self,
            text='Ajouter un film',
            command=self.new_movie_process
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
            command=self.new_director_process
        )
        self.button_new_director.grid(
            row=0,
            column=1,
            padx=5
        )

        self.button_new_rate = ttk.Button(
            self,
            text='Noter un film',
            command=self.new_rate_process
        )
        self.button_new_rate.grid(
            row=0,
            column=2,
            padx=5
        )

    def disable(self):
        self.button_new_movie['state'] = 'disable'
        self.button_new_director['state'] = 'disable'
        self.button_new_rate['state'] = 'disable'

    def new_director_process(self):
        self.parent.disable()
        self.new_director = NewDirector(self.parent, self.on_new_director_destroy)
        self.parent.wait_window(self.new_director)

    def on_new_director_destroy(self):
        self.parent.create_widgets()

    def new_movie_process(self):
        self.parent.disable()
        self.new_movie = NewMovie(self.parent, self.on_new_movie_destroy)
        self.parent.wait_window(self.new_movie)

    def on_new_movie_destroy(self):
        self.parent.create_widgets()

    def new_rate_process(self):
        self.parent.disable()
        self.new_rate = NewRate(self.parent, self.on_new_rate_destroy)
        self.parent.wait_window(self.new_rate)

    def on_new_rate_destroy(self):
        self.parent.create_widgets()
