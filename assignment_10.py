#Que:1-> Write a python script to print MySirG N times on the screen.
n=int(input('How many times you want to print MySirG:'))
for i in range(1,n+1):
    print('MySirG',end=' ')
#Que:2-> Write a python script to print to print first N natural numbers.
n=int(input('\nHow many natural numbers you want to print:'))
for i in range(1,n+1):
    print(i,end=' ')
#Que:3-> Write a python script to print to print first N natural numbers in reverse order.
n=int(input('\nHow many natural numbers you want to print in reverse order:'))
for i in range(n,0,-1):
    print(i,end=' ')
#Que:4 -> Write a python script to print first N odd natural numbers.
n=int(input('\nHow many first odd natural numbers you want to print:')) 
for i in range(1,n+1):
    print(2*i-1,end=' ')
#Que:5 -> Write a python script to print first N odd natural numbers in reverse order.
n=int(input('\nHow many first odd natural numbers you want to print in reverse order:')) 
for i in range(n,0,-1):
    print(2*i-1,end=' ')
#Que:6 -> Write a python script to print first N even natural numbers.
n=int(input('\nHow many first even natural numbers you want to print:')) 
for i in range(1,n+1):
    print(2*i,end=' ') 
#Que:7 -> Write a python script to print first N even natural numbers in reverse order.
n=int(input('\nHow many first even natural numbers you want to print in reverse order:')) 
for i in range(n,0,-1):
    print(2*i,end=' ')
#Que:8 -> Write a python script to print squares of first N natural numbers.
n=int(input('\nHow many first natural numbers squares you want to print:'))
for i in range(1,n+1):
    #print(i*i,end=' ')     #this is second method
    print(i**2,end=' ') 
#Que:9 -> Write a python script to print cubes of first N natural numbers.
n=int(input('\nHow many first natural numbers cubes you want to print:')) 
for i in range(1,n+1):
    #print(i*i*i,end=' ') #this is second method
    print(i**3,end=' ')
#Que:10 -> Write a python script to print first 10 multiples of N.
n=int(input('\nWhich number first 10 multiples you want to print:'))
for i in range(1,11):
    print(n*i,end=' ')