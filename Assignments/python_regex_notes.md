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
    - `re.search()` checks for a match anywhere in the string.

```python
# s
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

3. `re.match(pattern, string, flags=0)` :- **`re.match()` checks for a match only at the beginning of the string.**
    - If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding
      Match. Return `None` if the string does not match the pattern. *Note* that this is different from a zero-length
      match.
    - **Note:- that even in MULTILINE mode, `re.match()` will only match at the beginning of the string and not at the
      beginning of each line.**

    - **If you want to locate a match anywhere in string, use search() not match().**
    - `re.fullmatch()` checks for entire string to be a match.

### 🌟 Meta Characters :-

- Meta characters are characters with special meaning.

1. `\` Backslash :- **The backslash (\) makes sure that the character is not treated in a special way. This can be
   considered a way of escaping metacharacters.**

    - **For Example, If you want to search for the dot(`.`) in the string then you will find that dot(`.`) will be
      treated as a special character as is one of the metacharacters. So for this case, we will use the backslash(`\`)
      just before the dot(`.`) so that it will lose its specialty.**
    - **The first search (`re.search(r'.', s)`) matches any character, not just the period, while the second
      search (`re.search(r'\.', s)`) specifically looks for and matches the period character.**

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
# <<<   <re.Match object; span=(6, 7), match='.'>
```

2. `[]` **(Square Brackets) :-** 👉 &nbsp; Square Brackets (`[]`) represent a character class consisting of a set of
   characters that we wish to match. For example, the character class `[abc]` will match any single `a`, `b`, or `c`.

We can also specify a range of characters using – inside the square brackets. For example,

- `[0, 3]` is sample as `[0123]`
- `[a-c]` is same as `[abc]`

We can also invert the character class using the caret(^) symbol. For example,

- `[^0-3]` means any character except `0`, `1`, `2`, or `3`
- `[^a-c]` means any character except `a`, `b`, or `c`

- `[]`Used to indicate a set of characters. In a set
    - **Characters can be listed individually, e.g. `[amk]` will match `a`, `m`, or `k`**
    - **Ranges of characters can be indicated by giving two characters and separating them by a '-', for example `[a-z]`
      will match any lowercase ASCII letter, `[0-5][0-9]` will match all the two-digits numbers from `00` to `59`,
      and `[0-9A-Fa-f]` will match any hexadecimal digit. If `-` is escaped (e.g. [`a\-z]`) or if it’s placed as the
      first or last character (e.g. `[-a]` or `[a-]`), it will match a literal '`-`'.**

    - **Special characters lose their special meaning inside sets. For example, `[(+*)]` will match any of the literal
      characters `'(', '+', '*', or ')'`.**

    - **Characters that are not within a range can be matched by complementing the set. If the first character of the
      set is `^`, all the characters that are not in the set will be matched. For example, `[^5]` will match any
      character except `5`, and `[^^]` will match any character except `^`. `^` has no special meaning if it’s not the
      first character in the set.**

    - **To match a literal `]` inside a set, precede it with a `backslash (\)`, or place it at the beginning of the set.
      For example, both `[()[\]{}]` and `[]()[{}]` will match a right bracket, as well as left bracket, braces, and
      parentheses.**
- **Example :-** 👇

```python
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = r"[a-m]"
re.findall(pattern, string)
# <<< ['h', 'e', 'i', 'c', 'k', 'b', 'f', 'j', 'm', 'e', 'h', 'e', 'l', 'a', 'd', 'g']

```

3. `^` **(Caret) :-** 👉 &nbsp;  **Caret `(^)` symbol matches the beginning of the string i.e. checks whether the string
   starts with the given character(s) or not. For example –**

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

4. **`$` Dollar :-** 👉 **Dollar`($)` symbol matches the end of the string i.e checks whether the string ends with the
   given character(s) or not. For example-**

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

5. `.` **Dot :-** 👉 **Dot`(.)` symbol matches only a single character except for the newline character (`\n`). For
   example –**

- **`a.b` will check for the string that contains any character at the place of the dot such as `acb`, `acbd`, `abbb`,
  etc.**
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

- This code uses a regular expression to search for the pattern `brown.fox` within the string. The dot (`.`) in the
  pattern represents any character. If a match is found, it prints `Match found!` otherwise, it prints
  `Match not found`.

6. `{m}` :- 👉 **Specifies that exactly `m` copies of the previous RE should be matched; fewer matches cause the entire
   RE not to match. For example, `a{6}` will match exactly six `a` characters, but not five.**
7. `+` :- 👉 **Plus (`+`) symbol matches one or more occurrences of the regex preceding the + symbol.**
    - Example :-👇
      - **Pattern** `a+`
      - **This will match a string that contains one or more consecutive 'a' characters (e.g., "a", "aa", "aaa").**
      - **Example match: "aa", "aaa" (but not "b", "ab").**
    - `\d+` :👇
        - `\d` :- **This represents a digit, equivalent to `[0-9]`. It matches any single digit from 0 to 9.**
        - `+` :- **This is a quantifier that means one or more of the preceding(before) element (in this case, a digit).
          **
        - `\d+` matches one or more digits in a sequence.

    - `\w+` :👇
        - `\w` :- **This represents a word character, equivalent to `[a-zA-Z0-9_]`. It matches any letter (uppercase or
          lowercase), digit, or underscore.**
        - `+` :- **As before, this is a quantifier that means one or more of the preceding element (in this case, a word
          character).**
        - **`w+` matches one or more word characters.**