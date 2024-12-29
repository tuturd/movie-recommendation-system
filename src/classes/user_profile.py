import ctypes
from src.classes.director import Director
from src.classes.genre import Genre
from src.classes.user_movie import MinimizedUserMovie


class UserProfile(ctypes.Structure):
    """
    A class to represent a user profile with attributes and methods to convert
    between ctypes and Python native types.

    Attributes:
    -----------
    user_id : int
        The ID of the user.
    directors : list[Director]
        A list of Director objects associated with the user.
    genres : list[Genre]
        A list of Genre objects associated with the user.
    user_movies : list[MinimizedUserMovie]
        A list of MinimizedUserMovie objects associated with the user.
    movie_count : int
        The number of movies associated with the user.
    cuser_id : ctypes.c_int
        The ID of the user in ctypes format.
    cdirectors : ctypes.Array
        An array of Director objects in ctypes format.
    cgenres : ctypes.Array
        An array of Genre objects in ctypes format.
    cuser_movies : ctypes.Array
        An array of MinimizedUserMovie objects in ctypes format.
    cmovie_count : ctypes.c_int
        The number of movies associated with the user in ctypes format.

    Methods:
    --------
    convert() -> None
        Converts the ctypes attributes to their corresponding Python native types.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.user_id: int = 0
        self.directors: list[Director] = []
        self.genres: list[Genre] = []
        self.user_movies: list[MinimizedUserMovie] = []
        self.movie_count: int = 0

        self.cuser_id: ctypes.c_int = 0
        self.cdirectors = (Director * 3)()
        self.cgenres = (Genre * 3)()
        self.cuser_movies = (MinimizedUserMovie * 100)()
        self.cmovie_count: ctypes.c_int = 0

    def convert(self) -> None:
        """Convert ctypes attributes to Python native types"""

        self.user_id = int(self.cuser_id)
        self.directors = []
        self.genres = []
        self.user_movies = []
        self.movie_count = int(self.cmovie_count)

        for i in range(3):
            self.directors.append(self.cdirectors[i])
            self.directors[-1].convert()

            self.genres.append(self.cgenres[i])
            self.genres[-1].convert()

        for i in range(self.movie_count):
            self.user_movies.append(self.cuser_movies[i])
            self.user_movies[i].convert()

    _fields_ = [
        ('cuser_id', ctypes.c_int),
        ('cdirectors', Director * 3),
        ('cgenres', Genre * 3),
        ('cuser_movies', MinimizedUserMovie * 100),
        ('cmovie_count', ctypes.c_int)
    ]
