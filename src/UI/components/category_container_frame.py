from __future__ import annotations
from typing import TYPE_CHECKING
from tkinter import ttk
from src.UI.components.category_frame import CategoryFrame

if TYPE_CHECKING:
    from src.UI.app import App
    from src.database.utils.user_movie import UserMovie


class CategoryContainerFrame(ttk.Frame):
    """
    A class representing the category container frame for the Movie Recommendation System.

    Attributes:
    -----------
    parent : App
        The parent application instance.
    kwargs : dict
        Additional keyword arguments.
    display_movies_by_genre : list[list[UserMovie]]
        A list of lists containing UserMovie instances categorized by genre.
    categories : list[CategoryFrame]
        A list of CategoryFrame instances representing different movie categories.

    Methods:
    --------
    __init__(parent, **kwargs):
        Initializes the category container frame with the given parent and additional keyword arguments.
    create_widgets():
        Creates and arranges the category frames based on the movies categorized by genre.
    disable():
        Disables all category frames within the container.
    """

    def __init__(self, parent: App, **kwargs):
        super().__init__(
            parent
        )
        self.grid(
            row=3,
            column=0,
            columnspan=3
        )
        self.parent = parent
        self.kwargs = kwargs
        self.display_movies_by_genre: list[list[UserMovie]]
        self.categories: list[CategoryFrame] = []

    def create_widgets(self):
        """Create and arrange the category frames based on the movies categorized by genre."""

        self.categories = [
            CategoryFrame(
                self,
                self.parent,
                i[0].movie.genre,
                [
                    user_movie
                    for user_movie in i
                ]
            )
            for i in self.display_movies_by_genre
        ]

    def disable(self) -> None:
        """Disable all category frames within the container."""

        for category in self.categories:
            category.disable()
