# ---------------- Polynomial -------------------
import numpy as np

print(np.polyval([1.1, 2, 3], 0))

x = int(input("Enter the value of x: "))
# user_input = map(float, input("Enter space separated value: ").split())

# print(list(user_input))
# arr = np.array([*user_input])
# print(np.polyval(arr, x))

lst = [list(map(float, input("Enter space separated value: ").split())) for _ in range(x)]
print(lst)

arr = np.array(lst)
print(round(np.linalg.det(arr),2))


def polyval_problem(arr_elements: list[int], x):
    arr = np.array([*arr_elements])
    print(np.polyval(arr, x))
    pass


if __name__ == '__main__':
    # polyval_problem()
    pass
