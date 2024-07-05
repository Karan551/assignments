# OOPS in Python: -

## What is class: -

- In Python, everything is an object. To create an object, we required some Model or BluePrint that is nothing but
  **class.**
- We create a class to represent properties(attributes) and methods(actions) of an object.
- Properties can be represented by variables.
- Actions can be represented by Methods.
- So a **class** contains both **variables** and **methods**.

### How To Create a class:-

- We create a class by using **class** keyword.

#### Syntax :-

```text

class className:
    """documentation string"""
    variables: instance variables, class variables (static variables ), local variables
    methods: instance methods, class methods, static methods
    
```

- Documentation string represents description of the class. Within class docstring is always optional. There are two
  methods to get docstring of the class:-

```python

print(className.__doc__)
print(help(className))

```

- For Example: -

```python

class Student:
    """This is a Student class with required data."""
    print(Student.__doc__)
    print(help(Student))

```

- Within Python, class we can represent data using variables.
- There are three types of variables are allowed in Python class:-

1. Instance Variable (Object Level Variable)
2. Class Variable (Static Variable)
3. Local Variable (Method Level Variable)

- With in Python `class`, we represent **operations** using **methods (function)**. The following type of methods is
  allowed in Python
  class: -

1. Instance Methods
2. Class Methods
3. Statice Methods

```python
class Student:
    """Developed By Master For Demo"""

    def __init__(self):
        # instance variables
        self.name = "Master"
        self.age = 20
        self.marks = 90

    # instance method
    def talk(self):
        print("Hello I am:", self.name)
        print("My age is:", self.age)
        print("My marks are:", self.marks)


```

-----

## What is Object: -

- **Physical existence** of a **class** is nothing but an object. We can create **any number of objects** for a **class
  **.
- **Syntax: -** 👇<br> To create an object:
  — **referenceVariable = className()**
- **Example** 👉   **s = Student()**

-----

## What is reference variable: -

- The **variable** which can be used to **refer an object** is called **reference variable.** By using **reference
  variable**, we can
  **access properties and methods of an object**.

### self variable :-

- `self` is the **default variable** which is always pointing to a **current object.**
- By using `self` we can access **instance variables** and **instance methods** of an object.

>  [!Note] <br>
>  - `self` should be the first parameter inside constructor.<br>
  <pre>
    def __init__(self):
      pass
  </pre>
> - `self` should be the first parameter inside instance methods.

<pre>
  def talk(self):
    pass
</pre>
-----
## `__init__()` method [Constructor method ] :-

- `__init__()` is a special method in a Python.
- `__init__()` method is executed automatically at the time of object creation.
- The main purpose of `__init__()` method is to **declare and initialize instance variables**.
- Per object `__init__()` method is executed only once.
- `__init__()` method can take at least one argument that is `self` variable.
- `__init__()` method is optional and if we are not providing any `__init__()` method then **python** will provide
  **default constructor**.
------
## Difference Between Methods and Constructor: -

| Method                                                      | Constructor                                                                            |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 1.) Name of method can be any name.                         | 1.) Constructor name should be always `__init__()`                                     | 
| 2.) Per Object, method can be executed any number of times. | 2.) Per Object, **constructor** will be executed **only once**.                        |
| 3.) **Method** will be executed if **we call that method.** | 3.) **Constructor** will be **executed automatically** at the time of object creation. |
| 4.) Inside **method** we can write **business logic.**      | 4.) Inside **constructor** we have to **declare and initialize instance variables.**   |

------------------

## Types of Variables: -

1. **Instance Variable (Object Level Variable)**
2. **Class Variable (Static Variable)**
3. **Local Variable (Method Level Variable)**

<h2 align="center"> 1. Instance Variable (Object Level Variable): -</h2>
