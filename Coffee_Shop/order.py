
from menu import menu

orders = []


def add_order():
    product = input("Enter product name: ")

    if product in menu:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            order = {
                "product": product,
                "price": menu[product],
                "quantity": quantity
            }

            orders.append(order)

            print("Order added successfully!")

        else:
            print("Quantity must be greater than zero!")

    else:
        print("This product is not available!")


def show_orders():

    if len(orders) == 0:
        print("No orders registered yet!")

    else:
        print("\n-------- Your Orders --------")

        for order in orders:
            print("Product:", order["product"])
            print("Price:", order["price"])
            print("Quantity:", order["quantity"])
            print("------------------")
