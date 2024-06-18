import re


# Que:-1
# user_input = input("Enter string that you want: ")
# for char in range(len(user_input)):
#     print(f"Positive index of {user_input[char]} {char}, And Negative Index Is {char - len(user_input)} ")

# Que:-2
# ---------- 1st Method
# user_input = input("Enter string that you want: ")
# i = 0
# print("In Forward Direction :-")
# while i < len(user_input):
#     print(user_input[i])
#     i += 1
# print("In Backward Direction :-")
# counter = len(user_input) - 1
# while counter >= 0:
#     print(user_input[counter])
#     counter -= 1

# ---------- Alternative Method
# print("In Forward Direction")
# for char in user_input:
#     print(char)
# for char in user_input[::]:
#     print(char)
# print("In Backward Direction:-")
# for char in user_input[::-1]:
#     print(char)

# Que:3
# main_string = input("Enter Main string that you want: ")


# sub_string = input("Enter Sub string that you want: ").lower()


def find_all_string_using_list():
    result = [index for index in range(len(main_string)) if main_string.startswith(sub_string, index)]
    print(result)


def find_all_substring():
    counter = False
    pos = -1
    length = len(main_string)
    while True:
        pos = main_string.find(sub_string, pos + 1, length)
        if pos == -1:
            break
        print("Found at position :", pos)
        counter = True

    if not counter:
        print("Substring not found.")


# ------------- 3rd method using re module
def re_find_all():
    for i in re.finditer(sub_string, main_string):
        print(i.start())


# ------------ 4th method using list method
def list_find_all_substring():
    user_string = input("Enter the string that you want: ")
    sub_string = input("Enter sub string that you want: ")
    result_lst = []
    while user_string.find(sub_string) != -1:
        result_lst.append(user_string.find(sub_string))
        user_string = user_string.replace(sub_string, "*", 1)


# Que:-4
def reverse_string(user_string: str):
    result = reversed(user_string)
    result = list(result)
    return "".join(result)
    # This is another method using slicing
    # print(main_string[::-1])


# function call
# print(reverse_string(main_string))

# Que:-5
def reverse_words(user_string: str):
    lst = user_string.split()
    result = lst[::-1]
    # for i in result:
    #     print(i, end=' ')
    # This is shorthand
    print(" ".join(result))


# call a function
# reverse_words(main_string)

# Que:6
def reverse_internal_words(words: str):
    word_lst = []
    for word in words.split():
        word_lst.append(word[::-1])

    print(" ".join(word_lst))


#  call a function
# reverse_internal_words(input("Enter a string "))

# Que:7
def even_odd__position_string():
    user_string = input()
    #  First method

    # print("This is even Position characters ", user_string[0::2])
    # print("This is odd Position characters ", user_string[1::2])

    # Second Method
    counter = 0
    print("Even Places characters :")
    while counter < len(user_string):
        print(user_string[counter], end="")
        counter += 2

    print()
    counter = 1
    print("Odd Places characters :")
    while counter < len(user_string):
        print(user_string[counter], end="")
        counter += 2


# even_odd__position_string()


# Que:8
def merge_characters_1():
    """
    This function is used to merge two strings with alternative letters, Using for loop and zip().
    :return: None
    """
    result = ""
    first_string = input("Enter first string: ")
    second_string = input("Enter second string: ")
    for i, j in zip(first_string, second_string):
        result += i + j
    print(result)


# function call
# merge_characters_1()

def merge_characters_2():
    """
    This function is used to merge two strings with alternative letters, Using while loop.

    :return:None
    """
    first_string = input("Enter first string: ")
    second_string = input("Enter second string: ")
    i, j = 0, 0
    output = ""
    while i < len(first_string) or j < len(second_string):
        if i < len(first_string):
            output += first_string[i]
            i += 1
        if j < len(second_string):
            output += second_string[j]
            j += 1
    print(output)


# function call
# merge_characters_2()


# Que:9
def sort_string_number():
    user_input = "B4A1D3"
    char_lst = []
    number_lst = []
    for char in user_input:
        if char.isalpha():
            char_lst.append(char)

    char_lst.sort()

    for char in user_input:
        if char.isdigit():
            number_lst.append(char)

    number_lst.sort()

    print("".join(char_lst + number_lst))


# call a function
sort_string_number()


def sort_string_number_2():
    user_input = input("Enter a string: ")
    char = number = output = ""
    for i in user_input:
        if i.isalpha():
            char += i
        else:
            number += i
    for i in sorted(char):
        output += i

    for i in sorted(number):
        output += i

    print(output)


# sort_string_number_2()

#  Que:10
def string_repetition():
    user_input = "a4b3c2"
    chars = user_input[0::2]
    numbers = user_input[1::2]
    for char, num in zip(chars, numbers):
        print(char * int(num), end="")


string_repetition()
