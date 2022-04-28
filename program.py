import sys
import view.view as view
sys.stdout.reconfigure(encoding='UTF-8')
# This program has the objective of the user to be able to insert in a list the countries 
# he wants and to be able to do in that same list several operations, such as, for example, 
# insert a country at the beginning of the list or at the end and even delete a country from 
# the list through its name .

if __name__ == '__main__':
    view.main() # Invoking the main method found in the "view" file