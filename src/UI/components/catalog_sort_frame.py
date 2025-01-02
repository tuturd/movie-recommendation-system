from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.UI.app import App
    from src.UI.catalog import Catalog


class CatalogSortFrame(ttk.LabelFrame):
    """
    A class representing the sort frame for the Movie Recommendation System.

    Attributes:
    -----------
    app : App
        The main application instance.
    parent : Catalog
        The parent catalog instance.
    combo_sort_method : ttk.Combobox
        The combobox widget for selecting the sorting method.

    Methods:
    --------
    __init__(parent: Catalog, app: App):
        Initializes the sort frame with the given parent and app instance.
    create_widgets():
        Creates and arranges the widgets in the sort frame.
    refresh_sort(event=None):
        Handles the sorting of movies based on the selected method.
    __on_click(e):
        Event handler for combobox selection.
    """

    def __init__(self, parent: Catalog, app: App):
        super().__init__(
            parent,
            borderwidth=2,
            relief=tk.SOLID,
            text='Tris',
        )
        self.grid(
            row=0,
            column=2,
            padx=5
        )
        self.app = app
        self.parent = parent

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the sort frame."""

        self.combo_sort_method = ttk.Combobox(
            self,
            values=[
                'Enregistrement croissant',
                'Enregistrement décroissant',
                'Date de sortie croissante',
                'Date de sortie décroissante',
            ]
        )
        self.combo_sort_method.grid(
            row=0,
            column=0,
            padx=10,
        )
        self.combo_sort_method.bind('<<ComboboxSelected>>', self.__on_click)

    def refresh_sort(self, event=None) -> None:
        """Handle the sorting of movies based on the selected method."""

        movies_to_display = self.parent.movies_to_display
        sorting_method = self.combo_sort_method.current()

        match sorting_method:
            case 0:
                movies_to_display.sort(key=lambda movie: movie.id)
            case 1:
                movies_to_display.sort(key=lambda movie: movie.id, reverse=True)
            case 2:
                movies_to_display.sort(key=lambda movie: movie.release_date)
            case 3:
                movies_to_display.sort(key=lambda movie: movie.release_date, reverse=True)

        self.parent.movies_to_display = movies_to_display

    def __on_click(self, e) -> None:
        self.refresh_sort()
        self.parent.refresh_movies()
