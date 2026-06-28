# models/user.py
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password  # store hashed in real app
        self.role = "user"

    def check_password(self, password):
        return self.password == password

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "role": self.role,
        }

    @classmethod
    def from_dict(cls, data):
        role = data.get("role", "customer")
        if role == "admin":
            return Admin(data["user_id"], data["name"], data["email"], data["password"])
        return Customer(data["user_id"], data["name"], data["email"], data["password"])


class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.role = "customer"


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.role = "admin"

    def add_product(self, product_list, product):
        product_list.append(product)

    def remove_product(self, product_list, product_id):
        product_list[:] = [p for p in product_list if p.product_id != product_id]
