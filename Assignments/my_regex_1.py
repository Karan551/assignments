import re

s = 'Python is very funny language.'

match = re.search(r'very', s)

# print('Start Index:', match.start())
# print('End Index:', match.end())

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

match2 = re.findall(r'\d+', string)
# print("this is result::", match2)

s = "python.django"
res = re.search(r".", s)
# print(res)
# print("this is res::", re.search(r"\.", s))

# print(res.span())

string = "The quick brown fox jumps over the lazy dog"
pattern = r"[a-m]"
res1 = re.findall(pattern, string)
# print(res1)

# ----
# Caret symbol
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']

# for string in strings:
#     if re.match(regex, string):
#         print(f'Matched: {string}')
#     else:
#         print(f'Not matched: {string}')

# -----
# print(re.search(r"ld$", "Hello world"))
# # $ symbol
# for string in strings:
#     if re.search(r"fox$", string):
#         print(f"matched: {string}")
#
#     else:
#         print(f"Not matched :{string}")

# ----
## + symbol
pattern = r"ag+"
lst = ["Hello Python", "It is a funny amazing language.", "Yeah ofcourse", "DjAngo", "bAA"]

string = "Hello World"

for string in lst:
    match3 = re.search(pattern, string, flags=re.IGNORECASE)
    if match3:
        print(f"Match found! {string}", match3)
    else:
        print(f"Match not found. {string}")
        print()
