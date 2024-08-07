def yell(text):
    return text.upper() + "!"


def greet(func):
    result = func("hello i'm a python developer.")
    print(result)


# function call
# greet(yell)


def outer_function(text):
    # function definition
    def inner_function(t):
        return t.lower()

    # inner function call
    return inner_function(text)


#  function call
# print(outer_function("HELLO WORLD HOW ARE YOU"))

#  Example of closure :-
def my_func(x):
    def chai_func(n):
        return n ** x

    return chai_func


square_num = my_func(2)


# print(square_num(5))
# print(square_num(10))

# cube
# cube_num = my_func(3)
# print("cube is :", cube_num(5))
# print("cube is :", cube_num(7))

# print("cube is :", my_func(3)(5))
# print("cube is :", my_func(3)(4))

class Adder:
    def __init__(self, num):
        self.num = num

    def __call__(self, x):
        return self.num + x


plus_5 = Adder(5)

print(plus_5(12))
print(plus_5(13))