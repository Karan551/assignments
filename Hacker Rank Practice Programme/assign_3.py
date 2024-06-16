# This file contains the
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque


def defaultDictProblem():
    lst = ["Python", "Java", "C++"]
    # dct = defaultdict(list)
    # dct['python'].append("awesome")
    # dct['js'].append("fun")
    # dct['something'].append("new")
    # print("This is default dict:\n", dct)
    # for i in dct.items():
    #     print(i)
    dct_a = defaultdict(list)
    dct_b = defaultdict(list)
    n, m = input("Enter the value of N | M: ").split()
    n = int(n)
    m = int(m)

    groupA = [input('enter group A elements: ') for i in range(n)]
    # for _ in range(int(n)):
    #     user_input = input("enter value of Group A: ")
    #     lst_a.append(user_input)

    print("this is first dict:", groupA)

    # for _ in range(int(m)):
    #     user_input = input("enter value of Group B: ")
    #     lst_b.append(user_input)
    groupB = [input('enter group B elements: ') for i in range(m)]
    print("this is first dict:", groupB)


defaultDictProblem()

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


# dequeMethods()


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

# total_shoe_amount = 0


def counterProblem():
    total_shoe_amount = 0

    number_of_shoes = int(input("Enter number of shoes: "))
    available_shoes_size_lst = input("Enter shoes size space separated :").split()
    count_shoes = Counter(available_shoes_size_lst)

    # if number_of_shoes == len(available_shoes_size_lst):

    total_customers = int(input("Enter number of customers: "))
    for _ in range(total_customers):
        shoes_size, price = input("Enter shoe size | price ").split()
        price = int(price)
        if shoes_size in count_shoes.keys():

            if count_shoes[shoes_size] > 0:
                total_shoe_amount += price
            count_shoes[shoes_size] -= 1

    print("Total price :", total_shoe_amount)


# counterProblem()


def practiceCounter():
    myList = [1, 3, 2, 10, 11, 1, 2, 1, 2, 1, 11, 2, 11, 22, 44, 1, 10, 10, 11, 10]
    result = Counter(myList)
    print("this is initial result:", result)
    user_input = int(input("enter number that you want: "))

    if user_input in myList:
        result[user_input] -= 1
        pass
    print('This is final result: ', result)


# practiceCounter()


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
