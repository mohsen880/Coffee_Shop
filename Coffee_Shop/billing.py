
def calc_t(orders):
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total


def calc_discount(total):

    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount


def invoice(orders):

    if len(orders) == 0:
        print("No orders to print!")
        return

    print("\n--------- Invoice ---------")

    for order in orders:
        print("Product:", order["product"])
        print("Quantity:", order["quantity"])

    total = calc_t(orders)
    discount = calc_discount(total)
    final_price = total - discount

    print("---------------------------")
    print("Total Price:", total, "Toman")
    print("Discount:", discount, "Toman")
    print("Final Price:", final_price, "Toman")
    print("===========================")
