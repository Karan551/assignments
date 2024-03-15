# Que:1-> Write a python program to create a simple function which prints "MySirG".
def print_MySirG():
    print(' "MySirG" ')


# calling a function
print_MySirG()


# Que:2-> Write a python program to create a function which expects(needs) two arguments and print
# them in the function body.


def print_arguments(x, y):
    print('first name is:', x)
    print('second name is:', y)


# calling a function
print_arguments('Kartik', 'GladeRial')


# Que:3 -> Write a python program to create a function which expects an unknown number of arguments.


def add(*element):
    print('Number of arguments:', len(element))
    print("Passed arguments is :", element)
    print('Sum of total number is that you entered:', sum(element))


# calling a function
add(5, 2, 31, 4, 7, 8)


# Que:4-> Write a python program to create a function which expects kwargs arguments.


def fun(**kwargs):
    for key, values in kwargs.items():
        print(key, ':', values)


# function calling
fun(first='Python', second='Java', third='C', fourth='C#')
# Que:5-> Write a python program to create a function which expects list as an argument.
tp = (1, 2, 3, 4, 5, 6, 7, 8)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# defining function
def identify_list(element):
    if type(element) == list:
        return True
    return False


print("Given element is list :", identify_list(tp))  # calling a function
print("Given element is list :", identify_list(lst))  # calling a function

# Que:6-> Write a python program to create a function that find a maximum of four arguments.
print('enter four numbers:')
a, b, c, d = int(input()), int(input()), int(input()), int(input())


def greatest_num(num1, num2, num3, num4):
    print(f'Entered number is : {num1} , {num2}, {num3} , {num4}')
    if (num1 > num2) and (num1 > num3):
        print(f'{num1} is the greatest number.') if num1 > num4 else print(f'{num4} is the greatest number.')
    elif num2 > num3 and num2 > num4:
        print(num2, 'is the greatest number.') if num2 > num1 else print(num1, 'is the greatest number.')
    elif num3 > num4 and num3 > num1:
        print(num3, 'is the greatest number.') if num3 > num2 else print(num4, 'is the greatest number.')
    else:
        print(num4, 'is the greatest number.')


# calling a function
greatest_num(a, b, c, d)
# Que:7-> Write a python program to sum all the numbers in a List.
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]


def list_sum(element):
    if isinstance(element, list):  # using isinstance() to find the given element is list or not.
        total = 0
        for i in element:
            if type(i) == int:
                total += i
            elif type(i) == list:
                total += list_sum(i)
        return total
    return "Please Pass an element as a List."


# calling a function and print the result.
print('Sum of all list elements is:', list_sum(lst2))
# Que:8->Write a python program to create a function to check whether number falls in a given range.
start_num = int(input("Enter a number for starting range:"))
end_num = int(input("Enter a number for ending range:"))
small_num = min(start_num, end_num)
big_num = max(start_num, end_num)
print(f"Range is {small_num, big_num} where {big_num} is involved.")
user_input = int(input("Enter a number that you want to check for above range:"))


def check_range(x, y, z):
    isRange = range(y, z + 1)
    if x not in isRange:
        return False
    return True


# calling a function and compare with boolean value.
# if condition is True then below code is execute otherwise else code block is executed
if check_range(user_input, small_num, big_num):
    print(f"Number {user_input} is in the given range {small_num, big_num}")
else:
    print(f"Number {user_input} is not in the given range {small_num, big_num}")

# Que:9-> Write a python program to multiply all the numbers in a list.
product_list = [1, 2, 3, 4, "hello", "Python", [2, 1], [2, 1]]


def list_multiply(element):
    if isinstance(element, list):
        prod = 1
        for i in element:
            if isinstance(i, int):  # if list element is int then multiply.
                prod *= i
            elif isinstance(i, list):
                # if list element is a sublist of given list then multiply all sublist elements.
                prod *= list_multiply(i)  # call the above function again and multiply the all elements.
        return prod
    return "Please pass an element as a List."


print('Multiplication of all list elements is =', list_multiply(product_list))
# Que:10-> Write a python program to create a function to check whether a given number is even or odd.
user_input = int(input('Enter number that you want to check Even or Odd:'))


def evenOdd(num1):
    if num1 % 2 == 0:
        print(num1, 'is the even number.')
    else:
        print(num1, 'is the odd number.')


# calling a function
evenOdd(user_input)
