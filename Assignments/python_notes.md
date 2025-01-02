# Python :-

- Python is a high level general purpose programming language. It's design philosophy emphasizes code readability with
  the use of significant indentation.
- **Python is dynamically type-checked and garbage-collected.** It supports multiple programming paradigms, including
  structured (particularly procedural), **object-oriented** and **functional programming**. It is often described as a
  **"batteries included"** language due to its comprehensive standard library.

## History Of Python :-

- Python was conceived in the late 1980s by **[Guido Van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)** at
  **Centrum Wiskunde & Informatica** in the Netherlands as a successor of the **ABC Language**.
- He has been in variably worked as the lead developer until 12 July 2018.
- In January 2019 active Python core developer elected a five member council to lead the Project.

## Version History Of Python :-

1. _Python &emsp; 1.0 &emsp; 1994_
2. _Python &emsp; 2.0 &emsp; 2000_
3. _Python &emsp; 3.0 &emsp; 2008_

### Latest Version :-

Python &emsp; 3.13 &emsp; 7 October 2024

-----

### 🌟 Name Python :-

- Python developers aim for it to be fun to use.
- The Name **Python** is a tribute to the **British Comedy Group Monty Python.**

### Features Of Python :-

1. Simple And Straight Forward Language
2. Case Sensitive
3. Multi-paradigm programming language
4. Dynamically typed language
5. Emphasis on code readability
6. Automatic memory management
7. Large Library Support
8. Huge Community
9. Platform Independent

### Amazing Facts :-

- Ranked #1 (TIOBE Programing Community)
- Highest Rise in ratings in a year.(2007,2010,2018 and 2020)
- Python reduce app development.
- Large organizations that uses Python are **Google, NASA, Facebook, Amazon, Instagram, Spotify, Microsoft, CERN,
  YouTube, Netflix, Dropbox** etc.

### Variety of Use :-

- Python can serve as a scripting language for web applications.
- Web Frameworks - Django, Flask etc.
- Pyjs and Iron Python can be used to develop the client side of Ajax based applications.
- Twisted is a framework to program communications between computers and is used by dropbox.
- Libraries like numpy, Scipy Matplotlib are used in Scientific Computations.
    - You can develop variety of applications using Python.

    1. Console Application
    2. Web Application
    3. Desktop Application
    4. Mobile Application
    5. IOT Application
    6. AI based Applications
    7. Many more

  #### Major Use :-

    1. Website Development
    2. Task Automation
    3. Data Analysis
    4. Data Visualizations

------

### 🌟 Variable :-

- Variable are used to hold data during execution of the programme.
- In C , C++ you need to declare variables only after declaration you can use them.
- Example :-
  ```text
  int a;
  float b;
  ```
- In Python, you do not declare variable. If there is a need of a variable you think of a name nd start using it is a
  variable.

#### 🌟 Variable Name :-

- **Variable name is any combination of alphabet,digit and underscore.**
- **Variable name can not start with digit.**
- **Variable name are case-sensitive.**
- **Keywords can not be uses as variable names.**
- **Variable can be deleted also using** `del` **keyword.**

#### 🌟 Dynamic Type :-

- Not only the value of a variable may change during programme execution but type as well.
    - For example :- 👇

      ```python
      marks = 5                   # type of x is int.
      salary = 50000.725          # type of x is float.
      isNumber = True             # type of x is bool.
      user_name = "Iron Man"      # type of x is str.
      ```
- All Data types are class in Python.

#### 🌟 Data Types :-

1. Numbers :-
   --- Here display table
2. Boolean
3. String

- `double` is no there in Python.
- `char`  is not there in Python.
- _----- Here show picture.

#### 🌟 Name kiska hota hai:-

- Name in namespace is a variable which is used to contain id(reference) of
    1. Instance object
    2. Function object
    3. Class object

    - 🌟  **&nbsp; In Python everything is object.**

### 🌟 What is an object :-

- Object is something which can store data and has methods(function) to handle data.
- **e.g. :-** 👇
  ```python
  a, b, c = 5, 6, 7
  print(a, b, c, sep="-", end="$")
  print("Hello")
  # <<< 5-6-7$Hello
  ```

-----

### Data :-

- Data is any piece of information which is used by the programme to accomplish(complete) a task.
- **e.g. :-** 👇

    1. Find sum of two numbers.
    2. check whether a given number is even or odd.
    3. Find LCM of two numbers.

- All the above tasks can be done only using some data.

#### 🌟 Variety of Data :-

1. Integers
2. Real (Float)
3. Strings

#### 🌟 Garbage Collection :-

- It is a programme invoked(called) by Python itself whenever required whose job is to release memory of Garbage
  blocks.(Object which is not referenced by any name/variable.)

#### 🌟 What is an Object :-

- Object is real entity.
- Object is an instance of a class.
- Object is a proper noun.
- Class is a common noun.
- **Example :-** 👇

    - Doctor ----> Common Noun (class)
    - Dr. Mak ----> Proper Noun (object)
    - Dr. Alok ----> Proper Noun (object)

#### 🌟 `print()` function :-

**Syntax :-** 👇

```python
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

- print simple text ---->  `print("Welcome")`
- print variable ----> `print(x)`
- print expression ----> `print(x + 5*3)`
- print multiple value ----> `print(x , y)`

-----

### 🌟 Module Package & Library :-

- **Module :-** 👉 &nbsp; **It is a Python file. It can contain instance objects , function objects and class objects. In
  Simple words it contains variables functions and classes.**
    - **`.py` file is known as Module.**
- **Package :-** 👉 &nbsp; **Package is a collection of module and sub-packages.**
- **Library :-** 👉 &nbsp; **Library is a collection of packages.**

-----

### 🌟 `import` :-

  ```text
  import moduleName
  
  moduleName.moduleElement
  ```

- **Module element can be :- 👇**
    - `variable`
    - `function`
    - `class`
- If we want to import specific object form any module then we will write
  ```python
  from A2 import  x
  ```
- Where :-
    - A2 👉 **Module Name**
    - x 👉  **module element**

### 🌟 Keywords :-

- Predefined words
- Reserved words
- There are 35 keywords in `Python` .

|        |          |           |        |
|:------:|:--------:|:---------:|:------:|
| False  |  class   |   from    |   or   |
|  True  | continue |  global   |  pass  |
|  None  |   def    |    if     | raise  |
|  and   |   del    |  import   | return |
|   as   |   elif   |    in     |  try   |
| assert |   else   |    is     | while  |
| async  |  except  |  lambda   |  with  |
| await  | finally  | non local | yield  |
| break  |   for    |    not    |        |

### 🌟 Type conversion functions :-

1. `int()`
2. `float()`
3. `complex()`
4. `bool()`
5. `str()`

### 🌟 Number System :-

1. **Binary Number System :-** 👉 **&nbsp;0 , 1**
2. **Octal Number System :-** 👉 **&nbsp;0 , 1, 2, 3, 4, 5, 6, 7**
3. **Decimal Number System :-** 👉 **&nbsp;0 , 1, 2, 3, 4, 5, 6, 7, 8, 9,**
4. **Hexa Decimal Number System :-** 👉 **&nbsp;0 , 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F**

### 🌟 Number Conversion :-

```python
x = 25
bin(x)
# <<<< '0b11001'
oct(x)
# <<<< '0o31'
hex(x)
# <<<< '0x19'

#  x = 0b11001 (in binary)
#  x = 0o31    (in octal)
#  x = 0x19    (in hexadecimal)
```

### 🌟 Unicode :-

- **The Unicode is character encoding and its goal is to replace like existing character sets with its standard UTF.**

    - UTF 👉 **&nbsp; Unicode Transformation Format**
    - UTF-8 👉 **&nbsp; It is the most commonly used character encoding. It is also backward compatible with ASCII.**

### 🌟 Character To Unicode :-

```python
x = "A"
ord(x)
# <<<< 65
```

### 🌟 Unicode To Character  :-

```python
x = 65
chr(x)
# <<<< 'A'
```

### 🌟 Taking input from the User `input()`:-

- `input()` can take at most one argument of `str` type.
- `input()` always return `str` type value.

-----
### 🌟 Operators :-