from cmath import phase, polar
from itertools import count, product, permutations, combinations, combinations_with_replacement

# a = input("Enter a number :")
# b = input("Enter a number :")
# m = int(input("Enter a number :"))
# print(pow(9,29)+pow(7,27))
# complex_number = complex(input())
# print()
# print("This is complex number:", complex_number)
# print("this is imaginary number:", complex_number.imag)
# print("this is real number:", complex_number.real)
# print("this is conjugate number:", complex_number.conjugate())
# print("Distance:", (complex_number.imag ** 2 + complex_number.real ** 2) ** 1 / 2)
# print("angle", phase(complex(a, b)))
# print("R:", abs(complex(a, b)))
# print("List:", polar(complex(a, b)))
# print("List:", polar(complex_number))
# ----------------- Itertools Section-----
a = [1, 2]
b = [3, 4, 5]
print(list(((x, y) for x in a for y in b)))
print()


def itertoolsProduct():
    first_lst = list(map(int, input("Enter a space separated elements: ").split()))
    second_lst = list(map(int, input("Enter a space separated elements: ").split()))
    print(first_lst)
    print(second_lst)
    print(list(product(first_lst, second_lst)))


# Above generator method and below nested for loops are same
def nestedLoop():
    lst = []
    for x in a:
        for y in b:
            lst.append((x, y))
            print((x, y), end=' ')

    print()
    print(lst)


# lst=[]


# user_string, user_number = input("Enter a space separated elements: ").upper().split()
# user_string = sorted(user_string)
# user_number = int(user_number)
# print("this is user string: ", user_string)
# print("this is user number: ", user_number)

# result = combinations(user_string, user_number)


# print("This is my result:\n", sorted(result))
def combo(user_number):
    for i in range(1, user_number + 1):
        for j in combinations(user_string, i):
            print(''.join(j))


# combo()


# a = first_lst[1]
# print(a, type(a))
def permuted():
    result = permutations(sorted(first_lst[0]), int(first_lst[1]))
    for i in result:
        # print(i)
        a = ''.join(list(map(str, i)))
        # print(a)


# result = list(combinations(sorted(first_lst[0]), int(first_lst[1])))
# print('this is result:', result)

# first_lst = [*sorted(first_lst[0])]
# print(first_lst)
# lst = sorted()
# print(lst)
# lst = [i for i in s]
# a = ((i, j) for i in s for j in result)
# print(list(a))
# lst = []
# print(result)
# second_lst = [''.join(i) for i in result]
# first_lst.extend(second_lst)
# print("this is total list:", first_lst)
# total_lst_2=list(map(str,result))
# print("this is total list 2:\n",total_lst_2)
print()
# for j in result:
#     print(''.join(j))
# print(' '.join(result2))
# for i in result :
#     a = ''.join(list(map(str, i)))
#     print(a)
# print(list(product(lst,total_lst)))
# for i in range(1, user_number + 1):
#     for j in combinations(user_string, i):
#         print(''.join(j))

# result = combinations_with_replacement(user_string, user_number)
# print(list(result))

# for char in result:
#     print(''.join(char))


#

# if user_input:
#     num_result=eval(user_input)
#     if num_result is not None:
#         print(num_result)
# else:
#     print("This is empty")

# user_input = int(input("Enter a number:"))

# format(15,"x")
a = "15"
print(a.rjust(15))
# a.format()
number = 17
binary_number = format(number, 'b')


# print("Binary Number Is :", binary_number, "And length is :", len(binary_number))
# print(type(binary_number))


def print_formatted_number(number: int):
    # width = 5
    width = len(format(number, "b"))
    # width = str(width).rjust(width, " ")
    for num in range(1, number + 1):

        # print("Width is :", width)
        for base in "doXb":
            print("{0:{width}{base}}".format(num, base=base, width=width), end=' ')
        print()
    pass


print_formatted_number(int(input("Enter a number ")))
# for base in "doXb":
#     print(base, end=" ")
