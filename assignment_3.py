    #Que:1 -> Write a python script to convert a number into str format.
#num=int(input("Enter a number:"))
#print('The conversion of a number is str format='+str(num))
#Que:2-> Write a python script to print a Unicode of character of 'm'.
a='m'
#print(f'The Unicode of character {a} is = {ord(a)}')
#Que:3 -> Write a python script to print representation of a given unicode 100.
b=100
#print(f"Character of Unicode {b} is = {chr(b)}")
    #Que:4 -> Write a python script to print any number and its binary equivalent.
#Taking input from the user
#num=int(input("Enter a number:"))
#print(f'The binary equivalent of {num} is = '+bin(num))
#print(f'The binary equivalent of {num} is = '+bin(num).lstrip('0b'))
    #Que:5 -> Write a python script to print any number and its hexadecimal equivalent.
#num=int(input('Enter a number:'))
#print(f'The octal equivalent of {num} is = '+oct(num)) # To understand a programmer
#print(f'The octal equivalent of {num} is = '+oct(num).lstrip('0o')) # To understand normal user
    #Que:6 -> Write a python script to print any number and its hexadecimal format.
#num=int(input("Enter a number:"))
#print(f'The Hexadecimal equivalent of {num} is = '+hex(num))
#print(f'The Hexadecimal equivalent of {num} is = '+hex(num).lstrip('0x'))
    #Que:7 -> Write a python script to store binary number 1100101 in a variable and print it in decimal format.
num=0b0111   # this is a binary number
print('Decimal number is =',num)
    #Que:8 -> Write a python script to store a hexadecimal number 2F in a variable and print it in Octal format.
x=0x2F # due to hexadecimal number add 0x
print('Decimal number is =', x)
    # Que:9 -> Write a pythob script to stroe an octal number 125 in a variable and print it in binary format.
y= 0o125 # due to octal number add 0o
print('Binary number is = ',bin(y))
    #Que:10 -> Write a python script to add two numbers 25 (in octal ) and 39 (in hexa decimal ) and display the result in binary format.
a=0o25    # due to octal number add 0o
b=0x39    # due to hexa deciamal number add 0x 
print('Decimal number is =',a+b)
print('Addition is =',bin(a+b))
 
