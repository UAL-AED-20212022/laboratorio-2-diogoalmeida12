from controller.controller import *

def main():     
    #Create the main variables
    my_list = initialize_list()
    while True:
        try:
            commands:list[str] = input().strip().split() # Gets the list of parameters given by the user
        except EOFError:
            return
        
        if commands[0] == "RPI":
            RPI(my_list,commands[1])
        elif commands[0] == "RPF":
            RPF(my_list,commands[1])
        elif commands[0] == "RPDE":
            RPDE(my_list,commands[2],commands[1])
        elif commands[0] == "RPAE":
            RPAE(my_list,commands[2],commands[1])
        elif commands[0] == "RPII":
            RPII(my_list,int(commands[2]),commands[1])

def RPI(my_list,data):   
    for n in reg_country_start_list(my_list,data):
        print(n)

def RPF(my_list,data):   
    for n in reg_country_end_list(my_list,data):
        print(n)

def RPDE(my_list,x,data):   
    for n in reg_country_after_item(my_list,x,data):
        print(n)

def RPAE(my_list,x,data):   
    for n in reg_country_before_item(my_list,x,data):
        print(n)

def RPII(my_list,index,data):   
    for n in reg_country_at_index(my_list,index,data):
        print(n)
    
    