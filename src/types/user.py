class User:
    def __init__(self, **kwargs):
        self.username: str = kwargs.get('username', '')

    def __str__(self):
        return f'User(username={self.username})'


class UserComplete(User):
    def __init__(self, **kwargs):
        super().__init__()
        self.firstname: str = kwargs.get('firstname', '')
        self.lastname: str = kwargs.get('lastname', '')
        self.birthdate: float = kwargs.get('birthdate', 0.0)

    def __str__(self):
        return f'UserComplete(username={self.username}, firstname={self.firstname}, lastname={self.lastname}, birthdate={self.birthdate})'
