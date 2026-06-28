# services/cart_service.py
class CartService:
    def __init__(self, cart, products):
        self.cart = cart
        self.products = products  # list of Product objects

    def _find_product(self, product_id):
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None

    def add_to_cart(self, product_id, quantity):
        product = self._find_product(product_id)
        if not product:
            print("Product not found.")
            return
        if quantity > product.stock:
            print(f"Only {product.stock} units of {product.name} available.")
            return
        self.cart.add_item(product, quantity)
        print(f"Added {quantity} x {product.name} to cart.")

    def remove_from_cart(self, product_id):
        product = self._find_product(product_id)
        if not product:
            print("Product not found.")
            return
        self.cart.remove_item(product_id)
        print(f"Removed {product.name} from cart.")

    def update_quantity(self, product_id, new_quantity):
        product = self._find_product(product_id)
        if not product:
            print("Product not found.")
            return
        if new_quantity > product.stock:
            print(f"Only {product.stock} units of {product.name} available.")
            return
        self.cart.update_quantity(product_id, new_quantity)
        print(f"Updated {product.name} quantity to {new_quantity}.")
