import ctypes


class Director(ctypes.Structure):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.firstname: str = ''
        self.lastname: str = ''
        self.avg_rating: float = 0.0

        self.cfirstname: bytes = b''
        self.clastname: bytes = b''
        self.cavg_rating: ctypes.c_float = 0.0

    def convert(self) -> None:
        self.firstname = self.cfirstname.decode('utf-8')
        self.lastname = self.clastname.decode('utf-8')
        self.avg_rating = float(self.cavg_rating)

    _fields_ = [
        ('cfirstname', ctypes.c_char * 50),
        ('clastname', ctypes.c_char * 50),
        ('cavg_rating', ctypes.c_float)
    ]
