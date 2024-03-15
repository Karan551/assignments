	#Que:1 -> Write a  python script to store multiple items in a single variable(items are "Java" , "Python" , "SQL" , "C") using list.
lst=["Java", "Python","SQL","C"]
print("The List is:",lst)
    #Que:2 -> Write a python script to get a data type of a list.
print('The data type of the list is:',type(lst))
    #Que:3 -> Write a python script to get the last item of the list (mylist=["Java","C","Python"] )
mylist=["Java","C","Python"]
print('The last item of the list is:',mylist[-1])
    #Que:4 -> Write a python script to change the values of "SQL" and "Reactnative" with the values "NOSQL" and "Flutter". (LIst is thislist=["Java" , "SQL" ,"C" , " Reactnative" , "Javascript" ,"Python" ] )
thislist=["Java" , "SQL" ,"C" , " Reactnative" , "Javascript" ,"Python" ]
thislist[1]= "NOSQL"
thislist[3]="Flutter"
print('final list is:',thislist)
    #Que:5 -> Write a python script to add an item to the end of the list (item ="Python") (mylist=["Java" , "SQL" , "C" , "Reactantive" ] )
mylist=["Java" , "SQL" , "C" , "Reactantive" ] 
mylist.append("Python")
print("After appending the list is:",mylist)
    #Que:6 -> Write a python script to append elements from another list to the current list.(firstList=["Java" , "Python" , "SQL"]  secondList=["C" , "Cpp" ,"NoSQL" ] )
firstList=["Java" , "Python" , "SQL"]     #current list
secondList=["C" , "Cpp" ,"NoSQL" ]     #another list
firstList+=secondList
print('Finally the list is :',firstList)
    #Que:7 -> Write a python script to print all items by referring to their index number.(thislist=["Java" , "SQL" , "C" , '"Rectnative"' , "Javascript" , "Python"] )
thislist=["Java" , "SQL" , "C" , "Rectnative" , "Javascript" , "Python"]
for i in range(0,len(thislist)):
    print('index',i,'=' ,thislist[i]) 
    #Que:8 -> Write a python program to sort the list alphanumerically - thislist=["Java" , "SQL" , "C" , "Rectjs" , "Javascript" , "Python" ]    
thislist=["Java" , "SQL" , "C" , "Rectjs" , "Javascript" , "Python" ] 
thislist.sort()  
print('Sorted list is =',thislist)
	#Que:9 -> Write a python script to create a list of city names taken from the user.
lst=[]
j=0
num=int(input('How many city names you want to enter:'))
for i in range(1,num+1):
    cityName=input('Enter a city name:')
    lst.append(cityName)
print("City name is :", lst)
	#Que:10 -> Write a python script to crate a list where each of the list element is a digit of a given number.
element=int(input('How many elements you want to add in the list:'))
lst=[]
for i in range(1,element+1):
	num=input('Enter a number that you want to add the list element:')
	if num.isdigit():
	    num=int(num) 
	    lst.append(num)
	else:
		print('Please enter a number.')    
print('Finally the numbers list is =',lst)                