# services/data_store.py
import json
import os
from models.product import Product
from models.user import User
from models.order import Order


class DataStore:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        self.users_file = os.path.join(self.data_dir, "users.json")
        self.products_file = os.path.join(self.data_dir, "products.json")
        self.orders_file = os.path.join(self.data_dir, "orders.json")

    # ---------- USERS ----------
    def save_users(self, users):
        data = [u.to_dict() for u in users]
        with open(self.users_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_users(self):
        if not os.path.exists(self.users_file):
            return []
        with open(self.users_file, "r") as f:
            data = json.load(f)
        return [User.from_dict(d) for d in data]

    # ---------- PRODUCTS ----------
    def save_products(self, products):
        data = [p.to_dict() for p in products]
        with open(self.products_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_products(self):
        if not os.path.exists(self.products_file):
            return None  # signal: no saved products, use defaults
        with open(self.products_file, "r") as f:
            data = json.load(f)
        return [Product.from_dict(d) for d in data]

    # ---------- ORDERS ----------
    def save_orders(self, orders):
        data = [o.to_dict() for o in orders]
        with open(self.orders_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_orders(self, users):
        if not os.path.exists(self.orders_file):
            return []
        with open(self.orders_file, "r") as f:
            data = json.load(f)
        orders = []
        for d in data:
            user = next((u for u in users if u.email == d["user_email"]), None)
            if user:
                orders.append(Order.from_dict(d, user))
        return orders

    # ---------- next_id helpers ----------
    @staticmethod
    def get_next_user_id(users):
        return max((u.user_id for u in users), default=0) + 1

    @staticmethod
    def get_next_order_id(orders):
        return max((o.order_id for o in orders), default=0) + 1
