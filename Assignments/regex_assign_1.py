import string
import re
import email.utils


def valid_phone_number():
    pattern = r'^[789]\d{9}$'
    # ^: Asserts the start of the string.
    # [789]: Matches a single digit that is either 7, 8, or 9.
    # \d{9}: Matches exactly 9 digits (the remaining characters in the string).
    # $: Asserts the end of the string

    user_input = int(input("How many number you want to check : "))
    for _ in range(user_input):
        user_number = input("Enter your number : ")

        match = re.match(pattern, user_number)
        print("YES" if match else "NO")


def split_problem():
    user_string = "100,000,000.000"
    pattern = r"[,.]"
    # print(re.split(pattern, user_string))
    print("\n".join(re.split(pattern, user_string)))

    # for i in re.split(pattern, user_string):
    #     print(i)


#
# HERE: I have to solve this code
css_code = """
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}  
"""
code = """#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}"""

pattern3 = r"[{}:]"
# print('this is split ', code.strip().split(":"))
lst = []
#
pattern = r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})$"
pattern2 = r"^#([a-fA-F0-9]{6} | {a-fA-F0-9}{3})$"
pattern4 = r"^#([a-fA-F0-9]{3}){1,2}$"

new_pattern = r"^#([a-fA-F0-9]{3}|[a-fA-F0-9]{6})"
matches = re.match(pattern, code)


# print()

# print('this is result:', re.split(pattern3, code))
# print("response::", re.split(r"[:]+?", code))
# for char in re.split(r"[:]", code):
#     # print(char.strip("\n"))
#     char = char.strip(" ").strip("\n")
#     print('this is 🥰', char)
#
#     if re.search(pattern4, char):
#         print('new color:', char)
#     # print(re.findall(pattern, char))
#     # match = re.findall(pattern2, char)
#     # print('\n'.join(match))
#     # if match:
# print("*" * 10)
# print(re.findall(new_pattern, code))


def hex_color_code():
    pattern = r"^#([a-fA-F0-9{3}]|[a-fA-F0-9{6}])$"
    # hex color code length should be 3 or 6.
    # hex color code characters starts with # symbol.

    # code_lines = int(input("How many code lines you want to write: "))
    code_lines = 11
    for _ in range(code_lines):
        match = re.split(pattern, css_code)
        if match:
            print(f"Your hex color code  is correct \n{match}")
        else:
            print(f"Your hex color code is incorrect \n{match}")


a = "DEXTER <dexter@hotmail.com>"
b = "VIRUS <virus!@variable.:p>"
# print(email.utils.parseaddr("DOSHI <DOSHI@hackerrank.com>"))

# print('it is first email::', email.utils.parseaddr(a))
# print("it is second email:: ", email.utils.parseaddr(b))

email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))


def email_checker():
    email_pattern = r"^[a-zA-Z][\w-._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"

    user_choice = int(input("How many emails you input:: "))
    for _ in range(user_choice):
        user_input = input("Enter a name and email address: ")
        # name, my_email = user_input.split()
        response = email.utils.parseaddr(user_input)

        name, mail = response
        print(f"this is name {name} and this is mail::{mail}")

        if re.match(email_pattern, mail):
            r = (name, mail)
            print(email.utils.formataddr(r))

        # print(name, my_email)

    # [\w+@]
    pass


# print(re.VERBOSE)

# 🌟 done
def uuid_checker():
    id_pattern2 = r"(?!.*(.).*\1)(?=(.*[A-Z].*[A-Z])(?=(.*\d.*\d.*d).{10}$"
    pattern_3 = r"""
    (?=.*[A-Z]{2,})
    (?=.*\d{3,})
    (?=.*[a-zA-Z0-9])
    (?!.*(.).*\1+.*)
    .{10}$   
    """
    id_pattern = r"""
    (?=.*[A-Z].*[A-Z])
    (?=.*[0-9].*[0-9].*[0-9])
    (?=.*[a-zA-Z0-9]+)
    (?!.*(.).*\1.*)  
    
    .{10}
    """
    test_case = int(input("enter number of test cases: "))

    for _ in range(test_case):
        user_id = input("enter user id:: ")
        match = re.search(id_pattern, user_id, re.VERBOSE)
        # B1CD102354 , B1CDEF2354
        if match:
            print('Valid')
        else:
            print('Invalid')


def door_mat_pattern():
    door_length, door_width = map(int, input("Enter door length: ").split())

    if door_length % 2 == 0:
        return None

    # To print upper half design
    for i in range(1, door_length, 2):
        design = ".|." * i
        print(design.center(door_width, "-"))

    # To Print welcome msg
    print("WELCOME".center(door_width, "-"))

    # To print lower upper half design
    for i in range(door_length - 2, 0, -2):
        design = ".|." * i
        print(design.center(door_width, "-"))


# num = int(input("enter number value:: "))
# print(chr(num + 96))
# alphabet_letters = string.ascii_lowercase
# print('this is letters:: ', alphabet_letters)

# -.5
def check_float_number():
    float_pattern = r"^[+-]?(\d+(\.\d*)|\.\d+)$"
    while True:
        user_input = input("Enter a number:: ")
        match = re.search(float_pattern, user_input)

        if match:
            print(f"{user_input} is float number.", match)
        else:
            print(f"{user_input} is not a float number.", match)
        user_choice = input("Do you want to stop to check number.(y/n)").lower()
        if user_choice == 'n':
            break


def check_credit_card_number():
    card_pattern = r"^[456][^_ ]\d+{15}$"
    user_input = int(input("How many credit cards you want to check: "))
    for _ in range(user_input):
        pass
    pass


# print(".|.".center(21, "-"))
# print(".|.".center(21, "-"))
# print("WELCOME".center(21, "-"))
if __name__ == "__main__":
    # valid_phone_number()
    # split_problem()
    # hex_color_code()
    # email_checker()
    # uuid_checker()
    # door_mat_pattern()
    check_float_number()
    pass
