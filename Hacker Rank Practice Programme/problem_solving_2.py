import datetime

import numpy as np


def next_multiple_of_5(number):
    return number + (5 - number) % 5


def gradingStudents(grades):
    student_lst = []
    for grade in grades:
        if grade < 38:
            student_lst.append(grade)
            # return grade
        else:
            multiple_of_5 = next_multiple_of_5(grade)
            result = multiple_of_5 - grade

            if result < 3:
                student_lst.append(next_multiple_of_5(grade))
                # return next_multiple_of_5(grade)
            else:
                student_lst.append(grade)
                # return grade

        # return next_multiple_of_5(grade) if result < 3 else grade

    return student_lst


def student_info():
    number_of_students = int(input("how many number of students: ").strip())
    grades = []
    for _ in range(number_of_students):
        grade_item = int(input("enter grade: ").strip())
        grades.append(grade_item)

    result = gradingStudents(grades)
    result_2 = "\n".join(map(str, result))
    print('this is result:: \n', result_2)


# ------------------------------ Next Problem(Compare Two Triplets) ------------------------------

def compare_problem_input():
    a = list(map(int, input("Enter a space separated value: ").rstrip().split()))
    b = list(map(int, input("Enter a space separated value: ").rstrip().split()))

    if len(a) != len(b):
        raise ValueError("Please enter a same length elements")

    compare_triplets(a, b)


def compare_triplets(a: list, b: list):
    score_arr = [0, 0]

    for i in range(len(a)):
        if a[i] > b[i]:
            score_arr[0] += 1

        elif a[i] == b[i]:
            continue
        else:
            score_arr[1] += 1


# ------------------------------ Next Problem(Diagonal Difference) ------------------------------
def diagonal_problem_input():
    # user_input = int(input("enter a value that you want to insert: "))
    # # for i in range(user_input):
    # #     pass
    # lst = [list(map(int, input("Enter a space separated value: ").rstrip().split())) for _ in range(user_input)]
    # print("this is list::\n", lst)

    lst_2 = [[11, 2, 4],
             [4, 5, 6],
             [10, 8, -12]]

    arr = np.array(lst_2)
    print("\nthis is array::\n", arr)

    dig_1 = np.diagonal(arr)
    rotate_arr = np.rot90(arr)
    dig_2 = np.diagonal(rotate_arr)
    sum_1 = np.sum(dig_1)
    sum_2 = np.sum(dig_2)
    # print_tb()


# --------------------- this is second method(without numpy) ---------------------
def diagonal_problem_input_2(arr: list):
    main_diagonal_sum = 0
    rev_diagonal_sum = 0
    for i in range(len(arr)):
        main_diagonal_sum += arr[i][i]
        rev_diagonal_sum += arr[i][len(arr) - i - 1]

    print("Absolute value is:: ", abs(main_diagonal_sum - rev_diagonal_sum))


# ------------------------------ Next Problem(Time conversion) ------------------------------

# 07:05:45PM
def time_conversion_problem(s="07:05:45PM"):
    time_object = datetime.datetime.strptime(s, "%I:%M:%S%p")

    print("this is time object value::", time_object)
    time_value=time_object.strftime("%H:%M:%S")
    print("this is time object value::", time_value)
    pass


# s = int(s)
# if s


if __name__ == '__main__':
    # print(next_multiple_of_5(int(input("enter a value: "))))
    # student_info()
    # compare_problem_input()

    # diagonal_problem_input()
    # input("enter a value:: ")
    time_conversion_problem()
    pass
