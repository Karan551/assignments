import pickle
import shutil
import keyword

# Que:1-> Write a python script to print the following status of a file:
# a) whether a file is read only
file = open('first.txt', 'r')
# b) whether a file is closed or not
print('File is closed or not:', file.closed)
# c) which file opening mode is used
print('File mode is :', file.mode)
# d) Name of  the file
print('File name is :', file.name)
# closing the file.
file.close()
# Que:2-> Write a python script to create a new file 'myfile.txt' and store user entered text.
text = input('What you want to write in a file (myfile.txt) :')
f = open('myfile.txt', 'w')
f.write(text)
f.close()
# Que:3-> Write a python script to read the above content file 'myfile.txt' and display
# the content on the console.
with open('myfile.txt', 'r') as file:
    print(file.read())
# Que:4-> Write a python script to store list of cities name in a file 'cities.txt'.
# To create a list of cities.
city = ['Hyderabad ', 'Pune ', 'Bangalore ', 'Bhopal ', 'Lucknow ']
# To write the iterable in file.
with open('cities.txt', 'w') as file:
    file.writelines(city)
# Que:5-> Write a python script to append list of city names in a file 'cities.txt'.
# To create a list of cities that we will have to append in the file.
cityList = [' Surat ', ' Amritsar ', ' London ', 'Mumbai']
# To append list of city in file.
with open('cities.txt', 'a') as file:
    file.writelines(cityList)


# Que:6->Write a python script to search whether a particular city is there in the file
# 'cities.txt' or not.
def search_city(search_city_name: str):
    with open('cities.txt', 'r') as file_2:
        line_count = 0
        for line in file_2.readlines():
            line_count += 1
            # convert list of str type elements.
            str_list = line.split()
            word_count = 0
            for word in str_list:
                word_count += 1
                # convert both word into lower case.
                if word.lower() == search_city_name.lower():
                    return word_count, line_count
        else:
            return None


# enter city name that you want to search
city_name = input("Enter city name that you want to search:")
# calling a function and check that is not return None.
if search_city(city_name) is not None:
    word_number, line_number = search_city(city_name)
    print(f"{city_name} is 'cities.txt' file in {word_number} word and line is ={line_number} ")
else:
    print(f"{city_name} is not in the 'cities.txt file.'")


# Que:7-Write a python script to count the number of python keywords occurring in
# a python source file.
def countKeyword(fileName):
    """
    This function is used to count the keyword in given python source file.
    It also counts the keywords in strings and comment also.
    :param fileName:
    :return:int
    """
    with open(fileName, 'r') as key_file:
        # To display the content in the console.
        line_count = 0
        keyword_count = 0
        for line in key_file.readlines():
            # count the line in given file
            line_count += 1
            # To convert space separated list.
            str_list = line.split()
            # iterate over the given string type elements in list.
            for keys in str_list:
                # if keywords end with colon then this condition is True.
                if keys.endswith(':'):
                    keys = keys.rstrip(':')
                    if keyword.iskeyword(keys):
                        keyword_count += 1
                # this is normal situation to handle that and count the keyword.
                else:
                    if keyword.iskeyword(keys):
                        keyword_count += 1
        return keyword_count


# calling a function and print the result.
print("Total keywords are:", countKeyword('hello.py'))
# Que:8-> Write a python script to create a copy of a file.
destination = 'F:/Web Projects/Programmes/'
source = './first.txt'
# To copy a file we use the following method.
shutil.copy(source, destination)
# Que:9->Write a python script to store book data in a file. Book data is the
# form of a dictionary in which book name is the key and price is its value.
# Use pickle to store data into a file (say book-file)
bookFile = {'Discovery of India': 500, 'Mathematics': 550, 'Reasoning': 250}
f = open('first.txt', 'wb')
pickle.dump(bookFile, f)
f.close()
# Que:10-> Write a python script to extract book data from a book-file using pickle Also print
# extracted book data.
f = open('first.txt', 'rb')
# using pickle module to load the data.
s = pickle.load(f)
for key, value in s.items():
    print(key, ":", value)
f.close()
