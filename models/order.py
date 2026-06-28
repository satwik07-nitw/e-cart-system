# models/order.py
from datetime import datetime


class OrderItem:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def get_subtotal(self):
        return self.price * self.quantity

    def to_dict(self):
        return {
            "product_name": self.product_name,
            "price": self.price,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["product_name"], data["price"], data["quantity"])


class Order:
    def __init__(self, order_id, user, items, discount=0, tax_rate=0.0, timestamp=None):
        self.order_id = order_id
        self.user = user
        self.items = items  # list of OrderItem (snapshot)
        self.discount = discount
        self.tax_rate = tax_rate
        self.timestamp = timestamp or datetime.now()

    def get_subtotal(self):
        return sum(item.get_subtotal() for item in self.items)

    def get_tax(self):
        return self.get_subtotal() * self.tax_rate

    def get_total(self):
        subtotal = self.get_subtotal()
        tax = self.get_tax()
        return subtotal - self.discount + tax

    def print_bill(self):
        print("\n========== BILL ==========")
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.user.name}")
        print(f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print("---------------------------")
        for item in self.items:
            print(f"{item.product_name} x{item.quantity} = Rs.{item.get_subtotal()}")
        print("---------------------------")
        print(f"Subtotal: Rs.{self.get_subtotal()}")
        print(f"Discount: Rs.{self.discount}")
        print(f"Tax: Rs.{self.get_tax():.2f}")
        print(f"TOTAL: Rs.{self.get_total():.2f}")
        print("===========================")

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "user_email": self.user.email,
            "items": [item.to_dict() for item in self.items],
            "discount": self.discount,
            "tax_rate": self.tax_rate,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data, user):
        return cls(
            order_id=data["order_id"],
            user=user,
            items=[OrderItem.from_dict(i) for i in data["items"]],
            discount=data["discount"],
            tax_rate=data["tax_rate"],
            timestamp=datetime.fromisoformat(data["timestamp"]),
        )
