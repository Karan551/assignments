# This file contains the
from collections import defaultdict, namedtuple, OrderedDict, deque


def defDict():
    lst = ["Python", "Java", "C++"]
    dct = defaultdict(list)
    dct['python'].append("awesome")
    dct['js'].append("fun")
    dct['something'].append("new")
    print("This is default dict:\n", dct)
    for i in dct.items():
        print(i)


Point = namedtuple('Point', 'x,y,z')
# print(Point.__doc__)
pt1 = Point(10, 20, 50)


# print(pt1[0], pt1.y, pt1.z)
# print(pt1)
# print(pt1.y)
def namedTuple():
    total_student = int(input("How many students are their: "))
    Student = namedtuple('Student', input("enter column name ").upper().split())
    total_marks = 0
    for _ in range(0, total_student):
        data = input("Student Information ID | NAME | MARKS | CLASS :").split()
        if len(student_column) == len(data):
            students = Student(*data)
            total_marks += int(students.MARKS)


unordered_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print(unordered_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

# print("This is ordered dict:\n", ordered_dict)
# ordered_dict['c'] += 100
# ordered_dict['d'] = 40
# user_product_dct = OrderedDict()
# print("This is ordered dict:\n", ordered_dict)
# total_lst = []
# print(ordered_dict.keys())

product_order_dict = OrderedDict()
# product_order_dict.update(name="Ganesh", price=40)
# print(product_order_dict)
# print('names' in product_order_dict)

total_price = 0


# print("This is product first order dict", product_order_dict)


def superMarket():
    item_count = int(input("How many items you will buy: "))
    for _ in range(item_count):
        # user_product, net_price = input("Enter product name | price separated by space :").split()
        product_lst = input("Enter product name | price separated by space :").split()
        print(product_lst)
        user_product = ' '.join(product_lst[:-1])
        net_price = product_lst[-1]
        print("This is product", user_product)
        print("this is net price :", net_price)
        net_price = int(net_price)
        if user_product in product_order_dict:
            product_order_dict[user_product] += net_price
        else:
            # if new elements insert then do this
            product_order_dict[user_product] = net_price

    for name, price in product_order_dict.items():
        print(name, price)


# superMarket()

# n = int(input("how many products you want buy: "))
# order_dict = OrderedDict()  # Using OrderedDict to preserve the order of input
# print("This is product order dict", order_dict)
# while n > 0:
#     order = input("Enter product name: ")
#     price = int(input("Enter product price: "))
#
#     if order in order_dict:
#         order_dict[order] += price
#     else:
#         order_dict[order] = price
#
#     n -= 1


def dequeMethods():
    dct = deque()
    dct.append(10)
    dct.appendleft(12)
    dct.extend([20, 12, 25, 30, 35, 12])
    print("this is Deque: ", dct)
    print("This is element is pop: ", dct.pop())
    print("this is Deque: ", dct)
    dct.extendleft([120, 125, 130, 135])
    print("this is Deque: ", dct)
    # dct.reverse()
    dct.rotate(6)
    print()
    print("this is Deque: ", dct)
    # print("count", dct.count(12))
    for i in dct:
        print(i, end=' ')


dequeMethods()


def dequeProblem():
    num_operations = int(input("How many operations you want to perform: "))
    deque_object = deque()
    for _ in range(num_operations):
        user_choice = input("Enter operations space separated value: ").split()
        if user_choice[0] == "append":
            value = user_choice[-1]
            deque_object.append(value)

        elif user_choice[0] == "appendleft":
            value = user_choice[-1]
            deque_object.appendleft(value)

        elif user_choice[0] == "pop":
            deque_object.pop()

        elif user_choice[0] == "popleft":
            deque_object.popleft()

    print("This is deque:", deque_object)


# dequeProblem()


# ------------------------

# To find the fibonacci number using generator


def fib(num=5):
    first_num, second_num = 0, 1
    for _ in range(num):
        # print(first_num, end=' ')
        yield first_num
        first_num, second_num = second_num, first_num + second_num


# function call
# user_input = int(input("How many fibonacci numbers you want to print:"))
# print(list(fib(user_input)))
# print("Cube of fib numbers :", list(map(lambda x: x ** 3, fib(user_input))))


def num():
    pass
