def fizzBuzz(n):
    # Write your code here
    for i in range(1, n + 1):
        # print(i)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        elif i % 3 != 0 or i % 5 != 0:
            print(i)


# fizzBuzz(int(input("Enter a number:").strip()))

class Item:
    # Implement the Item here
    def __init__(self, name, price):
        self.name = name
        self.price = price

    pass


class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.item_lst = []
        self.count = 0
        self.price = None

    def add(self, item):
        self.item_lst.append(item)

    def len(self):
        return len(self.item_lst)

    def total(self):
        for item in self.item_lst:
            self.count += item.price

        return self.count


items = []


def cartOperation():
    n = int(input("How many Items: "))
    for _ in range(n):
        name, price = input("Enter Producnt info: ").split()
        item = Item(name, int(price))
        print("This is item Object :", item.name, item.price)
        items.append(item)


cart = ShoppingCart()
# cart.add()
# for _ in range(3):
#     a=input("enter comma")
cartOperation()
print(items)
print("Total Price : ", cart.total())


# for item in items:
#     print(item.name, item.price)


def operation():
    q = int(input("How many command you want to enter: "))

    for _ in range(q):
        line = input("Enter info ").split()
        command, params = line[0], line[1:]
        if command == "len":
            print(cart.len())
            pass
            # fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            print(str(cart.total()) + "\n")
            pass
            # fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)


operation()
print("Total Price : ", cart.total())
print()
