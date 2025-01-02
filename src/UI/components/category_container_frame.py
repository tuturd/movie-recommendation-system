from __future__ import annotations

from tkinter import ttk
from typing import TYPE_CHECKING

from src.UI.components.category_frame import CategoryFrame
from src.classes.user_movie import UserMovie
from src.classes.movie import Movie

if TYPE_CHECKING:
    from src.UI.app import App


class CategoryContainerFrame(ttk.Frame):
    """
    A class representing the category container frame for the Movie Recommendation System.

    Attributes:
    -----------
    parent : App
        The parent application instance.
    kwargs : dict
        Additional keyword arguments.
    display_movies_by_category : list[list[UserMovie]]
        A list of lists containing UserMovie instances categorized.
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
        self.display_movies_by_category: list[list[UserMovie]] | list[list[Movie]] = []
        self.categories: list[CategoryFrame] = []

    def create_widgets(self):
        """Create and arrange the category frames based on the movies categorized by genre."""

        if isinstance(self.display_movies_by_category[0][0], UserMovie):
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
                for i in self.display_movies_by_category
            ]

        elif isinstance(self.display_movies_by_category[0][0], Movie):
            self.categories = [
                CategoryFrame(
                    self,
                    self.parent,
                    '',
                    [
                        movie
                        for movie in i[j: j + 4]
                    ]
                )
                for i in self.display_movies_by_category
                for j in range(0, len(i), 4)
            ]

    def disable(self) -> None:
        """Disable all category frames within the container."""

        for category in self.categories:
            category.disable()
