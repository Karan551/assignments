# --------------------This file contains set practice questions---
from collections import Counter

a = ["1", "2"]
b = ["3", "4"]
z = ["Python", "JavaScript", "Ruby", "Perl"]
print(" ".join(z))
print(" ".join(a))
# print(''.join(a))
# c = product(a, b)
# print(c)
# print(list(product("".join(a), "".join(b))))
print()
# c = [i for i in product(a, b)]
# print(c)
# for i in c:
#     print(i)
# for a, b in i:
#     print(int(a),int(b))


# print(','.join(c))


# st = {1, 'Hello', "Python", "java", "Str", 14, 20}
# st2 = {14, "Hello", "java", "Str", "Python", 20, 1}

# print("Both sets are equal :", st == st2)
# print("Both sets are not equal :", st != st2)


ls = [154, 161, 167, 170, 171, 174, 176, 182]
st = {10, 11, 15, 20}  # --> 11,20
st2 = {20, 11, 14, 21}
# st2.difference(st)
# This is actual symmetric difference method (explain)
sym_diff = st.difference(st2) | st2.difference(st)


# print("difference", sym_diff)
# print('This is symmetric difference: -', st.symmetric_difference(st2))
# user_input_lst = input("Enter a space separated value: ").split()
# user_input_lst2 = input("Enter a space separated value: ").split()
# print("This is user input:", user_input_lst)
# num_1 = set(map(int, user_input_lst))
# num_2 = set(map(int, user_input_lst2 ))
# print("This user int input value:", num)
# print("this is symmetric difference \n", num_1.symmetric_difference(num_2))


# ----------------------------
def positiveNum(num):
    return 0 < int(num) <= 9


# set_element = int(input("enter number of elements:"))
# s = set(map(int, input("enter space separated elements:").split()))
# commands = int(input("Enter number of commands: "))


def setRemoveOperation():
    for i in range(commands):
        user_input = input(" enter pop | discard | remove ").split()
        if user_input[0] == "pop":
            s.pop()
        elif user_input[0] == "discard":
            value = int(user_input[1])
            s.discard(value)
        elif user_input[0] == "remove":
            value = int(user_input[1])
            if value in s:
                s.remove(value)


# print("Final set ", s)
# print("Total Sum is ", sum(s))
# s = {"hello", "Python", "Java", "Js"}
# print("Total count Is:", len(s))
def setAddOperation():
    s = set()
    count = int(input("Enter the total number of country stamps: "))
    for i in range(count):
        country_name = input("enter country name:")
        s.add(country_name)

    print("final country name: ", s)
    print("Total different country name :", len(s))


def commonGroupStudent():
    english_group_student = int(input("Enter total number of students: "))
    english_group_roll_number = input("Enter a roll number space separated:").split()
    french_group_student = int(input("Enter total number of students: "))
    french_group_roll_number = input("Enter a roll number space separated:").split()
    set_one = set(english_group_roll_number)
    set_two = set(french_group_roll_number)
    print(set_one, "\n", set_two)
    # This is symmetric difference (actual detail method)
    common_2 = set_one.difference(set_two) | set_two.difference(set_one)
    common = set_one ^ set_two
    print("common students: ", common)
    print(" number of common students: ", len(common))
    print("This is second method to solve this question:", common_2)
    print(" number of common_2 students: ", len(common_2))


def setOperation():
    elements = int(input("Enter number of element: "))
    set_one = set(input("Enter space separated elements: ").split())

    if elements != len(set_one):
        print("Please enter correct input.")
    else:
        other_set = int(input("Enter number of other set: "))
        for i in range(other_set):
            operation = input("""Enter operation name intersection_update | update                          | symmetric_difference_update | 
                              difference_update  followed by value
                               : """).split()
            second_set = set(input("Enter another set value space separated: ").split())
            if operation[0] == "intersection_update":
                set_one.intersection_update(second_set)
                print("after inter section update operation \n:", set_one)

            elif operation[0] == "update":
                set_one.update(second_set)
                print("after update operation \n:", set_one)

            elif operation[0] == "symmetric_difference_update":
                set_one.symmetric_difference_update(second_set)
                print("after symmetric update operation \n:", set_one)

            elif operation[0] == "difference_update":
                set_one.difference_update(second_set)
                print("after difference update operation \n:", set_one)

    print("The update set value is :", set_one)
    set_two = set(map(int, set_one))
    print("Total sum : ", sum(set_two))


# check subset
def subset():
    test_case = int(input("Enter the number of text case: "))
    for _ in range(test_case):
        set_one_length = int(input("Enter the number of elements in first set :"))
        set_one = set(input("enter space separated elements :").split())
        # check the length of set
        if set_one_length != len(set_one):
            break

        set_two_length = int(input("Enter the number of elements in second set :"))
        set_two = set(input("enter space separated elements :").split())
        # check the length of set
        if set_two_length != len(set_two):
            break
        statement = set_one.issubset(set_two)
        print("Subset are not: ", statement)


# Check strict superset
def strictSuperset():
    superSet = set(map(int, input("Enter space separated elements : ").split()))
    other_set = int(input("Enter number of other set: "))
    lst = []
    for _ in range(other_set):
        subset_1 = set(map(int, input("Enter space separated elements : ").split()))
        temp = True
        result = superSet.issuperset(subset_1)
        lst.append(result)

    print("result list is :", lst)
    print("Some values are TRue -----:", all(lst))


def symmetricDifference():
    result = None
    # symmetric difference
    size_set_one = int(input("enter the length of first set :"))
    first_set = set(map(int, input("enter space separated elements: ").split()))

    size_set_two = int(input("enter the length of second set :"))
    second_set = set(map(int, input("enter space separated elements: ").split()))

    if len(first_set) != size_set_one or len(second_set) != size_set_two:
        print("error")
    else:
        set_result = first_set.symmetric_difference(second_set)
        result = sorted(set_result)
        # print("result is:\n", set_result)
        # print("result is:\n", sorted(set_result))

    print(result)


# captain room
# size of each group -> 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
# lst = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]


# print("This is unique room number :", unique_room_number)


def captainRoom():
    # group_of_families = int(input("Enter the group of families: "))
    # room_number_lst = list(map(int, input("Enter space separated room number: ").split()))
    unique_room_number = set(room_number_lst)
    for room in unique_room_number:
        room_number_lst.remove(room)
        # print(f"this room number list and the length is {len(room_number_lst)}:", room_number_lst)
        if room not in room_number_lst:
            print(room)
            break


def captainRoom_2():
    group_of_families = int(input("Enter the group of families: "))
    room_number_lst = list(map(int, input("Enter space separated room number: ").split()))
    freq = Counter(room_number_lst)
    print("This is freq :", freq, type(freq))
    print("This is freq.items()----", freq.items())
    for num, count in freq.items():
        if count == 1:
            print(num)
            break

captainRoom_2()