
from menu import show_menu
from order import add_order, show_orders, orders
from billing import calc_t, invoice


def main():

    while True:

        print("\n========== Coffee Shop ==========")
        print("1. Show Menu")
        print("2. Add Order")
        print("3. Show Orders")
        print("4. Calculate Total")
        print("5. Print Invoice")
        print("6. Exit")

        choice = input("Your choice: ")

        if choice == "1":
             print("Option 1 Selected!")
             show_menu()

        elif choice == "2":
            add_order()

        elif choice == "3":
            show_orders()

        elif choice == "4":
            total = calc_t(orders)
            print("Total Price:", total, "Toman")

        elif choice == "5":
            invoice(orders)

        elif choice == "6":
            print("Thank you for choosing our coffee shop!")
            break

        else:
            print("Invalid choice! Please try again.")


main()
