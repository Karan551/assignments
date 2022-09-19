#Que:1 -> Write a python script to print MySirG N times on the screen.
n=input('How many times you want to print MySirG:')
if n.isdigit():
    n=int(n)
    i=1
    while i<=n:
        print("MySirG", end=' ')
        i+=1
else:
    print('Please enter a digit.')
#Que:2 -> Write a python script to print first N natural numbers.
n=input('\nHow many natural numbers you want to print:')
if n.isdigit():
    n=int(n)
    print(f'First {n} natural numbers are :')
    i=1
    while i<=n:
        print(i,end=' ')
        i+=1
else:
    print("Please enter a digit.")
#Que:3 -> Write a python script to print first N natural numbers in reverse order.
n=input('\nHow many natural numbers you want to print in reverse order:')
if n.isdigit():
    n=int(n)
    print(f'First {n} natural numbers in reverse order:')
    i=n
    while i>0:
        print(i,end=' ')
        i-=1
else:
    print('Please enter a digit.')        
#Que:4 -> Write a python script to print first N odd natural numbers.
n=input('\nHow many odd numbers you want to print:')
if n.isdigit():
    print(f'First {n} odd natural numbers are :')
    n=int(n)
    i=1
    while i<=n:
        print(2*i-1,end=' ')
        i+=1
else:
    print('Please enter a digit.')        
#Que:5 -> Write a python script to print first N odd natural numbers in reverse order.
n=input('\nHow many times you want to print first odd natural numbers in reverse order:')
if n.isdigit():
    n=int(n)
    print(f'First {n} natural numbers in reverse order :')
    i=n
    while i>0:
        print(2*i-1,end=' ')
        i-=1
else:
    print('Please enter a digit.')        
#Que:6 -> Write a python script to print first N even natural numbers.
n=input('\nHow many first even natural numbers you want to print:')
if n.isdigit():
    n=int(n)
    print(f'First {n} even natural numbers are :')
    i=1
    while i<=n:
        print(2*i,end=' ')
        i+=1
else:
    print("Please enter a digit.")        
#Que:7 -> Write a python script to print first N even natural numbers in reverse order.
n=input('\nHow many even natural numbers you want to print in reverse order:')
if n.isdigit():
    n=int(n)
    print(f'First {n} natural numbers in reverse order:')
    i=n
    while i>0:
        print(2*i,end=' ')
        i-=1
else:
    print('Please enter a digit.')        
#Que:8 -> Write a python script to print  squares of first N natural numbers.
n=input('\nHow many squares of first natural numbers you want to print:')
if n.isdigit():
    n=int(n)
    print(f'First {n} square natural numbers are :')
    i=1
    while i<=n:
        print(i**2,end=' ')
        i+=1 
else:
          print('Please enter a digit.')
#Que:9 -> Write a python script to print  cubes of first N natural numbers.
n=input('\nHow many cubes of first natural numbers you want to print:')
if n.isdigit():
    n=int(n)
    print(f'Cubes of First {n} natural numbers are :')
    i=1
    while i<=n:
        print(i**3,end=' ')
        i+=1
else:
    print('Please enter a digit.')  
#Que:10 -> Write a python script to print of first 10 multiples of N. 
n=input('\nWhich number you want to print first 10 multiples:')
if n.isdigit():
    n=int(n)
    print(f'First 10 multiplies of {n} :')
    i=1
    while i<=10:
        print(i*n,end=' ')
        i+=1
else:
        print('Please enter a digit.')
            