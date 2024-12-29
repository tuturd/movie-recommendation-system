from __future__ import annotations
from typing import TYPE_CHECKING
import ctypes

if TYPE_CHECKING:
    from src.classes.movie import Movie


class UserMovie:
    """
    A class to represent a user's interaction with a movie.

    Attributes:
    -----------
    id : int
        The unique identifier for the user-movie interaction.
    user_id : int
        The unique identifier for the user.
    movie_id : int
        The unique identifier for the movie.
    rating : int
        The rating given by the user to the movie.
    sold : bool
        Indicates whether the movie has been sold.
    sale_date : int
        The date when the movie was sold.
    movie : Movie
        The movie object associated with this interaction.

    Methods:
    --------
    __init__(**kwargs):
        Initializes the UserMovie instance with the provided keyword arguments.
    """

    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id', None)
        self.user_id: int = kwargs.get('user_id', None)
        self.movie_id: int = kwargs.get('movie_id', None)
        self.rating: int = kwargs.get('rating', None)
        self.sold: bool = kwargs.get('sold', None)
        self.sale_date: int = kwargs.get('sale_date', None)
        self.movie: Movie = kwargs.get('movie', None)


class MinimizedUserMovie(ctypes.Structure):
    """
    A class to represent a minimized user movie with ctypes structure.

    Attributes:
    -----------
    title : str
        The title of the movie.
    rating : int
        The rating of the movie.
    sale_date : int
        The sale date of the movie.
    ctitle : bytes
        The title of the movie in bytes.
    crating : ctypes.c_int
        The rating of the movie as a ctypes integer.
    csale_date : ctypes.c_int
        The sale date of the movie as a ctypes integer.

    Methods:
    --------
    __init__(*args, **kw)
        Initializes the MinimizedUserMovie instance with default values.
    convert() -> None
        Converts the ctypes attributes to their corresponding Python types.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.title: str = ''
        self.rating: int = 0
        self.sale_date: int = 0

        self.ctitle: bytes = b''
        self.crating: ctypes.c_int = 0
        self.csale_date: ctypes.c_int = 0

    def convert(self) -> None:
        """Convert ctypes attributes to Python native types"""

        self.title = self.ctitle.decode('utf-8')
        self.rating = int(self.crating)
        self.sale_date = int(self.csale_date)

    _fields_ = [
        ('ctitle', ctypes.c_char * 50),
        ('crating', ctypes.c_int),
        ('csale_date', ctypes.c_int)
    ]
