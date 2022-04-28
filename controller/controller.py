from platform import node
from models.Node import *
from models.LinkedList import *

def initialize_list():
    my_list = LinkedList()
    return my_list

######################################################### Insert at start and end #########################################################
def reg_country_start_list(self,data):
    LinkedList.insert_at_start(self,data)
    return get_elements(self)

def reg_country_end_list(self,data):
    LinkedList.insert_at_end(self,data)
    return get_elements(self)


################################################ Insert next to an item and before an item ###############################################

def reg_country_after_item(self,x,data):
    LinkedList.insert_after_item(self,x,data)
    return get_elements(self)

def reg_country_before_item(self,x,data):
    LinkedList.insert_before_item(self,x,data)
    return get_elements(self)


######################################################### Insert at index #########################################################

def reg_country_at_index(self,index,data):
    LinkedList.insert_at_index(self,index,data)
    return get_elements(self)


######################################################### Count the elements of the list #########################################################
def count_elements(self):
    return LinkedList.get_count(self)


######################################################### search country on the list #########################################################
def search_country(self,x):
    return LinkedList.search_item(self,x)


######################################################### delete first or last element of the list of countrys #########################################################
def delete_first_country(self):
    n:Node = self.start_node
    if n is not None:
        country:str = str(n.item)
        LinkedList.delete_at_start(self)
        return country
    else:
        LinkedList.delete_at_start(self)

def delete_last_country(self):
    n:Node = self.start_node
    last_n_item = LinkedList.get_last_node(self)
    if n is not None:
        country:str = str(last_n_item)
        LinkedList.delete_at_end(self)
        return country
    else:
        LinkedList.delete_at_end(self)


######################################################### delete element by value passed #########################################################
def delete_country_passed(self,x):
    return LinkedList.delete_element_by_value(self,x)
    

######################################################### Extra functions #########################################################
# Instead of using the function named "traverse_list" that is in the class of name "LinkedList" that 
# is on models I created this where I return the list of countries and print it in the view so that 
# the prints are exclusively in the view
def get_elements(self):
    elements:list = []
    n:Node = self.start_node
    while True:
        elements.append(n.item)
        if n.ref is None:
            return elements
        n = n.ref

    
