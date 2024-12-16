from src.database.config import DB_PATH
import ctypes
from pathlib import Path


class User(ctypes.Structure):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.id: int = 0
        self.username: str = ''
        self.firstname: str = ''
        self.lastname: str = ''
        self.birth_date: int = 0

    _fields_ = [('id', ctypes.c_int),
                ('username', ctypes.c_char * 50),
                ('firstname', ctypes.c_char * 50),
                ('lastname', ctypes.c_char * 50),
                ('birth_date', ctypes.c_int)]


libuser_path = Path(__file__).parent.parent.parent / 'c_extension/lib/user.so'
libuser = ctypes.CDLL(str(libuser_path))

libuser._get.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char))
libuser._get.restype = User


def get(user_id: int) -> User:
    db_path_bytes = bytes(str(DB_PATH), 'utf-8')
    user_id_bytes = bytes(user_id, 'utf-8')
    user = libuser._get(db_path_bytes, user_id_bytes)
    return user
