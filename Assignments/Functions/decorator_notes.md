# Inner Functions :-

- **We can define a function Inside other function such functions are called Inner function.**
- Here is an example of Inner function :- 👇

  ```python
  def parent():
      print("This is parent function.")
  
      # function definition
      def first_child():
          print("This first child function Inside parent function.")
  
      # function definition
      def second_child():
          print("This is second child function Inside parent function.")
  
      # function call
      second_child()
      first_child()
  
  
  # call parent function
  parent()
  # >>> This is parent function.
  # >>> This is second child function Inside parent function.
  # >>> This first child function Inside parent function.
  ```

- We can not access inner function outside of parent function because of their local scope.

## Function as Return Values :-

- **Python also allow us return function from function.**

  ```python
  def parent(num):
      
      def first_child():
          return "Hi, I'm First child"
  
      def second_child():
          return "I'm Second Child"
  
      if num == 1:
          # return function definition
          return first_child
      else:
           # return function definition
          return second_child
  ```
- We are returning `first_child` without parentheses. It means we’re returning a reference of 
  `first_child` function.`first_child()` **with parentheses refers to the result of evaluating the function.**  
  ```python
  # This will point first child function.
  first = parent(1)
  # >>> <function parent.<locals>.first_child at 0x703f4051d4e0>
  
  # This will point second child function.
  second = parent(2)
  # >>> <function parent.<locals>.second_child at 0x703f4051d620>
  ```
- **Output means that the `first` variable refers to the local `first_child()` function inside of` parent()`, while 
  `second` points to `second_child()`.**
- **We can now use `first` and `second` as if they’re regular functions, even though you can’t directly access the 
  functions they point inner function.**

  ```python
  # calling a function
  first()
  # >>> Hi I'm First Child.
  
  # calling a function
  second()
  # >>> Hi I'm Second Child.
  ```
------
# Decorators :-

- Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a **function** or **class**. **Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.** 
- Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

### How To Create a Decorator Function :- 
- **Decorating a function if function has pass no parameters or arguments.**
- **Syntax :-** 👇
  ```python
  def decorator(func):
      def wrapper():
          func()
          
      return wrapper
  ```

### Decorating a function with arguments :-

- **Syntax :-** 👇
  ```python
  def decorator(func):
      def wrapper(*args, **kwargs):
          func(*args, **kwargs)
  
      return wrapper
  ```

### Returning Values From Decorated Functions :-

- **Syntax :-** 👇
  ```python
  def decorator(func):
      def wrapper(*args, **kwargs):
          return func(*args, **kwargs)
  
      return wrapper
  ```

### Other Syntax or Boilerplate of Decorator :- 

```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

## How can use Decorator :-

```python
# decorator function
def decorator(func):
  def wrapper(*args, **kwargs):
    print("function name is :", func.__name__)
    return func(*args, **kwargs)

  return wrapper

# function that we use decorator
def add_num(num1, num2):
  return num1 + num2


# First method to use decorator (detail method)
my_num = decorator(add_num)
print("result is :", my_num(12, 15))
```

- **Python allows you to use decorators in a simpler way with the `@ symbol`, sometimes called the pie syntax. The following example does the exact same thing as the first decorator example:**
- **Second Syntax :-** 👇
```python
# function that we use decorator

@decorator
def add_num(num1, num2):
  return num1 + num2


# function call
result = add_num(12, 15)
print("result is :", 27)

```

- So, `@decorator` is just a shorter way of <br/> **add_num = decorator(add_num)**.<br/> It’s how you apply a decorator to a 
  function.

> **Note:-**  You can name your inner function whatever you want, and a generic name like `wrapper()` is usually okay. 
> You’ll see a lot of decorators in this tutorial. To keep them apart, you’ll name the inner function with the **same name as the decorator** but with a **wrapper_ prefix**.