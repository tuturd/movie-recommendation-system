from __future__ import annotations
from typing import TYPE_CHECKING
from tkinter import ttk
from src.UI.components.category_frame import CategoryFrame

if TYPE_CHECKING:
    from src.UI.app import App
    from src.database.utils.user_movie import UserMovie


class CategoryContainerFrame(ttk.Frame):
    def __init__(self, parent: App, **kwargs):
        super().__init__(
            parent
        )
        self.grid(
            row=3,
            column=0,
            columnspan=2
        )
        self.parent = parent
        self.kwargs = kwargs
        self.display_movies_by_genre: list[list[UserMovie]]
        self.categories: list[CategoryFrame] = []

    def create_widgets(self):
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
