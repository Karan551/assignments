	#Que:1 -> Write a python script to create a string 3 different possible ways.
a='MysirG'	#using single quotes
b="iNeuron"	#using double quotes
c='''Hello Python'''	#using triple quotes
print(a,b,c,sep=' , ')
	#Que:2 -> Write a python script to get the characters from the start to position 5 (given string "iNeuron" using the slice syntax.)
string="iNeuron"
print('String is =',string[0:5])
	#Que:3 -> Write a python script to get the characters from position 2 to position 5  (Given string "Hello Learners" using the slice syntax. )
str1="Hello Learners"
print('String is =',str1[1:5])
	#Que:4 -> Write a python script to demonstrate string concatenation ading space in between Given strings a="Learning" b="Python"
a="Learning" ; b="Python"
print('Finally string is = '+a+' '+b)
	#Que:5 -> Write a python script to get the count the total number of characters in string a="iNeuron"
a="iNeuron"
print(f'Total number of characters in "iNeuron" is = {len(a)}')
	#Que:6 -> Write a python script to reverse a string "iNeuron"
a="iNeuron"
print('Reverse string is =',a[-1:-8:-1])
	#Que:7 ->Write a python script to determine whether a string contains a specific substring.
string='Hello Kartik . How are you ? I am fine and you. Where are you at present ?'
print('This is a string.\n'+string)
sub=input('Enter a substring that you want to search :')
y=string.find(sub)
if y== -1:
	print('This substring is not in the above string.')
else:
	print("This substring / character starting index is =",y)
	#Que:8 -> Write a python script to check if a string contains only numbers.
num=input('Enter a number:')
if num.isdigit():
	print('This string contains only numbers.')
else:
	print('This is a Alphabetical or AlphaNumeric string.')
	#Que:9 -> Write a python script to check if a string contains only characters of the alphabet.
name=input('Enter a alphabet: ')
if name.isalpha():
	print('This is a alphabetical string.')
else:
	print('This is a alphanumeric or numeric string.')
	#Que:10 -> Write a python script to convert an integer to a string.
num=int(input('Enter a number:'))
num=str(num)
print(num,"it's type =",type(num))		