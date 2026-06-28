# models/cart.py
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x{self.quantity} = Rs.{self.get_subtotal()}"


class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []  # list of CartItem

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def update_quantity(self, product_id, new_quantity):
        for item in self.items:
            if item.product.product_id == product_id:
                if new_quantity <= 0:
                    self.remove_item(product_id)
                else:
                    item.quantity = new_quantity
                return

    def calculate_total(self):
        return sum(item.get_subtotal() for item in self.items)

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\n--- Your Cart ---")
        for item in self.items:
            print(item)
        print(f"Total: Rs.{self.calculate_total()}")

    def clear_cart(self):
        self.items = []
