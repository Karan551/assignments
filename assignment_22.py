# Que:1-> Write recursive python function to calculate sum of first N natural numbers.
num = int(input('How many natural numbers you want to add:'))


def add(n):
    if n == 1:
        return 1
    return n + add(n - 1)


print(f"Sum of first {num} natural numbers is = {add(num)}")  # function  calling
# Que:2-> Write a recursive python function to calculate sum of first N odd natural numbers.
num = int(input('How many first N odd natural numbers you want to add: '))


def oddSum(n):
    if n == 1:
        return 1
    return (2 * n - 1) + oddSum(n - 1)


print(f'Sum of first {num} odd numbers is =', oddSum(num))  # function calling
# Que:3-> Write a recursive python function to calculate sum of first N even natural numbers.
num = int(input('How many first N even natural numbers you want to add: '))


def evenSum(n):
    if n == 1:
        return 2
    return 2 * n + evenSum(n - 1)


print(f'Sum of first {num} even natural numbers = {evenSum(num)}')  # function calling
# Que:4->Write a recursive python function to calculate sum of squares of first N natural numbers.
num = int(input('How many first N natural numbers squares you want to add: '))


def squareSum(n):
    if n == 1:
        return 1
    return n * n + squareSum(n - 1)


print(f'Sum of first {num} natural numbers squares is = {squareSum(num)}')  # function calling
# Que:5-> Write a recursive python to calculate sum of cubes of first N natural numbers.
num = int(input('How many numbers cubes you want to add:'))


def cubeSum(n):
    if n == 1:
        return 1
    return n * n * n + cubeSum(n - 1)


print(f'Cube Sum of first {num} numbers is =', cubeSum(num))  # function calling
# Que:6->Write a recursive python function to calculate the factorial of a number.
num = int(input('Enter a number that you want to find factorial: '))


def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        return n * factorial(n - 1)
    else:
        print('Please enter a positive number.')


print(f'Factorial of {num} is =', factorial(num))  # function calling
# Que:7-> Write a recursive python function to calculate sum of digits of a given number
num = int(input('Enter a number that you want to add digits:'))


def digitSum(n):
    if n > 0:
        return n % 10 + digitSum(int(n / 10))
    return 0


print(f'Digit sum of {num} is =', digitSum(num))  # function calling
# Que:8-> Write a recursive python function to print binary of a given decimal number.
num = int(input('Enter a number that you want to convert in binary:'))
print(f'Binary conversion of {num} is =', end=' ')


def decToBin(n):
    if n > 0:
        decToBin(int(n / 2))
        print(n % 2, end='')


decToBin(num)  # function calling
print()
# Que:9-> Write a recursive python function to print octal of a given number.
num = int(input('Enter a number that you want to convert in octal:'))
print(f'Octal conversion of {num} is =', end=' ')


def decToOct(n):
    if n > 0:
        decToOct(int(n / 8))
        print(n % 8, end='')


decToOct(num)  # function calling

# Que:10->Write a recursive python function to find the Nth term of the Fibonacci series.
num = int(input('\nWhich Fibonacci Term you want to print:'))


def fib(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(f'{num} th Fibonacci Term is =', fib(num))  # function calling
