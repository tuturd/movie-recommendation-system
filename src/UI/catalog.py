from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

from src.classes.movie import Movie
from src.UI.components.category_container_frame import CategoryContainerFrame
from src.UI.components.catalog_filter_frame import CatalogFilterFrame
from src.UI.components.catalog_sort_frame import CatalogSortFrame
from src.utils.logging import get_logger

if TYPE_CHECKING:
    from src.UI.app import App

logger = get_logger(__name__)


class Catalog(tk.Toplevel):
    """
    A class representing the catalog window for the Movie Recommendation System.

    Attributes:
    -----------
    parent : App
        The parent application instance.
    on_destroy : function
        The callback function to be called when the catalog window is closed.
    movies_to_display : list[Movie]
        The list of movies to be displayed in the catalog.
    label_title : ttk.Label
        The label displaying the catalog title.
    frame_filter : CatalogFilterFrame
        The frame for filtering movies in the catalog.
    frame_sort : CatalogSortFrame
        The frame for sorting movies in the catalog.
    frame_category : CategoryContainerFrame
        The frame displaying movie categories.

    Methods:
    --------
    __init__(parent: App, on_destroy: function):
        Initializes the catalog window with the parent application and on_destroy callback.
    create_widgets():
        Creates and arranges the widgets in the catalog window.
    refresh_movies():
        Refreshes the movies displayed in the catalog based on the current filters and sorting.
    close():
        Closes the catalog window and calls the on_destroy callback.
    """

    def __init__(self, parent: App, on_destroy: function):
        super().__init__()
        self.title('Movie Recommendation System - Catalogue')
        self.maxsize(1920, 1080)
        self.protocol('WM_DELETE_WINDOW', self.close)

        self.parent = parent
        self.on_destroy = on_destroy
        self.movies_to_display: list[Movie] = []

        self.label_title: ttk.Label = None
        self.frame_filter: CatalogFilterFrame = None
        self.frame_category: CategoryContainerFrame = None

        self.create_widgets()

    def create_widgets(self):
        """"""

        self.label_title = ttk.Label(
            self,
            text='Catalogue',
            anchor=tk.CENTER
        )
        self.label_title.grid(
            row=0,
            column=0
        )

        self.frame_filter = CatalogFilterFrame(self, self.parent)
        self.frame_filter.grid(
            row=1,
            column=0
        )

        self.frame_sort = CatalogSortFrame(self, self.parent)
        self.frame_sort.grid(
            row=1,
            column=1
        )

        self.refresh_movies()

    def refresh_movies(self):
        """"""

        self.frame_sort.refresh_sort()

        display_movies_by_category: list[list[Movie]] = [self.movies_to_display]

        if self.frame_category:
            self.frame_category.destroy()
        if len(display_movies_by_category[0]) > 0:
            self.frame_category = CategoryContainerFrame(self)
            self.frame_category.display_movies_by_category = display_movies_by_category
            self.frame_category.create_widgets()

    def close(self):
        """"""

        self.destroy()
        self.on_destroy()
