import ctypes


class ResultatSimilarite(ctypes.Structure):
    """
    A class to represent the similarity result between users.
    Attributes:
    -----------
    user_id : int
        The ID of the user.
    similarite : float
        The similarity score between users.
    Methods:
    --------
    __init__(*args, **kw)
        Initializes the ResultatSimilarite instance with default values.
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.user_id: int = 0
        self.similarite: float = 0.0

    _fields_ = [
        ('user_id', ctypes.c_int),
        ('similarite', ctypes.c_float)
    ]
