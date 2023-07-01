# import ascii_lowercase to get all the alphabet letters in lowerCase.
from string import ascii_lowercase

# Que:1-> Write a python program to create a function that takes a list and returns a new list with the
# original list unique elements.
lst = [1, 2, 3, 4, 4, 4, 4, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3]  # create a list of duplicate elements


# create a function that convert a list into unique list elements.
def uniqueList(a):
    print("Entered list is =", a)
    return list(set(a))


# calling a function and assign the result into the variable.
unique_list_element = uniqueList(lst)
print('Unique list elements is =', unique_list_element)

# Que:2-> Write a python program to create a function that takes a number as a parameter and checks
# if the number is prime or not.
user_input = int(input('Enter a number that you want to check is Prime or not:'))


def isPrime(num):
    """
    @param:num
    @return:f-string
    """
    for i in range(2, num):
        if num % i == 0:
            return f"{num} is not a Prime Number."
    return f"{num} is a Prime Number."


# calling a function and print the result.
print(isPrime(user_input))
# Que:3-> Write a python program to create a function that prints the even numbers from  a given list:
# Sample list :[1,2,3,4,5,6,7,8,9]
sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sample list is =", sampleList)


# define a function
def evenFunction(num):
    print("Even elements of the given list is :", end=" ")
    for i in range(len(num)):
        if num[i] % 2 == 0:
            print(num[i], end=" ")


# calling a function
evenFunction(sampleList)
# Que:4-> Write a python program to create a function that checks whether a passed string is
# Palindrome or not.
user_input = input("\nEnter a string that you want to check that is Palindrome or not:")


def check_palindrome(word):
    """
    @bref:To check that given string is Palindrome or not.
    :param word:
    :return:string
    """
    # reverse the given word or string and convert into iterable like :- list,tuple
    reverse_word = word[-1::-1]
    if word == reverse_word:
        return "This is a Palindrome String."
    return "This is not a Palindrome String."


# calling a function and print the result.
print(check_palindrome(user_input))

# Que:5-> Write a python program to create a function to find the Min. of three numbers.
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
num3 = int(input('Enter third number:'))


def findGreaterNumber(a, b, c):
    """
    @bref: To get the greatest number provided three numbers by user.
    @param:a,b,c
    @return:None

    """
    if a > b and a > c:
        print(a, 'is the greatest number.')
    elif b > a and b > c:
        print(b, 'is the greatest number.')
    else:
        print(c, 'is the greatest number.')


# calling a function
findGreaterNumber(num1, num2, num3)


# Que:6-> Write a python program to create a function and print a list where the values are square
# of numbers between 1 to 30.
def listNumberSquare():
    """
    @bref:To find the square of numbers between 1 to 30.
    :return:list[int]
    """
    square_num_list = [i * i for i in range(2, 30)]
    return square_num_list


# calling a function and print the result
square_list = listNumberSquare()
print('Square number list between 1 to 30 is : \n', square_list)
# Que:7-> Write a python program to access a function inside a function.
user_num = int(input("Enter a number that you want to add 10:"))


def outerFunction(num):
    num = num

    # defining innerFunction
    def innerFunction():
        # change the value of num using nonlocal keyword
        nonlocal num
        num += 10
        print(f"The result is = {num}")

    # calling inner function
    innerFunction()


# calling outer function
outerFunction(user_num)

# Que:8-> Write a python program to create a function that accepts string and calculate the
# number of uppercase letters and lowercase letters.
user_input = input('Enter a string in which you want to count the uppercase letter and lower case letter:')


def letterCount(string):
    """
    @param :string
    @return: string
    """
    space = upperCount = 0
    lowerCount = 0
    for st in string:
        if 65 <= ord(st) <= 90:
            upperCount += 1  # increase the value of upperCount for uppercase letters.
        elif 97 <= ord(st) <= 122:
            lowerCount += 1  # increase the value of lowerCount for lowercase letters.
        elif ord(st) == 32:
            space += 1  # increase the value of space for space.
        else:
            print("Invalid Input")
            break
    return f'No of lower case letter:{lowerCount}\nNo of Upper case letter:{upperCount}\nNo of spaces is = {space}'


ct = letterCount(user_input)  # calling a function
print(ct)
# Que:9-> Write a python program to create a function to check whether a string is a panagram or not.
user_string = input("Enter a string that you want to check is panagram or not:")


def panagram(text):
    """
    @bref:Those strings are panagram that contains all the letters of the alphabet.With the help of
    this function we can find the panagram string.
    @param: text
    :return: bool
    """
    # To get the all letters of the alphabet.
    alphabet = ascii_lowercase
    text = text.lower()  # To convert the sentence into lowercase.
    # loop until letter in alphabet (26 times)
    for letter in alphabet:
        # To check that each letter inside the user pass sentence.
        if letter not in text:
            return False
    return True


# call the function and check the condition is True or not.
if panagram(user_string):
    print("This is a Panagram String.")
else:
    print("This is not a Panagram String.")

# Que:10-> Write a python program to create a function to check whether a string is an anagram not.
user_input1 = input("Enter a first word that you want to check is an anagram or not:")
user_input2 = input("Enter a second word that you want to check is an anagram or not:")


def check_anagram(word1, word2):
    """
    @bref: An anagram is a word or phrase formed by rearranging the letters of a different word or a phrase,
            typically using all the original letters exactly once.
    :param word1:
    :param word2:
    :return:string
    """
    # first convert both words into lowercase words and resultant word into a list and compare both list.
    if sorted(word1.lower()) == sorted(word2.lower()):
        return "Both Words are Anagram."
    return "Both Words are not Anagram."


# calling a function and print the result.
print(check_anagram(user_input1, user_input2))
