from __future__ import annotations
from typing import TYPE_CHECKING
from tkinter import ttk
from src.UI.components.movie_frame import MovieFrame

if TYPE_CHECKING:
    from src.UI.app import App
    from src.UI.components.category_container_frame import CategoryContainerFrame
    from src.classes.user_movie import UserMovie


class CategoryFrame(ttk.Frame):
    def __init__(self, parent: CategoryContainerFrame, app: App, title: str, user_movies: list[UserMovie]):
        super().__init__(parent)
        self.pack(
            padx=5,
            pady=5
        )
        self.parent = parent
        self._app = app
        self.title = title
        self.user_movies = user_movies

        self.create_widgets()

    def create_widgets(self):
        self.label_title = ttk.Label(
            self,
            text=self.title,
        )
        self.label_title.grid(
            row=0,
            column=0,
            padx=5,
            columnspan=len(self.user_movies),
            sticky='w'
        )

        self.separator = ttk.Separator(self, orient='horizontal')
        self.separator.grid(row=1, column=0, columnspan=len(self.user_movies), sticky='ew', pady=(0, 5))

        for i, user_movie in enumerate(self.user_movies):
            MovieFrame(
                self,
                self._app,
                user_movie,
                column=i
            )

        # for idx in range(len(self.user_movies)):
        #     self.grid_columnconfigure(idx, weight=1)
