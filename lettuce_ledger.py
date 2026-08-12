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

    def run_query(self, query):
        # executes raw query string directly - no parameterization
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()
        # connection never closed elsewhere in the app - resource leak
