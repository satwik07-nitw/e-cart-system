# services/billing_service.py
from models.order import Order, OrderItem


class BillingService:
    def __init__(self, tax_rate=0.05, orders=None, next_order_id=1):
        self.tax_rate = tax_rate
        self.orders = orders if orders is not None else []
        self.next_order_id = next_order_id

    def generate_bill(self, cart, discount=0):
        if not cart.items:
            raise ValueError("Cart is empty. Cannot generate bill.")

        order_items = []
        for item in cart.items:
            item.product.reduce_stock(item.quantity)
            order_items.append(
                OrderItem(item.product.name, item.product.price, item.quantity)
            )

        order = Order(
            order_id=self.next_order_id,
            user=cart.user,
            items=order_items,
            discount=discount,
            tax_rate=self.tax_rate,
        )

        self.orders.append(order)
        self.next_order_id += 1
        return order

    def get_user_orders(self, user):
        return [o for o in self.orders if o.user.email == user.email]
