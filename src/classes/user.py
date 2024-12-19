import ctypes


class User(ctypes.Structure):
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
