"""
Purpose:- to perform list operations
Author:- Rahul Lohar
Date:- 27/04/2020
"""

class ListOps:
    '''
    this class contains list operations function
    '''
    my_list = []
    def createlist(self):
        '''
        To create the list
        '''
    number = int(input("Enter how many elements you wnto add"))
    for i in range(0, number):
        lst_ele = int(input("\n Enter List Elements : "))
        my_list.append(lst_ele)
    def showlist(self):
        """
        To show the list
        """
        print("The list elements are :- ", self.my_list)
    def remelelist(self):
        """
        To remove elements in the list
        """
        self.my_list.pop()
        print("The list elements is been removed :- ", self.my_list)
    def updatelist(self):
        """
        To add elements in the list
        """
        lst_ele = input("\n Enter List Elements you want to add: ")
        self.my_list.append(lst_ele)
    def insertatspecificloclist(self):
        """
        To insert elementsat specific location in the list
        """
        pos_ele = int(input("\n Enter List Elements position: "))
        lst_ele = int(input("\n Enter List Elements you want to add: "))
        self.my_list.insert(pos_ele, lst_ele)

class Userwish(ListOps):
    '''
    to handele user options
    '''
    def user_options(self):
        '''
        To take user option in the list
        '''
        operations = {
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
        '''
        To take user want to continew or not the list
        '''
        ans = input("would you like to continew Y/N")
        if ans == "Y":
            self.user_options()
        else:
            print("\n Thank you !")
        