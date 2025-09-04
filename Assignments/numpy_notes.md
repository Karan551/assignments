# 🌟 Numpy :-

- **It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays
  and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape
  manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical
  operations, random simulation and much more.**

### 🌟 What is an Array :-

- In computer programming, an array is a structure for storing and retrieving data. We often talk about an array as if
  it were a grid in space, with each cell storing one element of the data.

- **Most NumPy arrays have some restrictions. For instance:**

    - **All elements of the array must be of the same type of data.**

    - **Once created, the total size of the array can’t change.**

    - **The shape must be “rectangular”, not “jagged”; e.g., each row of a two-dimensional array must have the same
      number of columns.**

#### 🌟 How To Create An Array :-

```python
import numpy as np

# create an one dimensional array
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)
# <<< [1 2 3 4 5]

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# <<< [ [1 2 3]
#  [4 5 6]]
```

#### 🌟 How To Create A Basic Array :-

1. `np.zeros(shape,dtype)` :- **Return a new array of given shape and type, filled with zeros.**
    - `shape` :- `int` or `tuple` of `int`.
    - `dtype` (optional)
    - [Click Here](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html) For More Information.
2. `np.ones(shape,dtype)` :- **Return a new array of given `shape` and `type`, filled with `ones`.**
3. `np.empty(shape,dtype)` :- **The function empty creates an array whose initial content is random and depends on the
   state of the memory. The reason to use empty over zeros (or something similar) is speed - just make sure to fill
   every element afterwards!**
4. `np.arange([start],stop,[step])` :- **And even an array that contains a range of evenly spaced intervals. To do this,
   you will specify the first number, last number, and the step size.**
5. `np.linspace(start,stop,num)` :-To create an array with values that are spaced linearly in a specified interval.

#### 🌟 Array Properties :-

1. `np.size` :- **This will tell you the total number of elements of the array.**
2. `np.dytpe` :- **This will tell you data type of the array.**
3. `np.ndim` :- **This will tell you the number of axes, or dimensions, of the array.**
4. `np.shape` :- **This will display a `tuple` of integers that indicate the number of elements stored along each
   dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array
   is `(2, 3)`.**

### 🌟 Array Reshaping :-

- **Reshaping means will give a new shape to an array without changing its data.**
- **Syntax :-** 👇
    - `np.reshape(array, shape)`


- `np.flatten()` :- **Return a copy of the array collapsed into one dimension.**
- `Transpose` :- **This will transpose of the given array.**
    - **To create an Transpose of the array** :- 👉 `arr.T`
- `np.ravel()` :- **Return a contiguous(next,neighbor) flattened array.**

```python
import numpy as np

# ----------- first method -----------  
arr = np.arange(6)
# [0 1 2 3 4 5]
new_arr = arr.reshape(3, 2)
print(new_arr)
""" <<<
[[0 1]
 [2 3]
 [4 5]]
"""

# ------------- second method ------------------
new_arr = np.reshape(arr, shape=(3, 2))

""" <<<
[[0 1]
 [2 3]
 [4 5]]
"""
# # ------------- flattened------------------
flattened_arr = new_arr.flatten()
print(flattened_arr)
# <<< [0 1 2 3 4 5]
```

[Click Here](https://github.com/Karan551/assignments/blob/main/Learn%20Numpy/phase_1.ipynb) To Know difference between
`ravel()` and `flatten()` method.
--------

--------

- `np.poly()` :- **This poly tool returns the _coefficients of a polynomial_ with the given sequence of roots.**
- `np.roots()` :- **The roots tool returns the roots of a polynomial with the given coefficients.**
- `np.polyint()` :- **The `polyint` tool returns an antiderivative (indefinite integral) of a polynomial.**
- `np.polyval()` :- **The `polyval` tool evaluates the polynomial at specific value.**
- [Click Here](https://numpy.org/doc/stable/reference/routines.polynomials.poly1d.html) For More Information.