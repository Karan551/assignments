# Que:1 -> Write a python script to reverse a number.
enum = num = int(input("Enter a number that you want to reverse:"))
i = 0
reverseNum = 0
p = 0
while num > 0:
    p = num % 10
    reverseNum = reverseNum * 10 + p
    num = num // 10  # this gives an integer result and remove the floating point number.
print("Entered number is:", enum)
print("Reverse number is:", reverseNum)
# Que:2 -> Write a python script to check whether a given number is Prime or not.
num = int(input('Enter a number that you want to check is Prime or not:'))
# Using for else loop
for i in range(2, num):
    if num % i == 0:  # if given number is divided by any number ,its remainder zero so given number is not Prime.
        # number.
        print(num, 'is not Prime Number.')
        break
else:
    print(num, 'is Prime Number.')
# Que:3-> Write a python script to print all Prime numbers under 100.
count = 0
print('Prime Numbers under 100 is :')
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(f'{i},', end=' ')
        count += 1
print('\nTotal Prime Numbers is =', count, sep=' ')
# Que:4-> Write a python script to print all Prime Numbers between two given numbers (both values are inclusive.)
count = 0
a = int(input('Enter first value:'))
b = int(input('Enter second value:'))
print('Prime Numbers till ', b, ':')
for i in range(a, b + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        if i == 1:
            pass
        else:
            print(i, end=' ')
            count += 1
print('\nTotal Prime Numbers is =', count)
# Que:5->Write a python script to find next Prime Number of a given number.
x = int(input("Enter a number that you want to find the next Prime Number:"))


# Defining a function
def nextPrime(num):
    while True:
        num += 1  # increase value entered by user.
        i = 2
        while i < num:
            if num % i == 0:
                break
            i += 1
        else:
            return num


# Calling a function with string
print('Next Prime Number is = ', nextPrime(x))
# Que:6-> Write a python script to print first N Prime Numbers.
user_input = int(input("How many Prime numbers You want to print:"))
prime = 2  # this is the First Prime Number
count = 1  # counter variable
while count <= user_input:
    i = 2
    while i < prime:
        if prime % i == 0:
            break
        i += 1
    else:
        print(prime, end=" ")
        count += 1
    prime += 1  # increase the value of prime
# user_input = int(input("How many Prime Numbers You want to print:"))
# Que:7 -> Write a python script to check a whether a given pair of numbers are co-Prime numbers or not.
num_1 = int(input("\nEnter first number:"))
num_2 = int(input("Enter second number:"))
# This is the long division method to find the HCF of given two numbers.
bigNum = num_1 if num_1 > num_2 else num_2
smallNum = num_1 if num_1 < num_2 else num_2
while True:
    if bigNum % smallNum == 0:
        coPrime = smallNum
        break
    rem = bigNum % smallNum
    bigNum = smallNum
    smallNum = rem
# condition check for number that coPrime or not
if coPrime == 1:
    print(f"{num_1} and {num_2} are Co-Prime Numbers.")
else:
    print(f"{num_1} and {num_2} are not Co-Prime Numbers.")
# Que:8-> Write a python script to print first N terms of a Fibonacci terms.
user_input = int(input('How many Fibonacci terms you want to print:'))
i = 1
num_1, num_2 = 0, 1
num_3 = 0
while i <= user_input:
    print(num_1, end=" ")
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    # increase the value of i
    i += 1
# Que:9->Write a python script to calculate of LCM of two numbers.
print("\nEnter two numbers that you want to find LCM:")
num1 = int(input('Enter first number: '))
num2 = int(input("Enter second number: "))
bigNum = num1 if num1 > num2 else num2  # find the biggest number among two numbers.
product = num1 * num2  # product of given two numbers.
while bigNum <= product:  # loop starts bigNumber up to product of given numbers.
    if (bigNum % num1 == 0) and (bigNum % num2 == 0):  # condition check for both number divisibility
        print(f"LCM of {num1} and {num2} is ={bigNum}")
        break
    bigNum += 1  # increase the value of bigNum
# Que:10->Write a python script to calculate the HCF of two numbers.
# This is the factor method to find the HCF of the given two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
commonNum = []  # create an empty list
bigNum = num1 if num1 > num2 else num2  # find two numbers between two numbers
i = 1
# loop start from 1 to bigNum
while i <= bigNum:
    # condition check that both numbers is divided from i
    if (num1 % i == 0) and (num2 % i == 0):
        commonNum.append(i)  # divided numbers is appended to the empty list.
    i += 1  # increase the value of i
print(f'H.C.F. of {num1} and {num2} is = {max(commonNum)}')  # find the biggest number in the list commonNum
