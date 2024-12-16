class Movie:
    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id', None)
        self.title: str = kwargs.get('title', None)
        self.release_date: int = kwargs.get('release_date', None)
        self.genre: str = kwargs.get('genre', None)
        self.director: str = kwargs.get('director', None)
        self.price: int = kwargs.get('price', None)


class EmptyMovie:
    def __init__(self, **kwargs):
        self.id: None = None
        self.title: None = None
        self.release_date: None = None
        self.genre: None = None
        self.director: None = None
        self.price: None = None


class MovieTitleAndDirector:
    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id', None)
        self.title: str = kwargs.get('title', None)
        self.director: str = kwargs.get('director', None)
