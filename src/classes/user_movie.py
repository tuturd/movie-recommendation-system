from __future__ import annotations
from typing import TYPE_CHECKING

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
