import math
import string
import time
from time import gmtime, localtime, strftime
import datetime
from itertools import groupby, combinations


# from datetime import datetime


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


# queries = int(input("Enter queries:: "))
# for _ in range(queries):
#     stream_name, n = input("enter stream and value separated by space: ").split()
#     n = int(n)
#     if stream_name == "even":
#         print_from_stream(n)
#     else:
#         print_from_stream(n, OddStream())

# -------------------------------------


# 🥰 DONE
def print_rangoli_2(size):
    # user_input = int(input("enter a number: "))
    alphabet = string.ascii_lowercase
    rows = []

    width = 2 * size - 1
    for i in range(size - 1, -1, -1):
        right_part = "-".join(alphabet[i:size]).ljust(width, "-")
        left_part = "".join(reversed(right_part))[:-1]
        full_row = left_part + right_part

        rows.append(full_row)

    print("\n".join(rows))

    print("\n".join(rows[-2::-1]))


def iterable_iterator_problem():
    length_of_list = int(input("Enter the length of the list:: "))
    letter = input("enter space separated list: ").split()
    if len(letter) != length_of_list:
        raise ValueError("please insert correct length.")

    indices = int(input("enter indices: "))

    all_combinations = list(combinations(letter, indices))

    count_a = 0
    for i in all_combinations:
        if "a" in i:
            # print(i)
            count_a += 1
        # print(i, end=" ")

    # print("this is string length::", len(all_combinations))

    print(f'{count_a / len(all_combinations):.4f}')

    # valid_combinations = [i for i in all_combinations if "a" in i]
    # all_combinations=
    # print("this is valid combination::", valid_combinations)
    # print("this is valid combination::", list(all_combinations))


# print('this is gmtime value::', gmtime())
# print(strftime("%a %A, %d %b %Y %H:%M:%S +0000", gmtime()))


# user_input = int(input("ente a value:: "))
# print(type((user_input,)))
# value = (user_input,)
# value_1 = "Sun 10 May 2015 13:54:36 -0700"
# value_2 = "Sun 10 May 2015 13:54:36 -0000"
# date_format = "%a %d %b %Y %H:%M:%S %z"
# print("\nthis is local time value::", localtime())

# print(strftime("%b", user_input))

# d1 = datetime.datetime.strptime(f"{value_1}", date_format)

# d2 = time.strptime(f"{value_2}", date_format)
# d2 = datetime.datetime.strptime(f"{value_2}", date_format)


# print("\nthis is strptime value::", time.strptime(f"{value}", date_format))
# print("this is d1::", d1)
# print("this is d2::", d2)
# print("this is the difference of \n", (d1 - d2).total_seconds())


def time_delta(t1=None, t2=None):
    start_date = datetime.datetime.strptime(t1, date_format)
    end_date = datetime.datetime.strptime(t2, date_format)

    result = int(abs((start_date - end_date).total_seconds()))
    print("this is result::", result)


def fizzBuzz(n):
    # Write your code here
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    else:
        print(n)


# 🥰
def compress_string_problem():
    for key, value in groupby("1222311"):
        print((len(list(value)), int(key)), end="")


if __name__ == "__main__":
    # print_rangoli_2(5)
    # time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000")
    # fizzBuzz(int(input("enter a number: ")))
    # compress_string_problem()
    iterable_iterator_problem()
    pass
