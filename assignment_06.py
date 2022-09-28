import calendar
#Que:1 ->Write a python script to check whether a given number is positive or non-positive.
num=int(input('Enter a number:'))
if num>0:
	print(num,'is positive number.')
else:
	print(num,'is non-positive number.') 
#Que:2 -> Write a python script to check whether a given number is divisble by 5 or not.
num=int(input('Entter a number:'))
if num%5==0:
	print(num,'is divisble by 5.')
else:
	print(num,'is not divisble by 5.')
#Que:3 -> Write a python script to check whether a given number is even or odd.
num=int(input('Enter a number:'))
if num%2==0:
	print(num,'is even number.')
else:
	print(num,'is odd number.')
#Que:4 -> Write a python script to print greater between two numbers.Print number only once if the numbers are the same.
a=int(input('Enter first number:')) 
b=int(input('Enter second number:'))
if a>b:
	print(a,'is greater than',b)
elif a==b:
	print(a)
	print('Both values are same.')
else:
	print(b,'is greater than',a)
    #Que:5 ->Write a python script to print two given words in dictionary order.
a=input('Enter first word:')
b=input('Enter second word:')
if a<b:
    print('Dictionary order is:',a , b)
else:
    print('Dictionary order is:',b , a)         
#Que:6 -> Write a python script to check whether a given number is a three digit number or not.
num=int(input('Enter a number:'))
if 99<num<1000:
   print(num,'is a three digit number.')
else:
 print(num,'is not a three digit number.')  
 #Que:7 -> Write a python script to check whether a given number is positive negative or zero.
a=int(input('Enter a number:'))
if a>0:
 	print(a,'is positve number.')
elif a==0:
 	print(a,'is zero.')           
else:
	print(a,'is negative number.')
#Que:8 -> Write a python script to check whether a given quardatic equation has two real and distinct (different) roots , real & equal roots or imaginary roots.
print('Enter the value of quardatic equation (ax^2b+ bx +c ) constants  or enter value of a , b and c:',end=' ')
a,b,c=int(input()),int(input()),int(input())
d=0
d=b**2-4*a*c
if d>0:
	print('Quardatic equation roots are real and different.')
elif d==0:
	print('Quardatic equation roots are real and equal.')
else:
	print('Quardatic equation roots are imaginary.')		 
#Que:9 -> Write a python script to check whether a given year is leap year or not.
num=input('You want to check leap year or century:')
if num.lower()=='century':
	century=input('Enter a century year:')
	if century.isdigit() and century[-1:-3:-1]=='00':
		print('Leap year in Century.') if int(century)%400==0 else print('Normal year in centry') 
elif num.lower()=='year':    
	year=int(input('Enter a year that you want to check leap year or not:'))
	print(year,'is a leap year') if year%4==0 else print(year,'Normal year.')       
#a=calendar.isleap(year)
#print('Year is leap:',a)
else:
	print('Invalid input.')
#Que:10-> Write a python script to print greater among three numbers.Print number only once even if the numbers are the same.
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))    
if a>b and a>c:
    print(a,'is the greatest number.')
elif b>c and b>a:
    print(b,'is the greatest number.')
elif a==b==c:
    print('All numbers are equal.','And number is=',a)    
else:
    print(c,'is the greatest number.')
#Que:11 -> Write a python script to take the month value in numeric format and display the number of days in it.
lst=[1,3,5,7,8,10,12]
lst2=[4,6,9,11]
month=int(input('Enter the month value:'))
if month in lst:
	print('This month in 31 days.')
elif month in lst2:
	print('This month in 30 days.')
elif month==2:
	print('This month in 28 or 29 days.')
else:
	print('Please enter value before 13.')		
'''year=int(input('Enter the year value:'))
month=int(input('Enter the month value:'))
if month>12 or month<=0:
    print('Please enter month value before 13.')
else:
    a=calendar.monthrange(year,month)
    print(f'Number of total days in {month} month is = {a[1]}')'''
#Que:12 -> Write a python script to accept one  number from the user and display the greater number between real part  and imaginary part.
a=eval(input('Enter a complex number:'))
if type(a)== complex:
    print(int(a.real),'Real part is greater.') if a.real>a.imag else print(int(a.imag),'Imaginary part is greater.')
else:
    print('Please enter a complex number.')