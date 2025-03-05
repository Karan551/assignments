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

> [!Note] <br>
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


------

# Encapsulation :-

- **Encapsulation is the idea of hiding the internal details of an object and exposing only the necessary information to
  the outside world.**
- This allows the class to be used in a predictable and consistent manner, even if the underlying implementation
  changes. **By using private and protected fields, developers can control the visibility and accessibility of class
  attributes and methods, preventing accidental or intentional misuse.**

### Private Attribute In Python Class :-

- **Private attributes are denoted by a double underscore prefix before the attribute name** (e.g. `__private_attribute)
  `.
- **The idea behind private attributes is that they can only be accessed within the class and should not be accessed
  from outside the class.** However, it is important to note that the **double underscore syntax is just a convention**
  **and not a strict rule.**

- **When an attribute with a double underscore prefix is referenced from outside the class, the attribute name is
  automatically mangled(destroy) to prevent accidental access.**

- For Example:-

```python
class Person:
    def __init__(self, name, age, ):
        self.name = name
        # private attribute
        self.__age = age

    # method to get the value of private attribute
    def get_age(self):
        return self.__age


# create an object of Person class
person1 = Person("mahesh", 14)
print("Person name is :", person1.name)

print("Person age is :", person1.age)  ## This will give error
```

- When trying to access the **private attribute directly from outside the class**, an `AttributeError` **is raised,
  indicating that the attribute is not accessible.** This protects the **private attribute from being accidentally or
  intentionally modified from outside the class, maintaining the integrity of the class.**

### Protected Attribute in Python class :-

- **Protected attributes in Python are denoted by a single underscore prefix before the attribute name.**
- Protected attribute is similar to the Private attribute, but they will not be access directly from outside of the
  class. **But they will be access in subclasses or child classes.**
- **Private attribute will not access in subclasses or child class But Protected attribute will be access in child
  class or subclass.**

- For example :-

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        # This is Protected attribute
        self._age = age


class Employee(Person):
    # To get value of protected variable.
    def get_age(self):
        return self._age
```

### Private Methods in class :-

- **Just like private attributes, private methods in Python are denoted by a double underscore prefix before the
  method name (e.g. `__private_method`). Private methods are meant to be used only within the class and should not be
  accessed from outside the class.**

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        # This is Protected attribute
        self._age = age

    # This is private method.
    def __showInfo(self):
        return f"User name is {self.name} and age is {self._age}"

```

- **Just like private attributes, attempting to access private methods from outside the class results in an**
  `AttributeError`.

### Protected Method is class :-

- **Protected methods in Python are denoted by a single underscore prefix before the method name (e.g.
  `_protected_method`). Protected methods are meant to be used within the class and within subclasses, but not from
  outside the class.**

```python
class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.__age = age
        self._contact = contact

    # This is protected method.
    def _getAge(self):
        return self.__age

```

------

### 🌟 Operator Overloading :-

- **Operator overloading is a feature in object-oriented programming that allows you to define new behavior for existing
  operators in a class.**
- It allows you to customize the way operators work for objects of that class, rather than using the default behavior
  provided by Python's built-in operators.
- This is useful when you want to provide a more specific or customized behavior for a specific type of object.
- **Operator overloading in Python allows you to define how operators (like `+`, `-`, `*`, etc.) behave when applied to
  instances of custom classes. This means that you can specify how operators work with objects of your own classes,
  enabling you to use operators on those objects just like you would with built-in types (like integers or strings).**
- **To implement operator overloading in Python, you define special methods in your class, known as "magic methods" or "
  dunder methods." These methods start and end with double underscores (__), and each operator corresponds to a specific
  magic method.**

- Common Operator Overloading Methods:

    - Here are some examples of magic methods for common operators:
    - `__add__(self, other)` : 👉 Defines behavior for the `+` operator.
    - `__sub__(self, other)` : 👉 Defines behavior for the `-` operator.
    - `__mul__(self, other)` : 👉 Defines behavior for the `*` operator.
    - `__truediv__(self, other)` : 👉 Defines behavior for the `/` operator.
    - `__eq__(self, other)` : 👉 Defines behavior for the `==` operator.
    - `__lt__(self, other)` : 👉 Defines behavior for the `<` operator.

1. `+` (Addition) :-

- **Method :-** 👉 `__add__(self, other)`
- **This method is called when you use the `+` operator between two objects of the class.**
- **Example :-** 👇

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Calls p1.__add__(p2)
print(p3.x, p3.y)  # Output: 4 6
```

2. `-` (Subtraction)

- **Method :-** 👉 `__sub__(self, other)`
- **This method is called when you use the - operator between two objects.**
- **Example :-** 👇

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


p1 = Point(5, 7)
p2 = Point(3, 4)
p3 = p1 - p2  # Calls p1.__sub__(p2)
print(p3.x, p3.y)  # Output: 2 3
```

3. `*` **(Multiplication) :-**
    - **Method :-** 👉 `__mul__(self, other)`
    - This method is called when you use the `*` operator.
    - **Example :-** 👇

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)


p = Point(2, 3)
p2 = p * 3  # Calls p.__mul__(3)
print(p2.x, p2.y)  # Output: 6 9
```

4. `==` (Equality) :-

- **Method :-** `__eq__(self, other)`
- This method is called when you use the `==` operator to compare two objects.
- **Example :-** 👇

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False

```

5. `<`(Less Than)
    - **Method:-** 👉 `__lt__(self, other)`
    - **This method is called when you use the `<` operator.**
    - Example :- 👇

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 < p2)  # Output: True
```

#### 🌟 Benefits of Operator Overloading :-

- **Readability :-** 👉 **It makes your code more intuitive and natural, especially when using mathematical or
  collection-related operations.**
- **Flexibility :-** 👉 **You can define custom behaviors for operators, tailoring them to the needs of your class.**
- **Encapsulation :-** 👉 **Operator overloading helps keep your class’s internal workings hidden while exposing an
  easy-to-use interface.**

------

### 🌟 Inheritance :-

- **The transfer of the characteristics of a class to other class that derived from it is known as Inheritance.**
- **It is a programming structure that allows a new class to inherit the attributes of an existing class. The new class is
  called the child class, subclass or derived class while the class it inherits from is the parent class , superclass or
  base class.**
- **Inheritance is a important feature because it promotes code reusability and efficiency.**
- **Syntax :-** 👇

```python
class ChildClass(ParentClass):
    pass
```
- In Python there are 3 types of inheritance :-
1. **Single Inheritance**
2. **Multiple Inheritance**
3. **Multilevel Inheritance**

- **Example :-** 👇

```python
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name + " " + self.last_name)


class Student(Person):
    pass


# creating an object
ganesh = Student("ganesh", "mishra")
ganesh.print_name()
```
- If we want to add `__init__()` function to the child class (instead of the `pass` keyword ).And we know that `__init__()` function is called automatically every time the class is being used to create a new object.

```python
class Student(Person):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
```

- Whe we add the `__init__()` function the child class will no longer inherit the parent `__init__()` function Because the child's `__init__()` function overwrite the inheritance of the parent's `__init__()` function.
- To keep the inheritance of the parent's `__init__()` function add a call to the parents `__init__()` function.

- **Example :-** 👇
```python
class Student(Person):
  def __init__(self, first_name, last_name):
    # call parent init function.
    Person.__init__(self, first_name, last_name)
```

#### 🌟 Use the `super()` function :-
- **Python also has a `super()` function that will make the child class inherit all the methods and properties from parent.**
- **By using the `super()` function we don't have to use the name of the parent element, it will automatically inherit methods and properties from its parent.**

- **Example :-**
```python
class Student(Person):
    def __init__(self,first_name,last_name):
      super().__init__(first_name,last_name)
```

### 🌟 Add Properties And Methods :-
- **Add a Property called graduation year to the student class.**

- Example :- 👇
```python
class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)

        # add property
        self.year = year
    
    # add method
    def welcome_message(self):
        print(f"Welcome {self.first_name} {self.last_name}")


# creating an object
mahesh = Student("Mahesh", "Babu", 2025)
```
- **If we add a method in the child class with the same name as function in the parent class the inheritance of the parent method wil be overridden.**

### 🌟 Multiple Inheritance :-
- In a multiple inheritance a class inherit multiple classes.

```python
class A:
    def displayA(self):
        print("Welcome to the India Mr. A.")


class B:
    def displayB(self):
        print("Welcome to the India Mr. B.")


class C(A, B):
    def displayC(self):
        print("Welcome To India Mr. C")


# create an object
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
```

### 🌟 Multilevel Inheritance :-
```python
class A:
    def displayA(self):
        print("Welcome Mr. A")


class B(A):
    def displayB(self):
        print("Welcome Mr. B")


class C(B):
    def displayC(self):
        print("Welcome Mr. C.")


# create an object
obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
```