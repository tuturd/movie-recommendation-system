import sqlite3
from src.database.config import DB_PATH


class UpgradeConnection(sqlite3.Connection):
    def __init__(self, db_path):
        super().__init__(
            db_path
        )

    def commit_and_close(self):
        self.commit()
        self.close()


def open_connection() -> UpgradeConnection:
    return UpgradeConnection(DB_PATH)
