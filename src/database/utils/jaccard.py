from src.database.config import DB_PATH
import ctypes
from pathlib import Path


class ResultatSimilarite(ctypes.Structure):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.user_id: int = 0
        self.similarite: float = 0.0

    _fields_ = [('user_id', ctypes.c_int),
                ('similarite', ctypes.c_float)]


libjaccard_path = Path(__file__).parent.parent.parent / 'c_extension/lib/Jaccard.so'
libjaccard = ctypes.CDLL(str(libjaccard_path))

libjaccard.calculer_similarites_pour_utilisateur.argtypes = (ctypes.POINTER(ctypes.c_char), ctypes.c_int)
libjaccard.calculer_similarites_pour_utilisateur.restype = ctypes.POINTER(ResultatSimilarite)


def similarites(user_id: int) -> list[ResultatSimilarite]:
    db_path_bytes = bytes(str(DB_PATH), 'utf-8')
    result_pointer = libjaccard.calculer_similarites_pour_utilisateur(db_path_bytes, user_id)
    results = []
    i = 0
    while result_pointer[i].user_id != -1:  # Assuming -1 is the sentinel value
        results.append(result_pointer[i])
        i += 1
    return results
