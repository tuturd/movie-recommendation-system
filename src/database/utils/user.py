from src.c_extension.utils.extension import LIB_FILE_EXTENSION
from src.c_extension.utils.builder_from_app import build
from src.database.config import DB_PATH
from src.classes.user import User
from src.classes.user_profile import UserProfile
import ctypes
from pathlib import Path

# Load the shared library
libuser_path = Path(__file__).parent.parent.parent / f'c_extension/lib/user.{LIB_FILE_EXTENSION}'
try:
    libuser = ctypes.CDLL(str(libuser_path))
except OSError as e:
    print(f"Error loading the shared library: {e}\nLaunching the builder script...")
    build()
    libuser = ctypes.CDLL(str(libuser_path))
    print('Build completed. Launching the app.')

# Define the return types and argument types for the functions in the shared library
libuser.get.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char))
libuser.get.restype = User


def get(user_id: int) -> User:
    """
    Retrieve a user from the database using their user ID.

    Parameters:
    -----------
    user_id : int
        The ID of the user to retrieve.

    Returns:
    --------
    User
        The user object corresponding to the given user ID.
    """

    db_path_bytes = bytes(str(DB_PATH), 'utf-8')
    user_id_bytes = bytes(user_id, 'utf-8')
    user = libuser.get(db_path_bytes, user_id_bytes)
    user.convert()

    return user


# Define the return types and argument types for the functions in the shared library
libuser.get_user_profile.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int)
libuser.get_user_profile.restype = UserProfile


def get_user_profile(user_id: int) -> UserProfile:
    """
    Retrieve the user profile for a given user ID.

    Parameters:
    -----------
    user_id : int
        The ID of the user whose profile is to be retrieved.

    Returns:
    --------
    UserProfile
        The profile of the user with the specified ID.
    """

    db_path_bytes = bytes(str(DB_PATH), 'utf-8')
    user_profile = libuser.get_user_profile(db_path_bytes, user_id)
    user_profile.convert()

    return user_profile
