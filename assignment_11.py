# Que:1 -> Write a python script to calculate sum of first N natural numbers.
num = int(input('Enter a number where you want to sum of first  natural numbers:'))
total = 0
for i in range(1, num + 1):
    total += i
print(f'Sum of first {num} numbers is = {total}')
# Que:2 -> Write a python script to calculate sum of squares of first N natural numbers.
num = int(input('Enter a number where you want to sum of squares of first  natural numbers:'))
squareTotal = 0
for i in range(1, num + 1):
    squareTotal += i * i
print(f'Sum of squares of first {num} numbers is = {squareTotal}')
# Que:3 -> Write a python script to calculate sum of cubes of first N natural numbers.
num = int(input('Enter a number where you want to sum of cubes first  natural numbers:'))
cubeTotal = 0
for i in range(1, num + 1):
    cubeTotal += i * i * i
print(f'sum of cubes first {num} natural numbers is = {cubeTotal}')
# Que:4 -> Write a python script to calculate sum of first N odd natural numbers.
num = int(input('How many first odd natural numbers you want to add:'))
oddTotal = 0
for i in range(1, num + 1):
    oddTotal += (2 * i - 1)
print(f'sum of  first {num} odd natural numbers is = {oddTotal}')
# Que:5 -> Write a python script to calculate sum of first N even natural numbers.
num = int(input('How many first even natural numbers you want to add:'))
evenTotal = 0
for i in range(1, num + 1):
    evenTotal += 2 * i
print(f'Sum of  first {num} even natural numbers is = {evenTotal}')
# Que:6 -> Write a python script to calculate factorial of a given number.
copyNum = num = int(input('Enter a number that you want to calculate factorial:'))
fact = 1
while num > 0:
    fact *= num
    num -= 1
if num < 0:
    print("Please enter a positive number.")
else:
    print(f"Factorial of {copyNum} is =", fact)
# Que:7-> Write a python script to count digits in a given number.
num = n = int(input('Enter a number that you want to count digits:'))
p = 0
count = 0
if n < 0:
    n = abs(n)  # To update a negative number with positive number.
while n > 0:
    p = n % 10
    n = int(n / 10)     # To remove the float number.
    count += 1
print('Number', num, ' in digits is =', count)
# Que:8 -> Write a python script to calculate sum of digits in a given number.
num = input('Enter a number whose you want to calculate sum of digits:')
Sum = 0
for i in num:
    i = int(i)  # To change the string with int type value.
    Sum += i  # Add numbers and assign the variable Sum.
print('Sum of digits:', Sum)
# Using while loop to perform the above task.
'''p = 0
Sum = 0
num = int(num)
while num > 0:
    p = num % 10
    Sum += p
    num = num // 10  # This gives a result int type value.
print('Sum of digits:', Sum, sep='')'''
# Que:9 -> Write a python script to print binary format equivalent of a given decimal number.(do not use bin()
# function.)
binary = " "
a = num = int(input("Enter a number that you want to convert in Binary: "))
while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = int(num / 2)
print(f"Binary conversion of {a} (in decimal) is = {binary}")
# Que:-10->Write a python script to print octal equivalent of a given decimal number (do not use oct () method.)
b = num = int(input("Enter a number that you want to convert in Octal format:"))
octal = " "
while num > 0:
    rem = num % 8
    octal = str(rem) + octal
    num = int(num / 8)
print(f"Octal Conversion of {b} (in decimal) = {octal}")
