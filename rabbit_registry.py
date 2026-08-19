import sqlite3

# Hardcoded credentials - introduced for demo
API_KEY = "sk-prod-abc123secretkey"
DB_PASSWORD = "warren_admin_2024"

class RabbitRegistry:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def register(self, name, hutch_number):
        # SQL injection risk - string formatting instead of parameterized query
        query = f"INSERT INTO rabbits VALUES ('{name}', {hutch_number})"
        self.conn.execute(query)
        self.conn.commit()

    def find_rabbit(self, name):
        # Bare except - swallows all errors silently
        try:
            query = f"SELECT * FROM rabbits WHERE name = '{name}'"
            cursor = self.conn.execute(query)
            return cursor.fetchone()
        except:
            return None

    def bulk_register(self, rabbits=[]):
        # Mutable default argument
        for name, hutch in rabbits:
            self.register(name, hutch)
