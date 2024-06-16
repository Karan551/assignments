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
main_string = input("Enter Main string that you want: ")


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
    result_lst = []
    while main_string.find(sub_string) != -1:
        result_lst.append(main_string.find(sub_string))
        main_string = main_string.replace(sub_string, "*", 1)


# Que:-4
def reverse_string(user_string: str):
    result = reversed(user_string)
    result = list(result)
    return "".join(result)
    # This is another method using slicing
    # print(main_string[::-1])


# function call
# print(reverse_string(main_string))


def reverse_words(user_string: str):
    lst = user_string.split()
    result = lst[::-1]
    # for i in result:
    #     print(i, end=' ')
    # This is shorthand
    print(" ".join(result))


reverse_words(main_string)
