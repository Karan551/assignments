def func_add(num1, num2):
    return num1 + num2


#  Closure:- A function that can refer environments that are no longer active.

# A closure allows you to bind variables into a function without passing them as parameters.
def my_func(num, b):
    def actual(x):
        print(f"this is first value {num} and this is second value {x}")
        print(f"first parameter is {num}\n next parameter {b}")
        # return num ** x
        return (num + b) * 2

    return actual


# print("Sum of two number is :", func_add(12, 15))
# result = my_func(20, 15)
# print("result:", result)
# print("final result is :", result(2))
# # print(my_func(20))


def chai_coder(num):
    def actual(x):
        return x ** num

    return actual


f = chai_coder(3)
print("final result is (cube):", f(2))
print("final result is (cube):", f(3))

f = chai_coder(2)
print("square is :", f(10))
print("square is :", f(5))
