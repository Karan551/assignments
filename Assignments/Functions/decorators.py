from time import sleep


def decorator(func):
    def wrapper(*args, **kwargs):
        print("function name is :", func.__name__)
        return func(*args, **kwargs)

    return wrapper


# a function that no parameter
def say_whee():
    print("Hello Python How are You ?")


# decorator(say_whee)()

#  if a function passing a parameter.
def user_info(name):
    print(f"Hi {name} how are you?")


#  if a function return something then

@decorator
def add_num(num1, num2):
    return num1 + num2


# -------------------------Test code

# -----------1st method
# decorator(user_info)("Master")
# print(decorator(user_info)("master"))

# ----------2nd method
# my_user = decorator(user_info)
# my_user("Master")

# -----

# my_num = decorator(add_num)
# print("result is :", my_num(12, 15))

# print("Result is :", add_num(12, 15))


def my_num(*args, **kwargs):
    # sleep(3)
    # print("after 3 seconds.")
    pos_arg = len(args)
    other_arg = len(kwargs)
    print("total pos_arg", pos_arg)
    print("total kwarg_arg", other_arg)
    print("Total arguments are:", pos_arg + other_arg)


# my_num(12, 14, 15, 18, 20, 25, 28, 101, num1=50, num2=101, num3=505)

def parent():
    print("This is parent function.")

    # function definition
    def first_child():
        print("This first child function Inside parent function.")

    # function definition
    def second_child():
        print("This is second child function Inside parent function.")

    # function call
    second_child()
    first_child()


# call parent function
# parent()

def parent_2(num):
    def first_child():
        return "Hi I'm First Child."

    def second_child():
        return "Hi I'm Second Child."

    if num == 1:
        return first_child
    else:
        return second_child


first = parent_2(1)
second = parent_2(2)

print(first())
print(second())
