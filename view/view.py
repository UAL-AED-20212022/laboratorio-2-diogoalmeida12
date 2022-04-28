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
        elif commands[0] == "VNE":
            VNE(my_list)
        elif commands[0] == "VP":
            VP(my_list,commands[1])
        elif commands[0] == "EPE":
            EPE(my_list)
        elif commands[0] == "EUE":
            EUE(my_list)
        elif commands[0] == "EP":
            EP(my_list,commands[1])

# Then we have the functions that perform all the necessary prints and invoke all the controller functions 
# that aim to perform what was requested in the statement.
def RPI(my_list,data):   
    show_elements_list(reg_country_start_list(my_list,data))

def RPF(my_list,data):   
    show_elements_list(reg_country_end_list(my_list,data))

def RPDE(my_list,x,data):   
    show_elements_list(reg_country_after_item(my_list,x,data))

def RPAE(my_list,x,data):   
    show_elements_list(reg_country_before_item(my_list,x,data))

def RPII(my_list,index,data):   
    show_elements_list(reg_country_at_index(my_list,index,data))

def VNE(my_list):
   print(f"O número de elementos são {str(count_elements(my_list))}.")

def VP(my_list,x):
    value:bool = search_country(my_list,x)
    if value is True: 
        print(f"O país {x} encontra-se na lista.") 
    elif value is False:
        print(f"O país {x} não se encontra na lista.")

def EPE(my_list):
    value = delete_first_country(my_list)
    if value is not None:
        print(f"O país {value} foi eliminado da lista.")

def EUE(my_list):
    value = delete_last_country(my_list)
    if value is not None:
        print(f"O país {value} foi eliminado da lista.")

def EP(my_list,data):
    value:bool = search_country(my_list,data)
    if value is True:
        delete_country_passed(my_list,data)
        print(f"O país {data} foi eliminado da lista.")
    elif value is False:
        print(f"O país {data} não se encontra na lista.")
        

############## Extra function #################
def show_elements_list(lista):
    for a in lista:
        print(a)
    