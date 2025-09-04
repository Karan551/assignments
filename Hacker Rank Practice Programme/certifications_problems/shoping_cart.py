# DONE : this task is done

class Item:

    # instantiate constructor
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    cart_item_list = []
    cart_item_price_list = []

    def __init__(self):
        super().__init__()

    def add(self, item: Item):
        self.cart_item_list.append(item.name)
        self.cart_item_price_list.append(item.price)

    def total(self):
        return sum(self.cart_item_price_list)

    def __len__(self):
        return len(self.cart_item_list)

    def show_cart(self):
        return " ".join(self.cart_item_list)


# not used for testing purpose
def add_item_in_cart():
    number_of_items = int(input("How many items you want to add: "))

    for _ in range(number_of_items):
        prod_name, prod_price = input("Enter product name and price space separated: ").split()

        item = Item(prod_name, int(prod_price))

    return

# not used for testing purpose
def cart_input(prod_item):
    while True:
        user_choice = int(input("""
            Enter Your choice :
            1. To know number of items in cart.
            2. To add product in cart.
            3. To get total cost from your cart.
            4. Exit
            """))
        cart = ShoppingCart()
        if user_choice == 1:
            print("No of items in your cart: ", len(cart))
        elif user_choice == 2:
            cart.add(prod_item)
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            break
        else:
            print("Please enter a valid input.")
            continue


if __name__ == '__main__':

    number_of_items = int(input("How many items you want to add: "))

    obj = ShoppingCart()

    for _ in range(number_of_items):
        prod_name, prod_price = input("enter product name and product price space separated: ").split()
        item = Item(prod_name, int(prod_price))

        obj.add(item)

    print("total cost ::", obj.total())
    print("No. of items::", len(obj))
    print(obj.show_cart())

