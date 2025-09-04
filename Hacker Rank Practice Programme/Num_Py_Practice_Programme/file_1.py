import numpy as np

#  How to create an array using numpy
arr = np.array([1, 2, 3, 4, 5])
print('this is 1-d array:\t', arr)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print('this is 2-d array:\n', arr_2d)
b = np.zeros(6, dtype=int)
# print(np.zeros((3, 3), int))
# print()
result = np.zeros((3, 3), int)
b = np.array(result)
# print(b)
# np.zeros()
c = np.ones(5)
# print("this will create an array :\n", np.arange(6))
arr = np.arange(6)
new_arr = arr.reshape(3, 2)
# print("this is new array::\n", new_arr)

# print("\n",np.reshape(arr,shape=(3,2)))
# print("this is flattened arr::\t", new_arr.flatten())
arr_2 = np.array([1, 2, 3, 4, 5])
print("this is numpy poly value::", np.poly(arr_2))


# print(c)

# print("this is an empty array:\n", np.empty(5))
# print("Create an array with a range of elements\n", np.arange(2, 10, 2))
# print(np.linspace(2, 7, num=5))

def arrTask():
    user_input = list(map(int, input("Enter a number space separated: ").split()))
    print(user_input)

    return numpy.array(user_input[::-1], float)


lst = []


# def zeroOrOnes
def zeroAndOneTask():
    user_input = list(map(int, input("Enter a number space separated: ").split()))
    # [3,3,3]
    print('this is list: ', user_input)
    print(np.zeros(user_input, int))
    print(np.ones(user_input, int))


# zeroAndOneTask()


print(np.array([1, 2]))


# print(np.concatenate((np.array([1, 2]))))


# print(lst)
def mergeArray():
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])
    print(np.concatenate((arr1, arr2)))


# mergeArray()
arr1 = []
arr2 = []


def mergeArrayProblem():
    n, m, p = input("Enter a space Separated Number: ").split()
    for _ in range(int(n)):
        user_input = list(map(int, input("enter space separated elements of col: ").split()))
        arr1.append(user_input)
        # np.concatenate(arr1)
    for _ in range(int(m)):
        user_input_2 = list(map(int, input("enter space separated elements of col: ").split()))
        arr2.append(user_input_2)


# print(arr1, "\n", arr2)
#
# print()
# print(np.concatenate((arr1, arr2)))
if __name__ == '__main__':
    # mergeArrayProblem()
    pass
