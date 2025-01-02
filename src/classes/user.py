import ctypes


class User(ctypes.Structure):
    """
    A class to represent a User with attributes for both Python and C compatibility.

    Attributes:
    -----------
    id : int
        The user's ID.
    username : str
        The user's username.
    firstname : str
        The user's first name.
    lastname : str
        The user's last name.
    birth_date : int
        The user's birth date as an integer.
    cid : int
        The user's ID in C structure.
    cusername : bytes
        The user's username in C structure.
    cfirstname : bytes
        The user's first name in C structure.
    clastname : bytes
        The user's last name in C structure.
    cbirth_date : int
        The user's birth date in C structure.

    Methods:
    --------
    convert() -> None
        Converts C structure attributes to Python attributes.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.id: int = 0
        self.username: str = ''
        self.firstname: str = ''
        self.lastname: str = ''
        self.birth_date: int = 0

        self.cid: int = 0
        self.cusername: bytes = b''
        self.cfirstname: bytes = b''
        self.clastname: bytes = b''
        self.cbirth_date: int = 0

    def convert(self) -> None:
        """Convert C structure attributes to Python attributes"""

        self.id = int(self.cid)
        self.username = self.cusername.decode('utf-8')
        self.firstname = self.cfirstname.decode('utf-8')
        self.lastname = self.clastname.decode('utf-8')
        self.birth_date = int(self.cbirth_date)

    _fields_ = [
        ('cid', ctypes.c_int),
        ('cusername', ctypes.c_char * 50),
        ('cfirstname', ctypes.c_char * 50),
        ('clastname', ctypes.c_char * 50),
        ('cbirth_date', ctypes.c_int)
    ]
