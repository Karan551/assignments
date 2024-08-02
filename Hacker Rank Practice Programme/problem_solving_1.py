def plusMinusArr(arr):
    length_ar = len(arr)
    positive_number_lst = []
    negative_number_lst = []
    for i in arr:
        if i > 0:
            positive_number_lst.append(i)
        elif i < 0:
            negative_number_lst.append(i)

    rem = length_ar - (len(positive_number_lst) + len(negative_number_lst))

    print(len(positive_number_lst) / length_ar)
    print(format(len(positive_number_lst) / length_ar, ".6f"))
    print()
    print(len(negative_number_lst) / length_ar)
    print(format(len(negative_number_lst) / length_ar, ".6f"))
    print()
    print(rem / length_ar)
    print(format(rem / length_ar, ".6f"))


lst = [-4, 3, -9, 0, 4, 1]


# plusMinusArr(lst)

def minMaxSum(arr):
    min_lst = arr.copy()
    min_lst.remove(max(arr))
    max_lst = arr[::]
    max_lst.remove(min(arr))
    print(min_lst)
    print(max_lst)
    print(sum(min_lst), sum(max_lst))


lst_2 = [3, 2, 1, 3]
lst_3 = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]


def diagonalCase(arr):
    left_lst = []
    right_lst = []
    left = 0
    right = 0
    for i in range(len(arr)):
        for _ in arr[i]:
            if arr[left][right] not in left_lst:
                left_lst.append(arr[left][right])

            if arr[left][right] not in right_lst:
                right_lst.append(arr[left][right])

        left += 1
        right += 1
    print("THis is left list", left_lst)


diagonalCase(lst_3)


# minMaxSum(lst_2)

def stairCase(num: int):
    for i in range(1, num + 1):
        print(" " * (num - i), "#" * i)


# stairCase(4)


def camelCaseProblem():
    """
    Write a program to convert a given string into camelCase String.
    :return:
    """
    # words_number=int(input("Enter number of words: "))
    user_string = input("Enter words separated by space: ").split()
    camelLst = [i.title() for i in user_string]

    camelcaseString = camelLst[0].lower() + "".join(camelLst[1:])
    print(camelcaseString)


# function call
# camelCaseProblem()


def camelCaseProblem_2():
    user_string = "saveChangesInTheEditor"

    count = 1
    for letter in user_string:
        if letter.isupper():
            count += 1
    return count


# camelCaseProblem_2()


def camelCaseProblem_3():
    user_string = "saveChangesInTheEditor"
    count = 0
    for letter in user_string:
        if 65 <= ord(letter) <= 90:
            count += 1
    return count + 1


def charChecker(letter):
    if 65 <= ord(letter) <= 90:
        return True

# user_string = "saveChangesInTheEditor"
# result = map(charChecker, user_string)
# print('This is my result:', list(result).count(True))
