import ctypes


class Director(ctypes.Structure):
    """
    A class to represent a Director with attributes for first name, last name, and average rating.
    This class also includes methods to convert C-style string attributes to Python string attributes.

    Attributes:
    -----------
    firstname : str
        The first name of the director.
    lastname : str
        The last name of the director.
    avg_rating : float
        The average rating of the director.
    cfirstname : bytes
        The C-style string for the first name of the director.
    clastname : bytes
        The C-style string for the last name of the director.
    cavg_rating : ctypes.c_float
        The C-style float for the average rating of the director.

    Methods:
    --------
    convert() -> None
        Converts C-style string attributes to Python string attributes.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.firstname: str = ''
        self.lastname: str = ''
        self.avg_rating: float = 0.0

        self.cfirstname: bytes = b''
        self.clastname: bytes = b''
        self.cavg_rating: ctypes.c_float = 0.0

    def convert(self) -> None:
        """Convert C-style string attributes to Python string attributes"""

        self.firstname = self.cfirstname.decode('utf-8')
        self.lastname = self.clastname.decode('utf-8')
        self.avg_rating = float(self.cavg_rating)

    _fields_ = [
        ('cfirstname', ctypes.c_char * 50),
        ('clastname', ctypes.c_char * 50),
        ('cavg_rating', ctypes.c_float)
    ]
