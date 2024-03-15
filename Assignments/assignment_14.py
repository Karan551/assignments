	#Que:1 -> Write a python script to create a list of first N natural numbers.
num=int(input('How many first Natural numbers you want to add in the list:'))
lst=[ i for i in range(1,num+1)]
print(f'Finally first {num} number list is = {lst}')
	#Que:2 -> Write a python script to create a list of first N odd natural numbers.
num=int(input('How many first odd numbers you want to add in the list:'))
lst=[ (2*i-1) for i in range(1,num+1) ]
print(f'Finally first {num} odd numbers list is = {lst}')
	#Que:3 -> Write a python script to create a list of first N even natural numbers.
num=int(input('How many first even numbers you want to add in the list:'))
lst=[ 2*i for i in range(1,num+1) ]
print(f'Finally first {num} even numbers list is = {lst}')
	#Que:4 -> Write a python script to find the greatest number in a given list of numbers.
numLst=[11,4,66,101,-5,-3,501]
print('Numbers list is =',numLst)
print('Greatest Number is above the list is =',max(numLst))
	#Que:5 -> Write a python script to find the smallest number in a given list of numbers.
numLst=[11,4,66,101,-5,-3,501]
print('Numbers list is =',numLst)
print('Smallest Number is above the list is =',min(numLst))
	#Que:6 -> Write a python script to calculate the sum of elements in a given list of numbers.
lst1=[10,40,30,60,50]
print('Number list is =',lst1)
print('Sum of all numbers is above the list elements is =',sum(lst1))
	#Que:7 -> Write a python script to remove all non int values from a list.
lst=[20,10,'Hello','Python','MySirG',3+7j,5.45]
lst2=[ ]
print('Orginal list is =',lst)
for i in range(0,len(lst)):
	if type(lst[i])==int:
		lst2.append(lst[i])
print('Integer list is =',lst2)
#Que:8->Write a python script to print distinct(seprate) elements along with their frequencis of occurence in the list.
lst=[1,2,3,4,5,'Hello','Python',1,1,1,2,2,3,4,4,3,5,2,4,4,3,'Hello','Python','Python','Hello']
for i in range(len(set(lst))):
	 print(f'frequencis of {lst[i]} = {lst.count(lst[i])}')
#Que:9 -> Write a python script to print indices of all occurences of given element in a given list.
lst3=[10,20,30,'Hello','Python',10,20]
for i in range(0,len(lst3)):
	print(f'index {i} = {lst3[i]}')			
#Que:10 -> Write a python script to sort a list.
lst=[20,30,60,50,100,11]
print(lst)
print('Sorted in ascending order :',sorted(lst))
lst.sort(reverse=True)
print('Sorted in Descending order :',lst)
lst2=['Hello','Python','MySirG','Telusko','Abc','abc']
print('Sorted in ascending order :',sorted(lst2))
lst2.sort(reverse=True)
print('Sorted in descending order :',lst2)		