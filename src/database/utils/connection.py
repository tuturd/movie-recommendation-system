import sqlite3

from src.database.config import DB_PATH


class UpgradeConnection(sqlite3.Connection):
    """
    A class that extends sqlite3.Connection to provide additional functionality.

    Parameters:
    -----------
    db_path : str
        The path to the SQLite database file.

    Methods:
    --------
    commit_and_close():
        Commits the current transaction and closes the connection.
    """

    def __init__(self, db_path):
        super().__init__(
            db_path
        )

    def commit_and_close(self):
        """Commits the current transaction and closes the database connection."""

        self.commit()
        self.close()


def open_connection() -> UpgradeConnection:
    """
    Opens a connection to the database.

    Returns:
    --------
    UpgradeConnection
        An instance of UpgradeConnection to interact with the database.
    """

    return UpgradeConnection(DB_PATH)
