# DONE this task is done.


def fizz_buzz_problem(number):
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    elif number % 5 == 0 and number % 3 != 0:
        return "Buzz"

    elif number % 5 != 0 and number % 3 == 0:
        return "Fizz"
    elif number % 5 != 0 and number % 3 != 0:
        return number


if __name__ == '__main__':
    user_number = int(input("enter a number :"))
    print("result::", fizz_buzz_problem(user_number))
