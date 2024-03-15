    #Que:1 -> Write a python script to remove the last digit from a given number.(for example if user enters 2534 then your output should be 253)
a=int(input('Enter a number:'))
q=a/10
print('Remained number is:',int(q)) # first method  
print('Remaining number is:',a//10) # second method
    #Que:2 -> Write a python script to get the last digit from a given number.
num=int(input('Enter a number:'))
rem=num%10
print(f'Last digit of {num} is = {rem}')
#Que:3 -> Wriite a python script to swap data of two variables.
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
print(f'first number is = {a} , And second number is = {b}')
#using temproary variable
temp=0
temp=a
a=b
b=temp
print(f'After swapping number first number is = {a} , second number is = {b}')
#second method 
a,b=b,a     # swapping of value
#print(f'After swapping number first number is = {a} , second number is = {b}')
    #Que:4 -> Write a python script to find x power y where values x and y are given by user.
x=int(input('Enter the base value:'))
y=int(input('Enter the power value:'))
print(f'{x} power {y} is = {x**y}')    # first method
print(f'{x} power {y} is = {pow(x,y)}') # second method
    #Que:5 -> Write a python script which takes three digit number from the user and displays only first digit.
a=int(input('Enter three digits number:'))
print(f'First digit of {a} is = {a//100}')     #first method 
print('First digit of '+str(a)+' is = ',int(a/100),sep='')    #second method
    #Que:6 -> Write a python script which takes a three digit number from the user and display only its middle digit.
a=input('Enter three digits number:')
print('Middle digit '+a+' is( using first method) = ',a[1],sep='')     # first method 
# second method
b=int(input('Enter three digits number:'))
c=b%100
d=c//10
print('Middle digit is (using second method) =',d)
    #Que:7 -> Write a python script which takes a three digit number from the user and display only its last digit.
a=input('Enter three digit number:')
print("Last digit is (first method) =",a[2])    #first method
# second method
b=int(input('Enter three digit number:'))
rem=b%10
print('Last digit is (second method) =',rem)
    #Que:8 -> Write a python script to use IN operator to display the data present in the list.
lst=[11,12,'Hello','Python','MySirG','Ineuron', 21 ]
print('the list is :',lst)
a=input('Enter the data that you want ot search:')
if a.isdigit():
    a=int(a)
    print(a,'in list',a in lst)
else:
    print(a,'in lst:',a in lst)
    # Que:9 -> Write a python script to use NOT IN operator to display the data not present in list.
print(a,'not in lst:',a not in lst)
    #Que:10 -> Write a python script to use IS operator to display if both variables are the same object or not ?
x=5
y=5
print('x is y:',x is y)