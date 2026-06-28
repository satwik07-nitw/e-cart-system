# models/product.py
class Product:
    def __init__(self, product_id, name, price, stock, category=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def reduce_stock(self, qty):
        if qty > self.stock:
            raise ValueError(f"Not enough stock for {self.name}")
        self.stock -= qty

    def increase_stock(self, qty):
        self.stock += qty

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["product_id"], data["name"], data["price"],
            data["stock"], data.get("category")
        )

    def __str__(self):
        return f"{self.name} - Rs.{self.price} (Stock: {self.stock})"
