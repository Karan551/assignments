import math 
    #Que:1 -> Write a python script to take your name as input from the user and print it.
name=input('Enter your name:')
print('My name is:'+name)
    #Que:2 -> Write a  python script to take input from the user input must be a number.
num=int(input('Enter a number:'))
print(num)
    #Que:3 -> Write a python script which takes two numbers from the user then calculate their sum and display the result.
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
print('Sum of '+str(a)+' and '+ str(b) +' is = '+str(a+b))
    #Que:4 -> Write a python script which takes the radius from the user and display the area of a circle.
r=int(input('Enter the radius of a circle :'))
area=(math.pi)*r**2
print('Area of a circle : ',area)
print('Area of a circle : ',round(area,4))
    #Que:5 -> Write a python script to calculate their square of a number. number is entered by the user.
a=int(input('Enter a number : '))
print('Square of a number is =',a*a)
print('Square of a number is =',pow(a,2))    # this is the second method to find the square of a number.
    #Que:6 -> Write a python script to calculate the area of a triangle. Number is entered by the user.
b=int(input('Enter the base of the triangle : '))
h=int(input('Enter the height of the triangle : '))
area=1/2*b*h
print('Area of a triangle =',area)
    #Que:7 ->Write a python script to calculate average of three numbers entered by the user.
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
num3=int(input('Enter third number:'))
avg=(num1+num2+num3)/3
print(f'Average of {num1} ,{num2} and {num3} is= {avg}')
    #Que:8 -> Write a python script to calculate simple interest. 
p=int(input('Enter Amount which that you want to calculate Simple interest:'))
r=int(input('Enter rate of principal:'))
t=int(input('Enter time :'))
interest=(p*r*t)/100
print('Simple Interest is =',interest)
print('Amount is =',p+interest)
    #Que:9 -> Write a python script to calculate the volume of cuboid.
a=int(input('Enter the length of the cuboid: '))
b=int(input('Enter the width of the cuboid: '))
c=int(input('Enter the height of the cuboid: '))
volume=a*b*c
print('Volume of cuboid is=',volume,sep='')
    #Que:10 -> Write a python script to calculate area of rectangle.
length=int(input('Enter length of the rectangle:'))
width=int(input('Enter width of the rectangle:'))
area=length*width
perimeter=2*(length+width)
print('Area of rectangle =',area)
print('Perimeter of rectangle =',perimeter)