import tkinter as tk
from tkinter import messagebox, ttk

import src.database.utils.director as DirectorUtils
import src.database.utils.movie as MovieUtils
import src.database.utils.genre as GenreUtils
from src.classes.movie import Movie
from src.utils.logging import get_logger

logger = get_logger(__name__)


class NewMovie(tk.Toplevel):
    """
    A class used to create a new movie entry window in the Movie Recommendation System.

    Attributes
    ----------
    on_destroy : function
        A callback function to be called when the window is closed.

    Methods
    -------
    __init__(self, parent, on_destroy)
        Initializes the NewMovie window with the given parent and on_destroy callback.

    create_widgets(self)
        Creates and arranges the widgets in the NewMovie window.

    on_submit(self, e=None)
        Handles the event when the user submits the new movie entry.

    close(self)
        Closes the NewMovie window and calls the on_destroy callback.
    """

    def __init__(self, parent, on_destroy):
        super().__init__(parent)
        self.on_destroy = on_destroy
        self.title('Nouveau Film - Movie Recommendation System')
        self.protocol('WM_DELETE_WINDOW', self.close)
        self._all_directors = DirectorUtils.get_all()
        self._all_genres = GenreUtils.get_all()
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the NewMovie window."""

        self.label_heading = ttk.Label(
            self,
            text="Ajout d'un film"
        )
        self.label_heading.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        self.label_title = ttk.Label(
            self,
            text='Titre :'
        )
        self.label_title.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.entry_title = ttk.Entry(
            self,
        )
        self.entry_title.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )
        self.entry_title.focus_set()

        self.label_director = ttk.Label(
            self,
            text='Réalisateur:'
        )
        self.label_director.grid(
            row=2,
            column=0,
            padx=10,
            pady=10
        )

        self.combo_director = ttk.Combobox(
            self,
            values=[
                f'{director.firstname} {director.lastname}'
                for director in self._all_directors
            ]
        )
        self.combo_director.grid(
            row=2,
            column=1,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.label_genre = ttk.Label(
            self,
            text='Genre:'
        )
        self.label_genre.grid(
            row=3,
            column=0,
            padx=10,
            pady=10
        )

        self.combo_genre = ttk.Combobox(
            self,
            values=[
                genre.name
                for genre in self._all_genres
            ]
        )
        self.combo_genre.grid(
            row=3,
            column=1,
            columnspan=3,
            padx=10,
            pady=10,
            sticky='nsew'
        )

        self.label_year = ttk.Label(
            self,
            text='Année de sortie :'
        )
        self.label_year.grid(
            row=4,
            column=0,
            padx=10,
            pady=10
        )

        self.entry_year = ttk.Entry(
            self,
        )
        self.entry_year.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

        self.label_price = ttk.Label(
            self,
            text='Prix de vente :'
        )
        self.label_price.grid(
            row=5,
            column=0,
            padx=10,
            pady=10
        )

        self.entry_price = ttk.Entry(
            self,
        )
        self.entry_price.grid(
            row=5,
            column=1,
            padx=10,
            pady=10
        )

        self.button = ttk.Button(
            self,
            text='Enregistrer',
            command=self.on_submit
        )
        self.button.grid(
            row=6,
            column=0,
            columnspan=3,
            pady=10,
            padx=10,
            sticky='ew'
        )

    def on_submit(self, e=None):
        """Handles the event when the user submits the new movie entry."""

        self.disable()

        movie_title = self.entry_title.get()
        movie_year = self.entry_year.get()
        movie_price = self.entry_price.get()
        movie_director_id = self.combo_director.current()
        movie_genre_id = self.combo_genre.current()

        if not movie_title or not movie_year or not movie_price or movie_director_id == -1 or movie_genre_id == -1:
            messagebox.showerror('Erreur', 'Veuillez remplir tous les champs.')
            self.enable()
            return

        new_movie = Movie(
            title=movie_title,
            release_date=movie_year,
            price=movie_price,
            director_id=self._all_directors[movie_director_id].id,
            genre_id=self._all_genres[movie_genre_id].id
        )

        MovieUtils.insert(new_movie)

        self.close()

    def disable(self):
        """Disable all the widgets in the NewMovie window."""

        self.entry_title['state'] = 'disable'
        self.combo_director['state'] = 'disable'
        self.entry_year['state'] = 'disable'
        self.entry_price['state'] = 'disable'
        self.button['state'] = 'disable'

    def enable(self):
        """Enable all the widgets in the NewMovie window."""

        self.entry_title['state'] = 'normal'
        self.combo_director['state'] = 'normal'
        self.entry_year['state'] = 'normal'
        self.entry_price['state'] = 'normal'
        self.button['state'] = 'normal'

    def close(self):
        """Close the NewMovie window and call the on_destroy callback."""

        self.destroy()
        self.on_destroy()
