import ctypes


class Genre(ctypes.Structure):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.name: str = ''
        self.avg_rating: float = 0.0

        self.cname: bytes = b''
        self.cavg_rating: ctypes.c_float = 0.0

    def convert(self) -> None:
        self.name = self.cname.decode('utf-8')
        self.avg_rating = float(self.cavg_rating)

    _fields_ = [
        ('cname', ctypes.c_char * 50),
        ('cavg_rating', ctypes.c_float)
    ]
