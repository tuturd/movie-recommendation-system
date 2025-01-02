from __future__ import annotations

from tkinter import ttk
from typing import TYPE_CHECKING

from src.UI.components.movie_frame import MovieFrame
from src.classes.user_movie import UserMovie
from src.classes.movie import Movie

if TYPE_CHECKING:
    from src.UI.app import App
    from src.UI.components.category_container_frame import CategoryContainerFrame


class CategoryFrame(ttk.Frame):
    """
    A class representing a category frame in the Movie Recommendation System UI.

    Attributes:
    -----------
    parent : CategoryContainerFrame
        The parent container frame.
    _app : App
        The main application instance.
    title : str
        The title of the category frame.
    user_movies : list[UserMovie]
        A list of user movies to be displayed in the category frame.
    movie_frames : list[MovieFrame]
        A list of movie frames created for each user movie.

    Methods:
    --------
    __init__(parent: CategoryContainerFrame, app: App, title: str, user_movies: list[UserMovie]):
        Initializes the category frame with the given parent, app, title, and user movies.
    create_widgets():
        Creates and arranges the widgets in the category frame.
    disable() -> None:
        Disables all movie frames within the category frame.
    """

    def __init__(self, parent: CategoryContainerFrame, app: App, title: str, user_movies: list[UserMovie] | list[Movie]):
        super().__init__(parent)
        self.pack(
            padx=5,
            pady=5
        )
        self.parent = parent
        self._app = app
        self.title = title
        self.user_movies = user_movies
        self.movie_frames: list[MovieFrame] = []

        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the category frame."""

        if isinstance(self.user_movies, UserMovie):

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
            self.movie_frames.append(
                MovieFrame(
                    self,
                    self._app,
                    user_movie,
                    column=i
                )
            )

    def disable(self) -> None:
        """Disables all movie frames within the category frame."""

        for user_movie in self.movie_frames:
            user_movie.disable()
