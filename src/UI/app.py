import tkinter as tk
from tkinter import ttk

from src.classes.user_movie import UserMovie
from src.database.utils import jaccard as JaccardUtils
from src.database.utils import movie as MovieUtils
from src.database.utils import user as UserUtils
from src.UI.auth import Auth
from src.UI.components.actions_frame import ActionsFrame
from src.UI.components.category_container_frame import CategoryContainerFrame
from src.UI.components.criteria_frame import CriteriaFrame
from src.UI.components.filter_frame import FilterFrame
from src.UI.profile import Profile
from src.utils.logging import get_logger

logger = get_logger(__name__)


class App(tk.Tk):
    """
    A class representing the main application window for the Movie Recommendation System.

    Attributes:
    -----------
    auth_number : int
        A counter for the number of authentication attempts.
    auth : Auth
        The authentication process instance.
    filter_frame_open : bool
        A flag indicating whether the filter frame is open.
    label_title : ttk.Label
        The label displaying the welcome message.
    button_logout : ttk.Button
        The button for logging out.
    button_profile : ttk.Button
        The button for accessing the user profile.
    frame_actions : ActionsFrame
        The frame containing action buttons.
    frame_criteria : CriteriaFrame
        The frame containing criteria selection widgets.
    frame_filter : FilterFrame
        The frame for filtering movie recommendations.
    frame_category : CategoryContainerFrame
        The frame displaying movie categories.
    user : UserUtils.User
        The authenticated user instance.
    _jaccard_result : list[JaccardUtils.ResultatSimilarite]
        The list of Jaccard similarity results.

    Methods:
    --------
    __init__(**kwargs):
        Initializes the main application window with optional keyword arguments.
    create_widgets():
        Creates and arranges the widgets in the main application window.
    disable():
        Disables interactive widgets in the main application window.
    restart_auth_process() -> None:
        Restarts the authentication process.
    auth_process() -> Auth:
        Initiates the authentication process.
    on_auth_destroy():
        Callback function to handle actions after authentication is destroyed.
    profile_process() -> Profile:
        Initiates the profile process.
    on_profile_destroy():
        Callback function to handle actions after the profile process is destroyed.
    open_filter_frame():
        Opens the filter frame.
    close_filter_frame():
        Closes the filter frame.
    refresh_movies():
        Refreshes the movie recommendations based on Jaccard similarity results.
    """

    def __init__(self, **kwargs):
        super().__init__()
        self.title('Movie Recommendation System')
        self.maxsize(1920, 1080)
        self.auth_number = 0
        self.auth: Auth = self.auth_process()
        self.filter_frame_open: bool = kwargs.get('filter_frame_open', False)
        self.label_title: ttk.Label = None
        self.button_logout: ttk.Button = None
        self.button_profile: ttk.Button = None
        self.frame_actions: ActionsFrame = None
        self.frame_criteria: CriteriaFrame = None
        self.frame_filter: FilterFrame = None
        self.frame_category: CategoryContainerFrame = None
        self.user: UserUtils.User = None
        self._jaccard_result: list[JaccardUtils.ResultatSimilarite] = []

    def create_widgets(self):
        """Create and arrange the widgets in the main application window."""

        self.label_title = ttk.Label(
            self,
            text=f'Bienvenue sur le système de recommendation, {self.auth.username} !',
            anchor=tk.CENTER
        )
        self.label_title.grid(
            row=0,
            column=0
        )

        self.button_logout = ttk.Button(
            self,
            text='Deconnexion',
            command=self.restart_auth_process
        )
        self.button_logout.grid(
            row=0,
            column=2,
            pady=5,
            padx=5,
            sticky='e'
        )

        self.button_profile = ttk.Button(
            self,
            text='Mon Profil',
            command=self.profile_process
        )
        self.button_profile.grid(
            row=0,
            column=1,
            pady=5,
            padx=5,
            sticky='e'
        )

        self.frame_container = ttk.Frame(self)
        self.frame_container.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.frame_actions = ActionsFrame(self.frame_container, self)

        self.frame_criteria = CriteriaFrame(self.frame_container, self)

        self.separator = ttk.Separator(
            self,
            orient='horizontal'
        )
        self.separator.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky='ew',
            pady=(10, 5),
            padx=20
        )

        self.frame_category = CategoryContainerFrame(self)

    def disable(self):
        """Disables interactive widgets in the main application window."""

        self.button_profile['state'] = 'disable'
        self.button_logout['state'] = 'disable'
        self.frame_actions.disable()
        self.frame_criteria.disable()
        self.frame_category.disable()

    def restart_auth_process(self) -> None:
        """Restarts the authentication process."""

        self.auth = self.auth_process()

    def auth_process(self) -> Auth:
        """Initiates the authentication process."""

        self.withdraw()
        try:
            self.frame_category.destroy()
        except AttributeError:
            pass
        self.auth_number += 1
        return Auth(self.on_auth_destroy, self.auth_number)

    def on_auth_destroy(self):
        """Callback function to handle actions after authentication is destroyed."""

        self.user = UserUtils.get(self.auth.username)
        self.create_widgets()
        self.refresh_movies()
        self.deiconify()

    def profile_process(self) -> Profile:
        """Initiates the profile process"""

        self.disable()
        return Profile(self, self.on_profile_destroy)

    def on_profile_destroy(self):
        """Callback function to handle actions after the profile process is destroyed."""

        self.create_widgets()
        self.refresh_movies()

    def open_filter_frame(self):
        """Opens the filter frame."""

        self.disable()
        self.frame_filter = FilterFrame(self.frame_container, self)

    def close_filter_frame(self):
        """Closes the filter frame."""

        self.frame_filter.destroy()
        self.frame_filter = None

    def refresh_movies(self):
        """Refreshes the movie recommendations based on Jaccard similarity results."""

        self._jaccard_result = JaccardUtils.similarites(self.user.id)
        logger.debug(f'jaccard result: {[r.similarite for r in self._jaccard_result]}')

        nearest_users = sorted(
            self._jaccard_result,
            key=lambda x: x.similarite,
            reverse=True
        )[:5]

        logger.debug(f'nearest users: {[u.user_id for u in nearest_users]}')

        display_movies: list[UserMovie] = MovieUtils.get_movies_to_recommend(nearest_users, self.user)

        logger.debug(f'display movies: {[m.movie.id for m in display_movies]}')

        unique_movies = {}
        for user_movie in display_movies:
            if user_movie.movie.id in unique_movies:
                existing_movie: UserMovie = unique_movies[user_movie.movie.id]
                existing_movie.rating = (existing_movie.rating + user_movie.rating) / 2
            else:
                unique_movies[user_movie.movie.id] = user_movie
        display_movies = list(unique_movies.values())

        # display_movies.sort(key=lambda x: x.movie.genre)
        genre_dict = {}
        for user_movie in display_movies:
            genre = user_movie.movie.genre
            if genre not in genre_dict:
                genre_dict[genre] = []
            genre_dict[genre].append(user_movie)

        display_movies_by_genre: list[list[UserMovie]] = [
            [
                movie
                for movie in genre_dict[genre]
            ]
            for genre in sorted(genre_dict.keys())
        ]
        self.frame_category.display_movies_by_genre = display_movies_by_genre
        self.frame_category.create_widgets()
