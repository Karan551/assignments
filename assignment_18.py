# Que:1->Write a python program to create and print a dictionary which stores your information.(name,age,
# education.......)
d1 = {'name': 'Kartik', 'age': 21, 'gender': 'male', 'education': 'graduate'}
print('The dictionary is:', d1)
# Que:2 ->Write a python program to access the items of a dictionary by referring to its key.
dct = {102: 'Rahul', 103: 'Arya', 104: 'Kartik', 105: 'Mahesh'}
for i in dct:
    print(i, ":", dct[i])
# Que:3 -> Write a python program to get the list of the values from a dictionary.
dct = {102: 'Rahul', 103: 'Arya', 104: 'Kartik', 105: 'Mahesh'}
print(dct.values())
# Que:4 -> Write a python program to print all key names in the dictionary one by one.
dct = {102: 'Rahul', 103: 'Arya', 104: 'Kartik', 105: 'Mahesh'}
print('All keys is =', end=' ')
for i in dct:
    print(i, end=' ')
# Que:5 -> Write a python program to change the value of a specific item by referring to its key name.
student = {102: 'Rahul', 103: 'Arya', 104: 'Kartik', 105: 'Mahesh'}
student.update({102: "Mahesh"})  # this is the first method using update().
# student[102] = 'Ganesh'  # edit the value of student dictionary.(this is the second method.)
print('\n', student, sep='')
# Que:-6 -> Write a python program to create a dictionary that contains three dictionaries (nested).
bigshop = {'shop1': {1: 'Monitor', 2: 'CPU', 3: 'Printer', 4: 'Accessories'},
           'shop2': {1: 'Copy', 2: 'Book', 3: 'Pen', 4: 'Pencil'},
           'shop3': {1: 'LED', 2: 'Smart LED', 3: 'Refrigerator', 4: 'Smart TV'}
           }
print("New nested dictionary:")
print(bigshop)
# Que:7-> Write a python program to create three dictionaries then create one dictionary that will contain the other
# three dictionaries.
child1 = {'name': 'Mahesh', 'age': 24, 'profession': 'Software Engineer', 'gender': 'Male'}
child2 = {'name': 'Ganesh', 'age': 21, 'profession': 'Engineer', 'gender': 'Male'}
child3 = {'name': 'Glade rial', 'age': 20, 'profession': 'Soldier', 'gender': 'Female'}
myfamily = {'child1': child1,
            'child2': child2,
            'child3': child3}
print(myfamily)
# Que:8-> Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and
# item from list2 is the value.
appliances = ['computer', 'cpu', 'monitor', 'printer']
number_of_appliances = [10, 12, 15, 16]
appliances_dict = {}  # create an empty dictionary.
if len(appliances) == len(number_of_appliances):
    for i in range(len(appliances)):
        # we pass a first list element as a key and second list element as a value(using update method).
        # (this is the first method)
        appliances_dict.update({appliances[i]: number_of_appliances[i]})
        # this is the second method.
        # appliances_dict[appliances[i]] = number_of_appliances[i]
else:
    print("Please enter number of both list elements is equal.")
print(appliances_dict)

# Que:9-> Write a python program to merge two python dictionaries into one dictionary.
child1 = {'name': 'Kartik', 'age': 21, 'gender': 'male', 'education': 'graduate'}
child2 = {'name': 'Rocky', 'age': 22, 'gender': 'male'}
family = {'child1': child1, 'child2': child2}
print(family)
# Que:10 -> Write a python program to get the key of lowest value from the dictionary .
# sample_dict={'C':92,'Java':66,'Python':85}
sample_dict = {'C': 92, 'Java': 66, 'Python': 85}
lst = [i for i in sample_dict.values()]  # creating a  list to find minimum value.
a = min(lst)  # find minimum value.
for i in sample_dict:
    if sample_dict[i] == a:  # comparison of dictionary values to the minimum value.
        print('Minimum data value of key is =', i)  # print the value of minimum key.
