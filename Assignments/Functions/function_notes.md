# Function :-

- Function is a block of code which only runs when it is called.
- Function has a name for identification.
- **Syntax :- (To create a function or define a function)** 👇

```python
def functionName(arguments):
    # code
    # code
    pass
```

- Once function is defined it can be called any number of times.
- **For example :-** 👇

```python
# define a function
def addNum(num1, num2):
    return num1 + num2


# To call a function
result = addNum(10, 12)
print("Result is :", result)

```
- **If function name without parentheses that means only a reference of that function is passed. That function will 
  not be executed.**
- **On other hand if function is written with parentheses so it will be called as usual.**
- **A function name without a parentheses is a reference to the function , while a function name with trailing 
  parentheses calls the function and refers to its return values.**
-----

## Python’s Functions Are First-Class :-

- **Python's function are first class objects.**
- **We can store them into a variable, store them into a datastructures,
  pass them as an argument or number of arguments to other functions, and even return them as values from other
  functions.**

- **For an Example :-** 👇

```python
# this is regular function
def yell(text):
    return text.upper() + '!'


# function call
yell("hello world")
# >>> HELLO !
```

#### Functions Are Objects :-

- **All data in a Python Program is represented by objects or relations between objects.** Things like **strings, lists,
  modules, and functions are all objects.** **There’s nothing particularly special about functions in Python.**

- Because `yell` function is an object in Python, so we can assign it into another variable.

  ```python
  # assign into another variable not function call
  bark = yell
  ```
- **This line does not call the function. It takes the function object referenced by `yell` and creates a second name
  pointing to it, `bark`. You could now also execute the same underlying function object by calling `bark`.**

  ```python
  # calling a function by reference variable.
  bark("hello world") 
  # >>> HELLO WORLD !
  ```
- **Function objects and their names are two separate concerns.**

- **We can delete the function’s original name (`yell`). Because another name (`bark`) still points to the underlying
  function you can still call the function through it.**

  ```python
  del yell 
  
  # function call
  yell("hello")
  # >>> NameError : "yell" is not defined
  
  # call by reference variable
  bark("hello")
  # >>> HELLO !
  ```
- By the way, Python attaches a string identifier to every function at creation time for debugging purposes. We can
  access this internal identifier with the `__name__` attribute.
  ```python
  bark.__name__
  # >>> yell
  ```
- While the function’s `__name__` is still **“yell”** that won’t affect how we can access it from our code. This
  identifier is merely a debugging aid. **A variable pointing to a function and the function itself are two separate
  concerns.**

#### Functions Can Be Passed To Other Functions :-

- **Because functions are objects, so we can pass them as arguments to other functions. Here’s a `greet` function that
  formats a greeting string using the function object passed to it and then prints it.**

  ```python
  # func is an argument represent to a function.
  def greeting(func):
      result=func("hello I'm a python developer.")
      print(result)
  
  # call a function and pass yell function as an argument which is also a function.
  greeting(yell)
  # >>> HELLO I'M A PYTHON DEVELOPER.!
  ```
- **The ability to pass function objects as arguments to other functions is powerful. It allows you to abstract away and
  pass around behavior in your programs.**

- **Functions that can accept other functions as arguments are also called higher-order functions. They are a necessity
  for the functional programming style.**
- _The classical example for **higher-order functions** in Python is the built-in `map` function. It
  takes **a function** and **an iterable** and calls the function on each element in the iterable, yielding the results
  as it goes along._

#### Functions Can Be Nested :-

- We can define a function inside another function that is called inner functions.
- Python allows functions to be defined inside other functions. These are often called nested functions or inner
  functions.
- **For an Example :-** 👇
  ```python
  def outer_function(text):
    
      # function definition
      def inner_function(t):
          return t.lower()
      
      # function call
      inner_function(text)
  
  # Outer function call
  outer_function("HELLO WORLD!")
  # >>> hello world!
  ```
- **For another Example :-** 👇
  ```python
  def speak(text):
    
      # inner function definition
      def whisper(t):
          return t.lower()
      
      # inner function call
      whisper(text)
  
  # outer function call
  speak("HELLO I'M A PYTHON PROGRAMMER.")
  # >>> hello i'm a python programmer.
  ```

- We can not call `inner function` from outside `outer function`.
- We can not do this:-
  ```python
  whisper("HELLO")
  # >>> NameError: 'whisper' is not defined.
  
  speak.whisper
  # >>> AttributeError : function object has not attribute whisper
  ```

- If we want to access that nested whisper function from outside `speak` function , **Well, functions are
  objects—you
  can return the inner function to the caller of the parent function.**

  ```python
  def get_speak_func(volume):
    
      # inner function definition
      def whisper(text):
          return text.lower() + '...'
      
      # # inner function definition
      def yell(text):
          return text.upper() + '!'
      
      
      if volume > 0.5:
          # return inner function definition here yell
          return yell
      else:
          # return inner function definition here whisper
          return whisper
  ```
- Notice how `get_speak_func` does not actually call one of its inner functions—it simply selects the appropriate
  function based on the volume argument and then returns the function object definition.
  ```python
  # function call
  get_speak_func(0.3)
  # >>> <function get_speak_func.<locals>.whisper at 0x10ae18>
  
  # function call
  get_speak_func(0.7)
  # >>> <function get_speak_func.<locals>.yell at 0x1008c8>
  
  ```

- **When we call outer function it returns inner function definition we can call directly inner function or assigning
  it to
  variable
  name first as we want.**

- **Here is Example :-** 👇
  ```python
  # first call outer function that will return inner function definition and further we call inner function.
  speak_func = get_speak_func(0.7)
  
  #  calling inner function
  speak_func('Hello')
  ```
- **This means not only can functions accept behaviors through arguments, but they can also return behaviors.**

#### Functions Can Capture Local State :-

- **Not only can functions return other functions, these inner functions can also capture and carry some of the parent
  function’s state with them.**

  ```python
  def get_speak_func(text, volume):
    
      # inner function
      def whisper():
          return text.lower() + '...'
      
      # inner function
      def yell():
          return text.upper() + '!'
      
      if volume > 0.5:
          # return function definition
          return yell
      else:
          # return function definition
          return whisper
  
  # function call
  get_speak_func('python world !',0.8)()
  
  # >>> PYTHON WORLD !
  
  ```

- Inner function `whisper` and `yell` have **no longer text parameter** , **But they can access** `text` parameter
  defined in
  the Parent function. **They capture and remember the value of that argument.**

- **Functions that do this are called lexical closures**. **A closure remembers the values from its enclosing lexical
  scope even when the program flow is no longer in that scope.**

  ```python
  # this is factory function
  def my_func(n):
      # inner function definition
      def num_power(x):
          return x ** n
  
      # return function definition
      return num_power
  
  
  # function call
  square_num = my_func(2)
  print(square_num(5))
  # >>> 25
  
  cube_num = my_func(3)
  print(cube_num(4))
  # >>> 64
  
  # we can also do like this 
  my_func(2)(5)
  # >>> 25
  
  my_func(3)(4)
  # >>> 64
  ```

### Objects Can Behave Like Functions :-

- **Objects aren’t functions in Python. But they can be made callable, which allows us to treat them like functions in
  many cases.**

  ```python
  class Adder:
      def __init__(self, n):
           self.n = n
      def __call__(self, x):
          return self.n + x
  
  plus_5 = Adder(5)
  
  print(plus_5(12))
  # >>> 17
  ```
- **Behind the scenes, “calling” an object instance as a function attempts to execute the object’s** `__call__` **method.**

###  Functions can be Stored in Data Structures :- 
- **As functions are first-class citizens you can store them in data structures, just like you can with other objects. For example, you can add functions to a list:**

  ```python
  funcs = [bark, str.lower, str.capitalize]
  
  ```

- Accessing the function objects stored inside the list works like it would with any other type of object:
  ```python
  for f in funcs:
      print(f('hey there')) 
  ```
- We can also do like this:-
  ```python
   funcs[0]('heyho')
   # >>> HEYHO !
   ```

#### What is Closure :-

- In a programming Language , **A closure , lexical closure or function closure** **is a technique for implementing
  lexically scoped name binding in a language with first-class functions.**
- **A closure is a record storing a function together with an environment.**
- [Click Here](https://en.wikipedia.org/wiki/Closure_(computer_programming)) **To Know about More Closure**.

#### What is First Class Function :-

- **In computer science, A programming language is said to have first-class functions if it treats functions as
  first-class citizens. This means the language supports passing functions as arguments to other functions, returning
  them as the values from other functions, and assigning them to variables or storing them in data structures.**

- **In languages with first-class functions, the names of functions do not have any special status; they are treated
  like ordinary variables with a function type.**