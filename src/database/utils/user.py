from src.database.config import DB_PATH
from src.classes.user import User
from src.classes.user_profile import UserProfile
import ctypes
from pathlib import Path


libuser_path = Path(__file__).parent.parent.parent / 'c_extension/lib/user.so'
libuser = ctypes.CDLL(str(libuser_path))

libuser.get.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char))
libuser.get.restype = User


def get(user_id: int) -> User:
    db_path_bytes = bytes(str(DB_PATH), 'utf-8')
    user_id_bytes = bytes(user_id, 'utf-8')
    user = libuser.get(db_path_bytes, user_id_bytes)
    user.convert()
    return user


libuser.get_user_profile.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int)
libuser.get_user_profile.restype = UserProfile


def get_user_profile(user_id: int) -> UserProfile:
    db_path_bytes = bytes(str(DB_PATH), 'utf-8')
    user_profile = libuser.get_user_profile(db_path_bytes, user_id)
    user_profile.convert()
    return user_profile
