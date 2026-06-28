# 🛒 E-Cart System

A command-line based E-Cart (Shopping Cart) system built in Python using Object-Oriented Programming (OOP) principles.

---

## 📌 Features

- **User Authentication** — Register and login with email & password
- **Product Catalog** — Browse available products with prices and stock
- **Cart Management** — Add, remove, and update item quantities in cart
- **Bill Generation** — Itemized bill with subtotal, tax, and total
- **Order History** — View all past orders after logging in
- **Stock Management** — Stock reduces automatically after checkout
- **Data Persistence** — All users, products, and orders are saved to JSON files and persist between sessions
- **Logout Protection** — Warns user if they try to logout with items still in cart

---

## 🗂️ Project Structure

```
E-cart system/
│
├── main.py                  # Entry point — CLI menu and app flow
│
├── models/                  # Data models (OOP classes)
│   ├── __init__.py
│   ├── user.py              # User, Customer, Admin classes
│   ├── product.py           # Product class
│   ├── cart.py              # Cart and CartItem classes
│   └── order.py             # Order and OrderItem classes
│
├── services/                # Business logic
│   ├── __init__.py
│   ├── auth_service.py      # Register and login logic
│   ├── cart_service.py      # Add/remove/update cart logic
│   ├── billing_service.py   # Bill generation and order tracking
│   └── data_store.py        # JSON save/load for persistence
│
└── data/                    # Auto-created on first run
    ├── users.json           # Saved user accounts
    ├── products.json        # Saved product stock levels
    └── orders.json          # Saved order history
```

---

## 🧠 OOP Concepts Used

| Concept | Where Used |
|---|---|
| **Inheritance** | `Customer` and `Admin` inherit from `User` |
| **Encapsulation** | Product stock and user data accessed via methods |
| **Abstraction** | Services separated from models |
| **Composition** | `Cart` contains `CartItem`, `Order` contains `OrderItem` |

---

## ▶️ How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
# Clone the repository
git clone https://github.com/satwik07-nitw/e-cart-system.git

# Navigate into the project folder
cd e-cart-system

# Run the program
python main.py
```

---

## 🖥️ Usage Flow

```
1. Register a new account
2. Login with your credentials
3. View available products
4. Add products to cart
5. View / update / remove cart items
6. Checkout → generates itemized bill
7. View order history anytime
8. Logout
```

---

## 📸 Sample Bill Output

```
========== BILL ==========
Order ID: 1
Customer: shravan
Date: 2026-06-13 12:45:00
---------------------------
Headphones x2 = Rs.3000
Keyboard x1 = Rs.800
---------------------------
Subtotal: Rs.3800
Discount: Rs.0
Tax: Rs.190.00
TOTAL: Rs.3990.00
===========================
```

---

## 👤 Author

**Satwik kumar yadav**  
```
