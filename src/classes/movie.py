class Movie:
    """
    A class used to represent a Movie.

    Attributes:
    -----------
    id : int
        The unique identifier for the movie.
    title : str
        The title of the movie.
    release_date : int
        The release year of the movie.
    genre : str
        The genre of the movie.
    director : str
        The director of the movie.
    price : int
        The price of the movie.

    Methods:
    --------
    __init__(**kwargs):
        Initializes a new instance of the Movie class with the given attributes.
    """

    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id', None)
        self.title: str = kwargs.get('title', None)
        self.release_date: int = kwargs.get('release_date', None)
        self.genre: str = kwargs.get('genre', None)
        self.director: str = kwargs.get('director', None)
        self.price: int = kwargs.get('price', None)


class EmptyMovie:
    """
    A class representing an empty movie with no attributes set.

    Parameters:
    -----------
    **kwargs : dict
        Arbitrary keyword arguments.

    Attributes:
    -----------
    id : None
        The ID of the movie.
    title : None
        The title of the movie.
    release_date : None
        The release date of the movie.
    genre : None
        The genre of the movie.
    director : None
        The director of the movie.
    price : None
        The price of the movie.
    """

    def __init__(self, **kwargs):
        self.id: None = None
        self.title: None = None
        self.release_date: None = None
        self.genre: None = None
        self.director: None = None
        self.price: None = None


class MovieTitleAndDirector:
    """
    A class to represent a movie with its title and director.

    Attributes:
    -----------
    id : int
        The unique identifier for the movie.
    title : str
        The title of the movie.
    director : str
        The director of the movie.

    Methods:
    --------
    __init__(**kwargs):
        Initializes the MovieTitleAndDirector with optional id, title, and director.
    """

    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id', None)
        self.title: str = kwargs.get('title', None)
        self.director: str = kwargs.get('director', None)
