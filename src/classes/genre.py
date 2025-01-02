import ctypes


class Genre(ctypes.Structure):
    """
    Represents a movie genre with a name and average rating.

    Attributes:
    -----------
    name : str
        The name of the genre.
    avg_rating : float
        The average rating of the genre.
    cname : bytes
        The name of the genre in bytes (C-style string).
    cavg_rating : ctypes.c_float
        The average rating of the genre as a C-style float.

    Methods:
    --------
    convert() -> None
        Converts the C-style attributes to Python-style attributes.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.name: str = ''
        self.avg_rating: float = 0.0

        self.cname: bytes = b''
        self.cavg_rating: ctypes.c_float = 0.0

    def convert(self) -> None:
        """Convert C-style attributes to Python-style attributes"""

        self.name = self.cname.decode('utf-8')
        self.avg_rating = float(self.cavg_rating)

    _fields_ = [
        ('cname', ctypes.c_char * 50),
        ('cavg_rating', ctypes.c_float)
    ]


class PyGenre:
    """
    Represents a movie genre with an ID and a name.

    Attributes:
    -----------
    id : int
        The ID of the genre.
    name : str
        The name of the genre.

    Methods:
    --------
    __init__(**kwargs)
        Initializes the PyGenre instance with provided values or defaults.
    """

    def __init__(self, **kwargs):
        self.id: int = kwargs.get('id', None)
        self.name: str = kwargs.get('name', None)
