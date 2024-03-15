#Que:1-> Write a recursive python function to print first N natural numbers.
n=int(input('How many natural numbers you want to print:'))
def printN(n):
	if n>0:
		printN(n-1)
		print(n,end=' ')
printN(n)
#Que:2->Write a python function to print first N natural numbers in reverse order.
n=int(input('\nHow many first N natural numbers in reverse order you want to print:'))
m=n+1
def reversePrintN(n):
	if n>0:
		reversePrintN(n-1)
		print(m-n,end=' ')
reversePrintN(n)			
#Que:3-> Write a recursive python function to print first N odd natural numbers.
n=int(input('\nHow many first odd natural numbers you want to print:'))
def oddNum(n):
	if n>0:
		oddNum(n-1)
		print(2*n-1,end=' ')
oddNum(n)
#Que:4->Write a recursive python function to print first N odd natural numbers in reverse order.
n=int(input('\nHow many first N odd natural numbers in reverse order you want to print:'))
m=(2*n-1)+1
def reverseOddN(n):
	if n>0:
		reverseOddN(n-1)
		print(m-(2*n-1),end=' ')
reverseOddN(n)		
#Que:5->Write a recursive python function to print first N even natural numbers.
n=int(input('\nHow many first even natural numbers you want to print:'))
def evenNum(n):
	if n>0:
		evenNum(n-1)
		print(2*n,end=' ')
evenNum(n)
#Que:6->Write a recursive python function to print first N even natural numbers in reverse order.
n=int(input('\nHow many first N even natural numbers in reverse order you want to print:'))
m=2*n+2
def reverseEvenN(n):
	if n>0:
		reverseEvenN(n-1)
		print(m-(2*n),end=' ')
reverseEvenN(n)	# calling a function		 
#Que:7->Write a recursive python function to print squares of first N natural numbers.
n=int(input('\nHow many squares of  first  natural numbers you want to print:'))
def squareN(n):
	if n>0:
		squareN(n-1)
		print(n*n,end=' ')
squareN(n)
#Que:8->Write a recursive python function to print cubes of first N natural numbers.
n=int(input(f'\nHow many cubes of first N natural numbers you want to print: '))
def cubeN(n):
	if n>0:
		cubeN(n-1)
		print(n*n*n,end=' ')
cubeN(n)
#Que:9-> Write a recursive python function to print first N multiples of a given number.
num=int(input('\nWhich number multiples you want to print:'))
n=int(input(f'How many multiples of {num} you want to print:'))
def multiplesN(n):
	if n>0:
		multiplesN(n-1)
		print(num*n,end=' ')
multiplesN(n)
#Que:10->Write a recursive python function to print a number in reverse order.
n=int(input('\nWhich number you want to print in reverse order:'))
m=n+1
def reverseNum(n):
	if n==0:
		return 0
	reverseNum(n-1)
	print(m-n,end=' ')
reverseNum(n)							