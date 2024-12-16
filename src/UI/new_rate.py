from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
import src.database.utils.movie as MovieUtils
import src.database.utils.user_movie as UserMovieUtils
from tkinter import ttk
from src.utils.logging import get_logger
from src.classes.movie import Movie, EmptyMovie
from src.classes.user_movie import UserMovie
from datetime import datetime

if TYPE_CHECKING:
    from src.UI.app import App

logger = get_logger(__name__)


class NewRate(tk.Toplevel):

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
        UserMovieUtils.insert(UserMovie(
            user_id=self.parent.user.id,
            movie_id=self._all_movies[self.movie_combo.current()].id,
            rating=self._rate.get(),
            sold=True,
            sale_date=int(datetime.now().timestamp())
        ))
        self.close()

    def close(self) -> None:
        self.destroy()
        self.on_destroy()

    def __get_movie(self, movie_id) -> Movie | EmptyMovie:
        if movie_id:
            return MovieUtils.get(movie_id)
        return EmptyMovie()

    def __movie_update(self, e=None) -> None:
        self.button.config(state='normal')
