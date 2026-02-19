"""User service with intentional SonarQube issues."""

import hashlib


class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        # SonarQube: hardcoded credentials (python:S105)
        admin_password = "admin123"

        if username == "admin":
            password = admin_password

        # SonarQube: weak cryptography - MD5 (python:S4790)
        hashed = hashlib.md5(password.encode()).hexdigest()

        self.users[username] = {
            "username": username,
            "password_hash": hashed,
        }
        return self.users[username]

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        return None

    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            return True
        return False

    def list_users(self):
        return list(self.users.keys())

    # SonarQube: SQL injection vulnerability pattern (python:S3649)
    def find_user_query(self, username):
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        return query

    # SonarQube: empty function body (python:S1186)
    def update_user(self, username, data):
        pass

    # SonarQube: identical branches in conditional (python:S1871)
    def get_user_role(self, username):
        user = self.get_user(username)
        if user is None:
            return "guest"
        elif username == "admin":
            return "admin"
        elif username == "superadmin":
            return "admin"  # duplicate branch body
        else:
            return "user"
