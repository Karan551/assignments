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

----- 

## 🌟🌟 List :-

- **`list` is a class.**
- **`list` is an iterable sequence.**
- **`list` is growable.**
- **`list` can store heterogeneous data.**
- **`list` elements are indexed.**
- ***List* is one fo the most commonly used sequences, and it is a most flexible type basically a list can contain any
  type (string, float, integer etc.) and number of items. It can hold one data type or a combination of several data
  types .**
- **A List is mutable(changeable) hence you can add, delete modify elements. We can build a list by assigning to it
  using the following syntax :-**
- **Syntax :-** 👇
  ```text
  lst_items = [ item1, item2, item3,.......]
  ```

**Example :-** 👇

```python
lst = [0, 5, 10, "Hello", "Python"]
```

### How to create list object :-

```python
# Square brackets are used to denote a list.
l1 = [10, 20, 30]

# Empty list object
l2 = []

# Heterogeneous elements
l3 = [50, 35, "abc", "Python", "JavaScript"]
```

### 🌟 How to access list elements :-

```python
l1 = [50, 20, 80, 30, 60, 40]
print(l1)
# <<< [50, 20, 80, 30, 60, 40]

print(l1[0])
# <<< 50

print(l1[1], l1[2])
# <<< 20 80

# Create a list of first 4 numbers
num_list = list(range(4))
print(num_list)
# <<< [0, 1, 2, 3]
```

- I have to insert Here image of list indexing

#### 🌟 Indexing :-

- **Just like strings we can access items on a list with the `index operator[]`.**
- **Always use an integer when indexing to avoid `TypeError`. Attempting to access a list element that is beyond the
  index range will result to and `IndexError.`**

##### 🌟 **Nested Indexing :-**

  ```python
lst_elements = [5, 6, 10, 15, "code", [1, 3, 5, 7, 9]]
print(lst_elements[5][1])
# <<< 3
print(lst_elements[4][0])
# <<< c
   ```

###### 🌟 **Negative Indexing :-**

- The last item on the list takes the -1 index the second to the last has the -2 index and so on.

```python
num_lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(num_lst[-1])  # same as it is ---> print(num_lst[len(num_lst)-1]) 
# <<< 80
print(num_lst[-2])  # same as it is ---> print(num_lst[len(num_lst)-2]) 
# <<< 70
```

##### 🌟 **Slicing of List :-**

- The slicing operator the `colon(:)` is used to access a range of elements on lists.

- **Example :-** 👇

```python
char_list = ["H", "e", "l", "l", "o", "W", "o", "r", "l", "d"]
print(char_list[0:5])
# ["H","e","l","l","o"]
```

#### 🌟 Accessing list elements via `for` loop :-

```python
num_lst = [10, 20, 30, 40, 50, 60, 70, 80]

for num in num_lst:
    print(num, end=" ")
```

##### 🌟 Accessing list elements via `while` loop :-

```python
num_lst = [10, 20, 30, 40, 50, 60, 70, 80]

i = 0
while i < len(num_lst):
    print(num_lst[i], end="")
    i += 1
```

##### 🌟 How to delete an element from the list:-

```python
num_lst = [10, 20, 30, 40, 50, 60, 70, 80]
del num_lst[4]
```

##### 🌟 How to edit an element of the list:-

```python
num_lst = [10, 20, 30, 40, 50, 60, 70, 80]
num_lst[4] = 100

# <<< [10, 20, 30, 40, 100, 60, 70, 80]
```

#### How to add more elements in the list :-

```python
num_lst = [10, 20, 30, 40, 50]
num_lst[6] = 60  # Index error

# not adding more values in the list but only updating values at index 3 & 1
num_lst[3] = 800
num_lst[1] = 600
```

- There are the following methods to add elements in the list:-

1. `append()`
2. `extend()`
3. `insert()`

- `class` is a group of variables and functions. These variables and functions are called attributes.

##### 🌟 Syntax :- 👇

```text
listObject.append(value)

listObject.extend(iterable)

listObject.insert(index,value)
```

- `append()` method adds value at the end of the list that is new element will become the last element of the list.
- `extend()` method extends the list by appending all the items from the iterable.
    - `extend()` method takes exactly one argument(maximum) and that argument should be iterable.
    - `extend()` method append(add) only iterable value not iterable type.
- `insert(index,value)` method insert an item at a given position.
    - if `index > last_index` then value will store at `last_index +1` means value will be appended.

#### 🌟 Example :- 👇

```python
num_lst = [10, 20, 30]

num_lst.append(40)
print(num_lst)
# <<< [10,20,30,40]

num_lst.insert(1, 200)
print(num_lst)
# <<< [10,200,30,40]

# if index > last_index then 
num_lst.insert(10, 10000)
print(num_lst)
# <<< [10,20,30,40,1000]

num_lst.extend([60, 70, 80, 90])
print(num_lst)
# <<<< [10,20,30,40,1000,60,70,80,90]

lst = [1, 3, 5]
lst.extend(range(6))

# this will give error because extend takes exactly one argument here two is given
# lst.extend([1,2,4,5],[7,8,9])  
```

#### 🌟 Packing And Unpacking :-

```python
a, b, c = 10, 20, 30
lst = [a, b, c]  # packing

num_lst = [40, 50, 60]
a, b, c = num_lst  # unpacking
```

- 🌟🌟 **When we unpack of any sequence then, number of variables on the left hand side must be same as the number of
  elements in the list.**
- 🌟🌟 **If we don't know how many elements are there in the `list/tuple/set` then we will have to assign at least one
  variable and after this variable we will have to use asterisk sign and name of the variable.**

```python
lst = [10, 20, 30, 40, 50, 60, 70]
a, *b = lst

print(a)
# <<< 10
print(b)  # type of b is list 
# <<< [20,30,40,50,60,70]
```

### 🌟 Built-in methods :-

1. `len()` 👉 Returns length of specified iterable.
2. `min()` 👉 Returns minimum value element.
3. `max()` 👉 Returns maximum value element.
4. `sum()` 👉 Returns sum of elements.
5. `sorted()` 👉 Returns sorted new list of elements (it's not change original list).

#### 🌟 `list()` method :-

- `list()` method takes at most(maximum) one argument that argument should be iterable.

```python
# create an empty list object.
lst = list()

# this will gives error because int object is not iterable.
# lst1=list(10)  

# this will gives error because list() method takes maximum one argument here 3 is given.
# lst2=list(10,20,30)

lst3 = list("Captain America")
# <<< ['C', 'a', 'p', 't', 'a', 'i', 'n', ' ', 'A', 'm', 'e', 'r', 'i', 'c', 'a']

lst4 = list(range(5))
# <<< [0, 1, 2, 3, 4]

lst5 = list([10, 20])
# <<< [10,20]
```

#### 🌟 Comparison Operator on `list` :-

```python
l1 = [1, 2, 3]
l2 = [2, 3, 1]
l3 = [1, 2, 3, 4, 5]
l4 = [1, 2, 3]
```

- If we compare two `list` then give the following results :-
- `l1 == l2` 👉 `False`
- `l1 == l3` 👉 `False`
- `l1 == l4` 👉 `True`
- `l1 > l4`  👉 `True`

#### 🌟 Concatenation Operator :-

```python
lst1 = [1, 5, 9]
lst2 = [2, 3, 1]

result = lst1 + lst2

print(result)
# <<< [1, 5, 9, 2, 3, 1]
```

#### 🌟 Repetition Operator :-

```python
l1 = [2, 5]
print(l1 * 5)
# <<< [2, 5, 2, 5, 2, 5]
```

#### 🌟 list of lists :-

```python
lst = [[1, 3, 5], [2, 1, 8], [5, 4, 4]]
```

#### 🌟 `list` object methods :-

<p align="center"> 🌟 <strong>Adding elements to a list :-</strong></p>

1. `append()` :- 👉 &nbsp; **It is used to add a single item at the end of the original list. It works with element data
   type not a value. It is change the original `list` object.**
    ```text
    list_object.append(object)
    ```
2. `extend()` :- 👉 &nbsp; **It is used to add two or more items at the end of the original list. It works only on
   element value not data type.**
    ```text
    list_object.extend(iterable)
    ```
3. `insert()` :- This method is used to insert an item on your desired location.
    ```text
    list_object.insert(index_number, value)
    ```

- **Example :-** 👇

```python
even_number = [2, 4, 6, 8]
even_number.append(10)
print(even_number)
# <<< [2, 4, 6, 8, 10]

num_list = [10, 20, 30, 40]
num_list.extend([101, 501, 511])
print(num_list)
# <<< [10, 20, 30, 40, 101, 501, 511]

odd_number = [1, 3, 5, 7, 9]
odd_number.insert(2, 55)
print(odd_number)
# <<< [1, 3, 55, 7, 9]
```

<p align="center"> 🌟 <strong>Removing or Deleting elements from a list :-</strong></p>

- There are four methods to remove items from the list :-

1. **`remove()` :-** 👉 **&nbsp; To remove an item from a list we can use remove method. It does not return anything.**
    ```text
    list_object.remove(value)
    ```

2. `pop()` :- 👉 **&nbsp; It is used to remove the item associated with the given index. If the index is not given By
   default It removes last element and returns that element. It is returned that value that is removed from the `list`.
   **
    ```text
    list_object.pop(index_value)
    ```
3. `clear()` :- **It is used to create an empty `list`.**
    ```text
    list_object.clear()
    ```
4. `del` **keyword :-** 👉 &nbsp; It is used to delete one or more items or event the entire list.
    - **To delete one item from the list is , Syntax is :-** <br />
      👉 &nbsp; `del list_object[index_value]`
    - **To delete range of item from the list is , Syntax is :-** <br />
      👉 &nbsp; `del list_object[:]`
    - **We can delete the entire items from the list by the replacing the entire range of items with an empty space.**
        - **Example :-** 👇

```python
numbers_list = [1, 2, 3, 4, 5, 6, 7]
numbers_list[:] = []
print(numbers_list)
# <<< []
``` 

#### 🌟 Example :-

```python
numbers_list = [1, 2, 3, 4, 5, 6, "Hello", 7]
numbers_list.remove("Hello")
print(numbers_list)
# <<< [1, 2, 3, 4, 5, 6, 7]

color_list = ["red", "yellow", "blue", "green", "pink", "brown", "white"]

# It removes the third index element from the list.
color_list.pop(3)

# It removes last item (By default).
color_list.pop()

color_list.clear()
print(color_list)
# <<< []
```

#### 🌟 Sorting Items on a `list` :-

- `sort()` **:-** 👉 &nbsp; **This method is used to sort items of similar data type with in the list. It sorts the items
  in ascending order (By default). It changes original `list`.**
- **Example :-** 👇

```python
number_list = [15, 13, 12, 16, 11, 14]
number_list.sort()
print(number_list)
# <<< [11, 12, 13, 14, 15, 16]
```

#### 🌟 Reverse method :-

- **This method is used to arrange items in the reverse or descending order. It changes original `list` also.**
- **Syntax :-** 👇

```text
list_object.sort(key=None, reverse=False)
```

- **Example :-** 👇

```python
number_list = [15, 13, 12, 16, 11, 14]
# sort in ascending order (By default)
number_list.reverse()
print(number_list)
# <<< [16, 15, 14, 13, 12, 11]

# sort in descending order
number_list.sort(reverse=True)
```

#### 🌟 `count()` method :-

- The `count()` method counts how many times an object occurs in a list.
    ```text
    list_object.count(object)
    ```

#### 🌟 `index()` method :-

- `index()` method returns of first occurrence of specifies element.

### 🌟 Some other important method of list :-

1. `copy()` :- 👉 &nbsp; **This method returns a shallow copy of the list.**
2.

#### 🌟 Testing For Membership in the `list` :-

- **Membership operators are used to test if an object is stored in a list. It returns True Oor False after evaluating
  the
  expression.**

```python
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(9 in numbers_list)
# <<< True

print(15 not in numbers_list)
## True
```

### 🌟 `list` Comprehension :-

- **`list` comprehension is a concise way of creating new list from an existing list. It consists of a expression and a
  `for` loop enclose in square brackets.**

**Syntax :-** 👇

```text
[expression for variable in iterable ]
```

```python
# Creating a list of 100 numbers using list comprehension :-
number_list = [number for number in range(1, 101)]

# for even number using filter
even_number_list = [number for number in range(1, 101) if number % 2 == 0]

# without list comprehension

lst = []
for num in range(1, 101):
    lst.append(num)
```

#### 🌟 `sorted(iterable, key=function_name, reverse=False)` :-

- **Returns a new list containing all items from the iterable in ascending order.**
- **A custom key function can be supplied to customize sort order.**
- **By default, it sorted in ascending order if we want to sort in descending order then we will have to
  set `reverse = True`**
- **By default `reverse = False`.**

-----

### 🌟 Mutability and Hashability :-

- **Mutable objects are changeable.**
- **immutable objects are not changeable.**
- **All immutable objects are hashable but not all hashable objects are immutable.**
- **Hashable is a feature of Python objects that tells if the object has a hash value or not if it has a hash value that
  does not change during its entire lifetime.**

| Data Type | Hashable | Mutable |
|:---------:|:--------:|:-------:|
|   `int`   |   Yes    |   No    |
|  `float`  |   Yes    |   No    |
| `complex` |   Yes    |   No    |
|  `bool`   |   Yes    |   No    |
|   `str`   |   Yes    |   No    |
|   `str`   |   Yes    |   No    |
|  `range`  |   Yes    |   No    |
|  `list`   |    No    |   Yes   |
|  `tuple`  |   Yes    |   No    |
|   `set`   |    No    |   Yes   |
|  `dict`   |    No    |   Yes   |

-----

<h2 align="center">Tuple</h2>

- `tuple` is a class.
- `tuple` is iterable.
- `tuple` is immutable.
- `tuple` is hashable.
- `tuple` is a sequence.
- A `tuple` is a sequence data type that contains ordered collectoin of objects. It is a immutable data type so once you
  have created we can not delete and update its elements.
- It is faster than list because we can delete or update its elements.

### 🌟 How To Create `tuple` object :-

- **To create a `tuple` we can place the elements with in parentheses and separate them with a comma.**
- We cannot create a tuple ony one element if we do this then we have to place a comma after the element.

```python
t1 = (10, 20, 30, 40)
t2 = ()  # empty value
# t3 = (10)  # It is not a tuple.
t4 = (10,)  # It is a tuple.
```

#### 🌟 Accessing `tuple` elements :-

##### Indexing :-

- The index operator indicates the index of the element that you want to access.

##### Slicing :-

- **If we want to access several items at the same time then we will have to use the slicing operator.**

- **We can access tuple elements using loop(while or for).**

- **Example :-** 👇

```python
tp = (10, 20, 30, 40, 50, 60)

# via indexing access tuple elements :-
print(tp[2])
# <<< 30

# via slicing access tuple elements 
print(tp[3:5])
# << (40, 50)

# ----------------------- using  while loop

count = 0
while count < len(tp):
    print(tp[count], end="")
    count += 1

# ----------------------- using  for loop
for item in tp:
    print(item, end="")
```

#### Concatenation and Repetition Operator :-

```python
tp1 = (10, 20, 30, 40, 50, 60)
tp2 = (11, 21, 31, 41)

print(tp1 + tp2)
# <<< (10, 20, 30, 40, 50, 60, 11, 21, 31, 41)

print(tp2 + tp1)
# <<< (11, 21, 31, 41, 10, 20, 30, 40, 50, 60)

print(tp2 * 3)
# <<< (11, 21, 31, 41, 11, 21, 31, 41, 11, 21, 31, 41)
```

#### Comparison Operator :-

```python
tp1 = (10, 20, 30, 40, 50, 60)
tp2 = (11, 21, 31, 41)

print(tp1 > tp2)
# False

print(tp2 < tp1)
# True

print(tp1 == tp2)
## <<< False
```

#### 🌟 Changing Reassigning and Deleting `tuple` elements :-

- **A `tuple` is immutable(unchangeable) data type so we cannot alter its elements.**
- **To reassign a `tuple` we an just list a different set of elements and assigning it to the `tuple`.**

- To delete a tuple and all the items you will use the keyword `del`.
- **Syntax :-** 👉   `del tuple_name`

### `tuple` object methods :-

- Only two python methods works with tuples.
    1. `count()`:- 👉 **&nbsp; It returns the number of elements which is equal to the given elements.**
        - **Syntax :-** 👉 `tuple_object.count(element)`
    2. `index()` :- 👉 **&nbsp; It returns the index of the first element which is equal to the given element.**
        - **Syntax :-** 👉 `tuple_object.index(element)`

```python
tp1 = (10, 20, 30, 10, 50, 20, 10, 20, 10, 20, 10)
print(tp1.count(20))
# <<< 4
print(tp1.index(30))
# <<< 2
```

### 🌟 User input :-

```python
user_input = input("enter numbers comma separated : ")

user_tuple = [number for number in user_input.split(",")]

# other way to create a tuple 
t2 = tuple()

t3 = tuple([10, 20, 30, 50, 40, 60, 90, 80, 70])
# <<< (10, 20, 30, 50, 40, 60, 90, 80, 70)

t4 = tuple(range(5))
# <<< (0, 1, 2, 3, 4)
```

### 🌟 built-in-methods :-

1. `len()`
2. `min()`
3. `max()`
4. `sum()`
5. `sorted()`

<h2 align="center"> 🌟 Set :- </h2>

- `set` is class.
- `set` is mutable.
- `set` is not hashable.
- `set` is not a sequence.
- `set` can not have duplicate values.
- `set` does not guarantee to store values in the order of insertion.
- Indexing is not applicable to set object.
- Slicing operator is not applicable.
- **A `set` is an ordered group of unique elements. Although a set itself is mutable its elements must be immutable.**
- A `set` is a collection unordered and unindexed that is iterable mutable and has no duplicate elements.

### 🌟 How to create a `set` object :-

- **We can create a `set` by enclosing all elements in curly braces or by using `set()` constructor.**
- **A `set` can hold items of different data type such as float, tuple string or integer.**
- **It cannot hold a mutable element such as a `dictionary`, `list` or `set`.**
- A comma is used to separate items from each other.

```python
s1 = {1, 5, 8}
s2 = {10, 2, 5, 14, 2, 8, 2, 8}

s3 = {}  # not a set object.

# To create a empty set object.
s4 = set()

```

- **To create an empty `set` we will have to use the `set()` function without an argument. We cannot use empty curly
  braces
  as this is the syntax for creating an empty dictionary.**

### 🌟 Accessing `set` elements :-

```python
# via for loop 

for e in setObject:
    print(e, end="")
```

#### 🌟 Concatenation and Repetition Operator :-

```text
# Concatenation operator
set + set ---> not supported    

# Repetition operator
set * int ---> not supported
```
#### 🌟 Comparison Operator :-
```text
s1 > s2
s1 < s2

s1 >= s2
s1 <= s2
s1 == s2
s1 != s2
```
- **Tow set objects are equal if their element are same doesn't matter the order of elements.**

#### 🌟 Changing elements in a `set` :-
- **Sets are mutable so we can change their elements. Because sets are unordered you cannot access or change an item or items through indexing or slicing.**

1. `add()` :- **This method is used to append a single element to a `set`.**
2. `update()` :- **This method is used to add multiple elements to a set. Strings, lists tuples or other set can be used as argument when we use `update()` method.**
   - **This method only element value not a data type.**

```python
my_set = {2, 4, 6, 8, 10}
my_set.add(12)
print(my_set)
# <<< {2, 4, 6, 8, 10, 12}

my_set.update([7, 9, 11, 13])
print(my_set)
# <<< {2, 4, 6, 7, 8, 9, 10, 11, 12, 13}
```

### 🌟 Removing `set` elements :-
- There are two methods to remove a specific item from a set.
1. `remove()` **:-** 👉 **&nbsp; This method is used to remove an item to a set. It `raise error` when the given argument does not exist.**
2. `discard()` **:-** 👉 **&nbsp; It is used to remove an item from a set. It does not raise error when the given argument does not exist. It simply remains unchanged to set.**
3. `pop()` **:-** 👉 **&nbsp;This method is used to remove and return and item on a set. Because set it unordered so we cannot possibly control which item will be popped.**
4. `clear()` **:-** 👉 **&nbsp;This method is used to remove all elements on a set.**

```python
# remove() method
my_set = {"a", "b", "c", "d", "e"}
my_set.remove("d")
print(my_set)
# <<< {'c', 'e', 'b', 'a'}

# discard() method 
my_set.discard("d")
{'c', 'b', 'a'}
print(my_set)

# pop() method
my_set.pop()
print(my_set)

# clear() method
my_set.clear()
print(my_set)
```