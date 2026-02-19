from test_python_project.user_service import UserService


class TestUserService:
    def setup_method(self):
        self.service = UserService()

    def test_create_user(self):
        user = self.service.create_user("alice", "password123")
        assert user["username"] == "alice"
        assert "password_hash" in user

    def test_create_admin_user(self):
        user = self.service.create_user("admin", "any_password")
        assert user["username"] == "admin"

    def test_get_user_exists(self):
        self.service.create_user("bob", "pass")
        user = self.service.get_user("bob")
        assert user is not None
        assert user["username"] == "bob"

    def test_get_user_not_exists(self):
        assert self.service.get_user("nobody") is None

    def test_delete_user_exists(self):
        self.service.create_user("charlie", "pass")
        assert self.service.delete_user("charlie") is True
        assert self.service.get_user("charlie") is None

    def test_delete_user_not_exists(self):
        assert self.service.delete_user("nobody") is False

    def test_list_users(self):
        self.service.create_user("alice", "pass1")
        self.service.create_user("bob", "pass2")
        users = self.service.list_users()
        assert "alice" in users
        assert "bob" in users
        assert len(users) == 2

    def test_find_user_query(self):
        query = self.service.find_user_query("alice")
        assert "alice" in query
        assert "SELECT" in query

    def test_update_user_does_nothing(self):
        self.service.create_user("alice", "pass")
        self.service.update_user("alice", {"email": "a@b.com"})
        # update is a no-op, user should still exist unchanged
        assert self.service.get_user("alice") is not None

    def test_get_user_role_admin(self):
        self.service.create_user("admin", "pass")
        assert self.service.get_user_role("admin") == "admin"

    def test_get_user_role_superadmin(self):
        self.service.create_user("superadmin", "pass")
        assert self.service.get_user_role("superadmin") == "admin"

    def test_get_user_role_regular(self):
        self.service.create_user("alice", "pass")
        assert self.service.get_user_role("alice") == "user"

    def test_get_user_role_guest(self):
        assert self.service.get_user_role("unknown") == "guest"
