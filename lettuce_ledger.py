import sqlite3


class LettuceLedger:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self._setup()

    def _setup(self):
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS bunnies (name TEXT, carrots INTEGER)"
        )
        self.conn.commit()

    def run_query(self, query, params=()):
        # parameterized - caller passes placeholders instead of raw strings
        cursor = self.conn.execute(query, params)
        return cursor.fetchall()

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
