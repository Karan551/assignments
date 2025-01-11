# Python Regex:-

- A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or set
  of strings.
- It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern
  into one or more sub-patterns.

### 🌟 Regex Module in Python :-

- Python has a built-in module named `re` that is used for regular expressions in Python.

### 🌟 How To Use Regex in Python :-

- We can use RegEx in Python after importing `re` module.

- 🌟 **Example :-**

```python
import re

s = 'Python is very funny language.'

match = re.search(r"very", s)

print('Start Index:', match.start())
print('End Index:', match.end())
# << Start Index: 10
# << End Index: 14
```

> Note :- **Here `r` character (r"very") stands for raw, not regex. The raw string is slightly different from a regular
string, it won’t interpret the \ character as an escape character. This is because the regular expression engine uses \
character for its own escaping purpose.**

## Regex Functions :-

1. `re.search(pattern, string, flags=0)` :- 👉 &nbsp; **`search()` function Searches for first occurrence of character or
   pattern.**
    - **Scan through string looking for the first location where the regular expression pattern produces a match, and
      return a corresponding Match. Return None if no position in the string matches the pattern.**

```python
#s
```

2. `re.findall()` :- 👉 &nbsp; **`findall()` matches all occurrences of a pattern, not just the first one as `search()`
   does.**
    - **Return all non-overlapping matches of pattern in string, as a list of strings or tuples. The string is scanned
      left-to-right, and matches are returned in the order found. Empty matches are included in the result.**

```python
import re

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
regex = r"\d+"

re.findall(regex, string)
# <<< ['123456789', '987654321']

```

### 🌟 Meta Characters :-

- Meta characters are characters with special meaning.

1. `\` Backslash :- **The backslash (\) makes sure that the character is not treated in a special way. This can be considered a way of escaping metacharacters.**

   - **For Example, If you want to search for the dot(`.`) in the string then you will find that dot(`.`) will be treated as a special character as is one of the metacharacters. So for this case, we will use the backslash(`\`) just before the dot(`.`) so that it will lose its specialty.** 
   - **The first search (`re.search(r'.', s)`) matches any character, not just the period, while the second search (`re.search(r'\.', s)`) specifically looks for and matches the period character.**
```python
import re

s = 'python.django'

# without using \
match = re.search(r'.', s)
print(match)
# <re.Match object; span=(0, 1), match='p'>

# using \
match = re.search(r'\.', s)
print(match)
#<<<   <re.Match object; span=(6, 7), match='.'>
```

2. `[]` **(Square Brackets) :-** 👉 &nbsp; Square Brackets (`[]`) represent a character class consisting of a set of characters that we wish to match. For example, the character class `[abc]` will match any single `a`, `b`, or `c`. 

We can also specify a range of characters using – inside the square brackets. For example, 
- `[0, 3]` is sample as `[0123]`
- `[a-c]` is same as `[abc]`

We can also invert the character class using the caret(^) symbol. For example, 
- `[^0-3]` means any character except `0`, `1`, `2`, or `3`
- `[^a-c]` means any character except `a`, `b`, or `c`

**Example :-** 👇
```python
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = r"[a-m]"
re.findall(pattern, string)
# <<< ['h', 'e', 'i', 'c', 'k', 'b', 'f', 'j', 'm', 'e', 'h', 'e', 'l', 'a', 'd', 'g']

```
3. `^` **(Caret) :-** 👉 &nbsp;  **Caret `(^)` symbol matches the beginning of the string i.e. checks whether the string starts with the given character(s) or not. For example –**  

- `^p` **will check if the string starts with g such as python, panda, pen etc.**
- `^pe` **will check if the string starts with ge such as pen, peacock,** 
```python
import re
regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
for string in strings:
    if re.match(regex, string):
        print(f'Matched: {string}')
    else:
        print(f'Not matched: {string}')
        
# <<< Matched: The quick brown fox
# <<< Matched: The lazy dog
# <<< Not matched: A quick brown fox
```

4. **`$` Dollar :-** 👉 **Dollar`($)` symbol matches the end of the string i.e checks whether the string ends with the given character(s) or not. For example-**

- `s$` will check for the string that ends with a such as `toys`, `boys`, `pens`, etc.
- `ks$` will check for the string that ends with ks such as `cheeks`, `leeks`, `ks`, etc.
```python
import re

string = "Hello World!"
pattern = r"World!$"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")
```

5.  `.` **Dot :-** 👉 **Dot`(.)` symbol matches only a single character except for the newline character (`\n`). For example –**  

- **`a.b` will check for the string that contains any character at the place of the dot such as `acb`, `acbd`, `abbb`, etc.**
- **`..` will check if the string contains at least 2 characters.**

- Example :- 👇
```python
import re

string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"

match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("Match not found.")
```
- This code uses a regular expression to search for the pattern `brown.fox` within the string. The dot (`.`) in the pattern represents any character. If a match is found, it prints `Match found!` otherwise, it prints `Match not found`.