#Que:1-> Write a python program to store all programing languages known to you using set.
language={'Python','Java','C','C++'}
print('Known programming languages:',language)
#Que:2 -> Write a python program to store your information .{name, age , gender, so on.}
intro={'Kartik',21,'Male','Graduate'}
print('My short intro is :',intro)
#Que:3 -> Write a python program to get the data type of the set.
print('Data type is :',type(intro))
#Que:4 -> Write a python script to find if "Python" is present in the set thisset={"Java","Python","Django"}
thisset={"Java","Python","Django"}
print("Python is Present in the given set.") if "Python" in  thisset else print("Python is not prsent in the given set.")
#Que:5 -> Write a python program to add items from another set to the current set. thisset={"Java","Python","SQL"} secondset={"C","Cpp","NoSQL"}
thisset={"Java","Python","SQL"} 
secondset={"C","Cpp","NoSQL"}
thisset.update(secondset)
print('New set is :',thisset)
#Que:6 -> Write a python program to add elements of list to a set.
st={1,2,3,4,5}
st.update(["Hello","Python","MySirG","iNeuron"])
print(st)
#Que:7 -> Write a python program to remove the last item of the given set thisset={"Python","Django","Javascript","SQL"} 
thisset={"Python","Django","Javascript","SQL"}
thisset.pop()
print('New Set is :',thisset)
#Que:8 -> Write a python program to delete the set completely.
st2={"Python","Django","Javascript","SQL"}
del st2 # using del keyword we can delete the setObject completely.
#Que:9 -> Write a python program to loop through the set and print values. thisset={"Python","Django","Javascript","SQL"} 
thisset={"Python","Django","Javascript","SQL"} 
for i in thisset:
	print(i,end=' ')
#Que:10 -> Write a python program to find the maximum and minimum value in a set.	
st2={10,29,5,67,101,21,5}
st3={'ABC','Hello','Python','Java','java','python','django'}
print()
print('Maximum value is =',max(st2))
print('Minimum value is =',min(st2))
print('Maximum value is (in string set) =',max(st3))
print('Minimum value is (in string set) =',min(st3))