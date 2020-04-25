#!/usr/bin/env python
# coding: utf-8

# In[121]:


"""
Documentation:- 

This is simple program that performs certain operation related to the List.
The key terms used in this program are:-
    1. class and objects
    2. self keyword
    3. inheritance
    4. superfunction
    5. list operations

Execution of the program:- 

lo =ListOperations()
opt = Userwish()
lo.CreateList()
opt.user_options()

"""

class ListOperations:
    my_list = []
    
    def CreateList(self):
        N = int(input("Enter how many elements you wnto add"))
        for i in range(0,N):
            lst_ele =int(input("\n Enter List Elements : "))
            self.my_list.append(lst_ele)
    def showlist(self):
        print("The list elements are :- ",self.my_list)
    def remelelist(self):
        self.my_list.pop()
        print("The list elements is been removed :- ",self.my_list)
    def updatelist(self):
        lst_ele =input("\n Enter List Elements you want to add: ")
        self.my_list.append(lst_ele)
    def insertatspecificloclist(self):
        pos_ele =int(input("\n Enter List Elements position: "))
        lst_ele =int(input("\n Enter List Elements you want to add: "))
        self.my_list.insert(pos_ele,lst_ele)

class Userwish(ListOperations):
        def user_options(self):
            operations={
                    1:"Dispaly Number of Elemnts In The List",
                    2:"Remove Element From The List",
                    3:"Add New Element To The List",
                    4:"Add New Element To specificlocation in the List"}
            print(operations)
            user_option = int(input("\n what operation would you like to perform"))
            if user_option == 1:
                super().showlist()
            elif user_option == 2:
                super().remelelist()
            elif user_option == 3:
                super().updatelist()
            elif user_option == 4:
                super().insertatspecificloclist()
            else:
                print("\n Sorry you have selected wrong option: \n please try Again !")
            self.finalans()
    
        def finalans(self): 
            A = input("would you like to continew Y/N")
            if(A == "Y"):
                self.user_options()
            else:
                print("\n Thank you !")
                
"""
Output:- 
lo.CreateList()

Enter how many elements you wnto add3

 Enter List Elements : 1

 Enter List Elements : 2

 Enter List Elements : 3
 
opt.user_options()
{1: 'Dispaly Number of Elemnts In The List', 2: 'Remove Element From The List', 3: 'Add New Element To The List', 4: 'Add New Element To specificlocation in the List'}

 what operation would you like to perform3

 Enter List Elements you want to add: 2
would you like to continew Y/NY
{1: 'Dispaly Number of Elemnts In The List', 2: 'Remove Element From The List', 3: 'Add New Element To The List', 4: 'Add New Element To specificlocation in the List'}

 what operation would you like to perform1
The list elements are :-  [1, 2, 3, '2']
would you like to continew Y/NY
{1: 'Dispaly Number of Elemnts In The List', 2: 'Remove Element From The List', 3: 'Add New Element To The List', 4: 'Add New Element To specificlocation in the List'}

 what operation would you like to perform3

 Enter List Elements you want to add: 12 34
would you like to continew Y/NY
{1: 'Dispaly Number of Elemnts In The List', 2: 'Remove Element From The List', 3: 'Add New Element To The List', 4: 'Add New Element To specificlocation in the List'}

 what operation would you like to perform1
The list elements are :-  [1, 2, 3, '2', '12 34']
would you like to continew Y/NN

 Thank you !
 
"""


# In[122]:


lo =ListOperations()


# In[123]:


opt = Userwish()


# In[124]:


lo.CreateList()


# In[125]:


opt.user_options()

