import calendar



def zipBaseProblem():
    number_of_students, subjects = input("Enter number of students | subjects:").split()
    lst_of_marks = []
    subjects = int(subjects)
    for _ in range(subjects):
        marks_lst = list(map(float, input("enter marks space separated: ").split()))
        lst_of_marks.append(marks_lst)
    each_student_marks_list = list(zip(*lst_of_marks))
    total_marks_list = list(map(sum, each_student_marks_list))
    for marks in total_marks_list:
        print(marks / subjects)


# zipBaseProblem()

lst = [
    [89, 90, 78, 93, 80],
    [90, 91, 95, 93, 97],
    [78, 84, 74, 65, 98]
]


def anyOrAllProblem():
    numbers = input("How many number you want to check: ")
    number_list = list(map(int, input("enter a number space separated :").split()))

    def isPalindrome(number):
        return True if (str(number) == str(number)[::-1]) else False

    if int(numbers) == len(number_list):
        positive_number = list(map(lambda num: num > 0, number_list))
        if all(positive_number):
            isPalindrome_list = list(map(isPalindrome, number_list))
            return any(isPalindrome_list)
        else:
            return False


# anyOrAllProblem()
# print(list(reversed([1, 5, 10, 11])))


def calProblem():
    result = calendar.TextCalendar(1).formatyear(2024)
    print(result)


#
# print(calendar.isleap(2024))
# print(calendar.isleap(2022))
# calendarProblem()
# help("calendar")
# print(calendar.Month(11))

# Write a program to find the number of leap years in a given range.
#
# print(calendar.leapdays(2014, 2024 + 1))

# print(calendar.weekday(2024, 6, 9))
# print(calendar.TUESDAY)
# print(calendar.OCTOBER)
# print(calendar.monthcalendar(2024, 6))
# print(calendar.Calendar.monthdays2calendar(2024,))
# a=calendar.Calendar.monthdays2calendar(2024,2024,6)

a = calendar.HTMLCalendar()
print(a.formatday(9, 3))
# print(result)
