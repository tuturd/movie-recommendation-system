from __future__ import annotations
from typing import TYPE_CHECKING
import ctypes

if TYPE_CHECKING:
    from src.classes.movie import Movie


class UserMovie:
    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id', None)
        self.user_id: int = kwargs.get('user_id', None)
        self.movie_id: int = kwargs.get('movie_id', None)
        self.rating: int = kwargs.get('rating', None)
        self.sold: bool = kwargs.get('sold', None)
        self.sale_date: int = kwargs.get('sale_date', None)
        self.movie: Movie = kwargs.get('movie', None)


class MinimizedUserMovie(ctypes.Structure):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.title: str = ''
        self.rating: int = 0
        self.sale_date: int = 0

        self.ctitle: bytes = b''
        self.crating: ctypes.c_int = 0
        self.csale_date: ctypes.c_int = 0

    def convert(self) -> None:
        self.title = self.ctitle.decode('utf-8')
        self.rating = int(self.crating)
        self.sale_date = int(self.csale_date)

    _fields_ = [
        ('ctitle', ctypes.c_char * 50),
        ('crating', ctypes.c_int),
        ('csale_date', ctypes.c_int)
    ]
