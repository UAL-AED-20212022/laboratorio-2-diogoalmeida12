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


######################################################### Insert next to an item and before an item #########################################################

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


######################################################### Extra functions #########################################################

def get_elements(self):
    elements:list = []
    n:Node = self.start_node
    while True:
        elements.append(n.item)
        if n.ref is None:
            return elements
        n = n.ref

    
