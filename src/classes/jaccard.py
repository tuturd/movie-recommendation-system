import ctypes


class ResultatSimilarite(ctypes.Structure):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.user_id: int = 0
        self.similarite: float = 0.0

    _fields_ = [
        ('user_id', ctypes.c_int),
        ('similarite', ctypes.c_float)
    ]
