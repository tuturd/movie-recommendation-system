import ctypes
from pathlib import Path

from src.c_extension.utils.extension import LIB_FILE_EXTENSION
from src.classes.jaccard import ResultatSimilarite
from src.database.config import DB_PATH

# Load the shared library
libjaccard_path = Path(__file__).parent.parent.parent / f'c_extension/lib/Jaccard.{LIB_FILE_EXTENSION}'
libjaccard = ctypes.CDLL(str(libjaccard_path))

# Define the return types and argument types for the functions in the shared library
libjaccard.calculer_similarites_pour_utilisateur.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int)
libjaccard.calculer_similarites_pour_utilisateur.restype = ctypes.POINTER(ResultatSimilarite)


def similarites(user_id: int) -> list[ResultatSimilarite]:
    """
    Retrieves a list of users who have similar preferences to the target user based on Jaccard similarity.

    Parameters:
    -----------
    user_id : int
        The ID of the target user for whom the similarities are being calculated.

    Returns:
    --------
    list[ResultatSimilarite]
        A list of ResultatSimilarite objects representing users with similar preferences.

    Raises:
    -------
    DatabaseError
        If there is an error during the retrieval of the similarities from the database.
    """

    db_path_bytes = bytes(str(DB_PATH), 'utf-8')
    result_pointer = libjaccard.calculer_similarites_pour_utilisateur(db_path_bytes, user_id)
    results = []
    i = 0
    while result_pointer[i].user_id != -1:  # Assuming -1 is the sentinel value
        results.append(result_pointer[i])
        i += 1
    return results
