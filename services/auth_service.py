# services/auth_service.py
from models.user import Customer, Admin


class AuthService:
    def __init__(self, users=None, next_id=1):
        self.users = users if users is not None else []
        self.next_id = next_id

    def register(self, name, email, password, role="customer"):
        if any(u.email == email for u in self.users):
            raise ValueError("Email already registered")

        if role == "admin":
            user = Admin(self.next_id, name, email, password)
        else:
            user = Customer(self.next_id, name, email, password)

        self.users.append(user)
        self.next_id += 1
        return user

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.check_password(password):
                return user
        return None
