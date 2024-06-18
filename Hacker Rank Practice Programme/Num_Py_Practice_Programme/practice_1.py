import numpy as np

# How To Create an array:-

# This is one dimension array.
arr = np.array([101, 2, 13, 4, 5, 36])

# This is two dimensions array
arr_2 = np.array([[1, 2, 43, 4], [5, 6, 37, 8], [10, 111, 12, 103]], )
# print("this is an array ", arr)
# print("Shape of array is:", arr.shape)
# print("Size of the array is", arr.size)
# print("Data type of array is", arr.dtype)
# print("Dimension of the array is", arr.ndim)


# print("this is an array \n", arr_2)
# print("Shape of array is:", arr_2.shape)
# print("Size of the array is", arr_2.size)
# print("Data type of array is", arr_2.dtype)
# print("Dimension of the array is", arr_2.ndim)

# ----------How To Create a basic array
zero_arr = np.zeros((2, 3), int)
# print(zero_arr)

ones_arr = np.ones((2, 3), int)
# print(ones_arr)

empty_arr = np.empty(2)
# print(empty_arr)

line_arr = np.linspace(0, 10, num=5, dtype=int)
# print(line_arr)

arrange_arr = np.arange(2, 20, 2)
# print(arrange_arr)

# -------------Sort of an array
arr_3 = np.sort(arr)
# print(arr_3)
arr_4 = np.sort(arr_2)
# print(arr_4)

# print(np.concatenate((arr,arr_2)))