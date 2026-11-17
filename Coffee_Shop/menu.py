menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000
}


def show_menu():
    print("MENU FUNCTION IS WORKING!")

    print("\n------- Coffee Menu -------")

    for product, price in menu.items():
        print(product, ":", price, "Toman")