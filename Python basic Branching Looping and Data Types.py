#!/usr/bin/env python
# coding: utf-8

# # Python Basic Commands That You Should know.
Shift + Enter --> Excute Code
Shift + Tab --> Help Code
↑ To change the cell position 
Heading --> To give A Heading 
Raw NB Conver --> Code which is not going to excute
markdown --> Added as an comment
# # Variable Sustitution
%d to sustitute value for integer (int)
%f to sustitute value for Float (float)
%s to sustitute value for String  (str)
# In[9]:


#Example 1: Assigning values to the Variables
A = 10
B = 20.4548
C = "Rahul Lohar"
print(" Value of Variable A : %d \n Value of Variable B : %f \n Value of Variable C : %s \n "%(A,B,C))


# In[12]:


#Example 2: Float Value modification
# you can specify after the decimal value how much digits should display.
# %.3f Deines only 3 digits should get display like this you can modify it.
B = 20.4548
print("%.3f"%B)


# In[11]:


#Example 3: Taking user inputs to assign values to user

A = int(input("Enter the Integer value you want : \n"))
B = float(input("Enter the Float value you want : \n"))
C = input("Enter the String value you want : \n")
print("\n Value of Variable A : %d \n Value of Variable B : %f \n Value of Variable C : %s \n "%(A,B,C))


# In[13]:


# # Problem statment: Write a program which will add two numbers and print the sum
A = int(input("Enter the Integer value you want : \n"))
B = float(input("Enter the Float value you want : \n"))
print("The addition of the int and float number is : %.3f"%(A+B))


# # Conditional Statements.....

# # If Elseif Else.........

# In[15]:


# # # Problem statment: Write a program which will identify the Even or ODD number
No = int(input("Enter the value you want : \n"))
if(No%2 == 0):
    print("The %d is Even number"%No)
else:
    print("The %d is Odd number"%No)    


# In[17]:


#WAP TO CALCULATE TAX

#0-2L --> tax 0%
#2-5L --> tax 10%
#5-10L --> tax 20%
#10L+ --> 30%

sal = input("Enter your salary")
sal = int(sal)
i = sal
if(i>0 and i<=200000):
    tax-=0
elif(i>200000 and i<=500000):
    tax=0.1*(i-200000)
elif(i>500000 and i<=1000000):
    tax=(0.1*300000) + 0.2*(i-500000)
else:
    tax=(0.1*300000)+(0.02*500000)+0.3*(i-1000000)
print("The total tax for %f salary is %f"%(i,tax))


# In[2]:


# WAP TO FIND FAV DISH STATE WISE
print(" Maharashtra : MH \n Gujrat : GJ \n MadhyaPradesh : MP \n Punjab : PJ \n ")

State=input("Please Enter your state from above : ")
if (State == "MH"):
    print("Our fav dish is Misal pav and VADAPAV")
elif (State == "GJ"):
    print("Our fav dish is Dhokla ")
elif (State == "MP"):
    print("Our fav dish is JILEBI ")
elif (State == "PJ"):
    print("Our fav dish is PAATHA")
else:
    print("I Think you r not from this planet")


# # DATA TYPES IN PYTHON

# # 1.1 List
Python List

Lists are just like the arrays, declared in other languages. Lists need not be homogeneous always which makes it a most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.

Method	    Description
--------------------------------------------------------
append() --->  Adds an element at the end of the list
clear()	 --->  Removes all the elements from the list
copy()	 --->  Returns a copy of the list
count()	 --->  Returns the number of elements with the specified value
extend() --->  Add the elements of a list (or any iterable), to the end of the current list
index()	 --->  Returns the index of the first element with the specified value
insert() --->  Adds an element at the specified position
pop()	 --->  Removes the element at the specified position
remove() --->  Removes the item with the specified value
reverse() ---> Reverses the order of the list
sort()	--->   Sorts the list
del List -->   to delete the list
# In[5]:


#Example
#Create a List

My_List = [123,"Rahul Lohar","sec 26 plot 141 nigdi pradhikaran","O+"]


# In[6]:


My_List


# In[7]:


# Accessing elemnts within the list 
#index()	 --->  Returns the index of the first element with the specified value
My_List[0]


# In[8]:


#index()	 --->  Returns the index of the first element with the specified value
My_List[3]


# In[9]:


# find out the lenghth of the List

len(My_List)


# In[15]:


# append() --->  Adds an element at the end of the list
# appended rahul for 3 times.

My_List.append("Rahul")


# In[16]:


My_List


# In[17]:


#count()	 --->  Returns the number of elements with the specified value

My_List.count("Rahul")


# In[26]:


#Join Two Lists
#By using unary operator such as +
#or By Using Extend() function

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print("Using + operator joined the two list.\n")
print(list3)

# now we will join this two list using extend function

list1.extend(list2)
print("\n Using Extend() function joined the two list.\n")
print(list1)


# In[37]:


# insert() --->  Adds an element at the specified position
# Syntax is :- insert(postion,element)

Fruits = ["apple", "banana", "cherry"]
print("Before inserting the fruit the list is : \n\n",Fruits)

Fruits.insert(3,"Jackfruit")
print("\n After inserting the fruit at postion 3 in the list is : \n\n",Fruits)


# In[42]:


# reverse() ---> Reverses the order of the list

No = [99,98,97,67,2,12]
print("Before reversing the No list is : \n\n",No)
No.reverse()
print("\nAfter reversing the No list is : \n\n",No)


# In[74]:


# sort()	--->   Sorts the list
No = [99,98,97,67,2,12]
print("Before Sorting the No list is : \n\n",No)
No.sort()
print("\nAfter Sorting the No list is : \n\n",No)


# In[85]:


# pop()	 --->  Removes the element at the specified position
# if we dont give any position then pop will automatically remove the last element.

Fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Before poping the fruit from list is : \n\n",Fruits)
popelement = Fruits.pop(0)
popelement1 = Fruits.pop()
print("\n The elemnt which has been poped out at 0th given position is : ",popelement)
print("\n Poping last elemt if index is not mention : ",popelement1)
print("\n After poping the fruit from list is : \n\n",Fruits)


# In[105]:


# remove() --->  Removes the item with the specified value

Fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Before poping the fruit from list is : \n\n",Fruits)
Fruits.remove("apple")
print("\n After poping the fruit from list is : \n\n",Fruits)


# In[113]:


# clear()	 --->  Removes all the elements from the list
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\n Before clearing the list is : \n\n",List)
List.clear()
print("\n After clearing the list is : ",List)


# In[150]:


# del List -->   to delete the list

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\n Before deleting the list is : \n\n",List)
del List
print("\n The list is deleted : \n\n If you try to print the list you will get the comented error message. ")

# ERROR MESSAGE:- 
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-122-f7d977c26113> in <module>
#       3 del List
#       4 print("\n The list is deleted : \n\n If you try to print the list you will get the below error message. ")
# ----> 5 print(List)

# NameError: name 'List' is not defined*/


# In[149]:


# copy()	 --->  Returns a copy of the list

List_1 = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
List_2 = []
print("\n Before Copying the list_1 is : \n\n",List_1)
print("\n Before Copying the list_2 is : ",List_2)
List_2 = List_1.copy()
print("\n After Copying the list_1 to List_2 is : \n\n",List_2)


# # 1.1.1 Multi-Dimensional List:  
Multi-dimensional lists in Python
There can be more than one additional dimension to lists in Python. 
Keeping in mind that a list can hold other lists, that basic principle can be applied over and over. 
Multi-dimensional lists are the lists within lists. Usually, a dictionary will be the better choice rather than a multi-dimensional list in Python.

For Multi-Dimensional rest function are the same.
# In[151]:


# Python program to demonstrate printing 
# of complete multidimensional list 
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
print(a) 


# In[166]:


# Assessing elemnts with in Multi-Dimensional List
a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
for i in range(len(a)):
    print("List : %d : "%i,a[i])


# # 1.2 Tuples in Python
Tuples in Python
A Tuple is a collection of Python objects separated by commas. A tuple in Python is similar to a list. 
The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas, in a list, elements can be changed.
In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.Python has two built-in methods that you can use on tuples.

Method	--> Description
count()	--> Returns the number of times a specified value occurs in a tuple
index()	--> Searches the tuple for a specified value and returns the position of where it was found
# In[174]:


#Create a Tuple:

My_tuple = ("apple", "banana", "cherry","apple","apple","apple")
print(My_tuple)


# In[176]:


My_tuple.index("apple")


# In[177]:


My_tuple.count("apple")


# # 1.3 Dictionary in Python
What is dictionary in Python?
Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.

Dictionaries are optimized to retrieve values when the key is known.

In Python dictionaries are written with curly brackets, and they have keys and values.Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	--> Description
clear()	--> Removes all the elements from the dictionary
copy()	--> Returns a copy of the dictionary
fromkeys()	--> Returns a dictionary with the specified keys and value
get()	--> Returns the value of the specified key
items()	--> Returns a list containing a tuple for each key value pair
keys()	--> Returns a list containing the dictionary's keys
pop()	--> Removes the element with the specified key
popitem()	--> Removes the last inserted key-value pair
setdefault() --> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	--> Updates the dictionary with the specified key-value pairs
values()    --> Returns a list of all the values in the dictionary
# In[184]:


# Declaration of Dictionary
# Syntax:-
# My_Dictionary = {Key:value,Key:value,Key:value}
My_Dictionary = {"Name":"Rahul","Surname":"Lohar","Address":"Nigdi pradhikaran","ZipCode":411044,"DOB":"20/05/1997"}
print(My_Dictionary)


# In[189]:


# Accessing the elements with in the Dictionary

# Accessing the elements with in the Dictionary using "Key"
My_Dictionary["Name"]


# In[190]:


# get()	--> Returns the value of the specified key
My_Dictionary.get("Surname")


# In[191]:


# values()    --> Returns a list of all the values in the dictionary
My_Dictionary.values()


# In[193]:


# keys()	--> Returns a list containing the dictionary's keys
My_Dictionary.keys()


# In[260]:


# fromkeys()	--> Python dictionary method fromkeys() creates a new dictionary with keys from iterable and values set to value.
# Syntax:- 
# dict.fromkeys(Iterable,value)
# Parameters
# Iterable − This can be a List,range or tupple which can be play a role as Keys of the dictionary.
# value − This is optional, if provided then value would be set to this value
# This method returns the dictionary.

rahul = [1,2,3,4,5]
My_Dictionary_Using_list = dict.fromkeys(rahul)
print("New Dictionary is created using list as a key")
print("New Dictionary : %s"%str(My_Dictionary_Using_list))
My_Dictionary_Using_list = dict.fromkeys(rahul,10)
print("\nNew Dictionary is created using list as a key and values is pass to all is 10")
print("New Dictionary : %s"%str(My_Dictionary_Using_list))

# I have assihgn the values to the My_Dictionary_Using_list using for loop
for i in range(1,6):
    My_Dictionary_Using_list[i]=i
print("\nNew Dictionary is created using for loop")
print("New Dictionary : %s"%str(My_Dictionary_Using_list))


# In[308]:


# setdefault() --> Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

My_Dictionary2 = My_Dictionary.setdefault("DOB")
My_Dictionary2


# In[265]:


#  items()	--> Returns a list containing a tuple for each key value pair

# The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
# The view object will reflect any changes done to the dictionary, see example below

My_Dictionary.items()


# In[294]:


# update()	--> Updates the dictionary with the specified key-value pairs
My_Dictionary ={'Name': 'Rahul',
 'Surname': 'Lohar',
 'Address': 'Nigdi pradhikaran',
 'ZipCode': 411044,
 'DOB': '20/05/1997',
 'Boold Gruop': 'O+'}

print("Before update the blood group \n",My_Dictionary)

My_Dictionary.update({"Boold Gruop":"B+"})

print("\n After update the blood group",My_Dictionary)


# In[302]:


# copy()	--> Returns a copy of the dictionary

MyDCtionary_1 ={}
print("Empty dictionary : ",MyDCtionary_1)
MyDCtionary_1 = My_Dictionary.copy()
print("Copied dictionary : \n",MyDCtionary_1)


# In[303]:


# pop()	--> Removes the element with the specified key

print("Before Pop dictionary : ",MyDCtionary_1)
MyDCtionary_1.pop("DOB")
print("\nAfter Pop dictionary : \n",MyDCtionary_1)


# In[304]:


# popitem()	--> Removes the last inserted key-value pair
print("Before Pop dictionary : ",MyDCtionary_1)
MyDCtionary_1.popitem()
print("\nAfter Pop dictionary : \n",MyDCtionary_1)


# In[305]:


# clear()	--> Removes all the elements from the dictionary

print("Before Clear dictionary : ",MyDCtionary_1)
MyDCtionary_1.clear()
print("\nAfter Clear dictionary : \n",MyDCtionary_1)

