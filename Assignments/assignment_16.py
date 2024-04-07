# Que:1-> Write a python script to store multiple items in a single variable.(Items are "Java" , "Python" , "SQL" , "C")
items = ("Java", "Python", "SQL", "C")
print(items)
# Que:2 -> Write a python program to store only one item using tuple.
item = ("Java",)  # or item = "Java",
print(item)
# Que:3 -> Write a python program to reverse the tuple.
items = ("Java", "Python", "SQL", "C")
items_1 = list(items)
print('Original tuple is =', items)
items_1.reverse()  # another way we can reverse the tuple using slicing operator like this -> items_1[-1::-1]
print('Reverse tuple is =', tuple(items_1))
# Que:4 -> Write a python program to swap two tuples in python.
tp1 = (10, 20, 30, 40)
tp2 = ("Java", "Python", "C", "C++")
print("Before swapping tuple is :")
print('First tuple is =', tp1)
print('Second tuple is =', tp2)
# this is first method to swap tuples
tp1, tp2 = tp2, tp1
print('After swapping tuple is :')
print('First tuple is =', tp1)
print('Second tuple is =', tp2)
# Que:5 -> Write a python program to check if all items in the tuple are the same.
tp = (10, 20, 30, 40)  # declaring a tuple with different element.
tp1 = (1, 1, 1, 1)  # declaring another tuple with all elements are same(equal).

i = 0
while i < len(tp):
    if i + 1 == len(tp):  # if counter variable +1 is equal to size of the tuple then below condition will apply.
        if tp[len(tp) - 1] == tp[len(tp) - 2]:  # compare first last and second last element in the tuple.
            print("Tuple elements are equal.")
    elif tp[i] == tp[i + 1]:  # compare previous element to the next element.
        if i == len(tp) - 1:  # this condition is used to print below statement one time.
            print("Tuple all elements are equal.")
    else:
        print("Tuple elements are not equal.")
        break
    i += 1  # increment the value of i.
# Que:6 -> Write a python program to divide the tuple into four variable tuple1=(100,200,300,400)
tuple1 = (100, 200, 300, 400)
a, b, c, d = tuple1
print(a, b, c, d)
# Que:7 -> Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,
# 4,5,6)
tuple1 = (1, 2, 3, 4, 5, 6)
tp = tuple1[3:5]
print('New tuple is =', tp)
# Que:8 -> Write a python program to sort a tuple of tuples by the second item. tuple1=(('a',21),('b',31),('c',11),
# ('d',29) )
tuple1 = (('a', 21), ('b', 31), ('c', 11), ('d', 29))


# define a function to sort according the last element in the given tuple.
def myfunc(element):
    return element[1]


print("Before sorting tuple is:")
print(tuple1)
new_tuple = tuple(sorted(tuple1, key=myfunc))
print("After sorting the tuple with respect to second element.")
print(new_tuple)
# Que:9 -> Write a python program to print the value 20 from given nested tuple tuple1=("Python", [10,20,30],(2,4,16))
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])
# Que:10 -> Write a python program to change the first item (22) of a list within the following tuple to 222.
# tuple1=(11, [22,33],44,55)
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
