import keyword,A1,datetime 
            #Que:1 -> Write a python script to add comments and print "Lerning Python" on screen.
# This is a single line comment.
print("Learning Python")
    # Que:2 -> Write a python script to add multilne comments and print values of four variables esach in a new line variable contains any value.
a=10; b=12.45
c='Hello World'; d=99.87
# this is the first method to print the variable values in new line.
print(a)
print(b)
print(c)
print(d)
# this is the second method to print the variable values in new line.
print(a,'\n',b,'\n',c,'\n',d,sep='')
print(f'{a}\n{b}\n{c}\n{d}')
    # Que:3 -> Write a python script to print types of variables. create 5 variables each of them containing different types of data .(like:- 35,True,'MySirG',5.46,3+4j)
a=35
b=True
c="MySirG"
d=5.46
e=3+4j
print('The type of variable a is:',type(a))
print('The type of variable b is:',type(b))
print('The type of variable c is:',type(c))
print('The type of variable d is:',type(d))
print('The type of variable e is:',type(e))
    # Que:4 -> Write a python script to print the id of two variables containing the same integer values.
x=25
y=25 
print("The id of variable a is:",id(x))
print("The id of variable b is:",id(y))
    # Que:5 -> Create four variables in a python script and assign values of different data types to them,Write a python script to print value its type and id of each variable.
a=21
b=22.22
c='MySirG'
d=5+7j
print(f'The type of variable a is: {type(a)} and the id of variable a is:{id(a)}')
print(f'The type of variable b is: {type(b)} and the id of variable b is:{id(b)}')
print(f'The type of variable a is: {type(c)} and the id of variable c is:{id(c)}')
print(f'The type of variable a is: {type(d)} and the id of variable d is:{id(d)}')
    # Que:6 -> Write a python script to print all the keywords.
print(keyword.kwlist)
    #Que:7 ->On shell use help() function and display the list of keywords.
''' first on we will open python shell and type help() and then we will press enter key and now we will type "keywords" now the list of all keywords are appear on the screen.
help()
"keywords"      '''
    #Que:8 -> Create two python files A0.py and A1.py and asign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py.
print(A1.x)
    # Que:9 -> Name the keywords uses as data in the python script.
''' There are 3 keywords that is used as data in the python programme whose are:
    True , False , None  '''
a=True
b=False
c=None
print(a,b,c)    
    #Que:10 -> Write a python script to display the current date and time first create variables to strore date and time then display date and time in proper format ( like : 13-08-2022 and 9:00 pm) 
c=datetime.datetime.now()  
print(c.strftime(f'%d-%m-%Y and time is:- %I:%M %P')) # using f-string  
print(c.strftime('The date is: %d-%m-%Y And the time is: %I:%M:%S %P ')) # without f-string
    
 

