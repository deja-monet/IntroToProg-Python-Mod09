# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# dejam,220906,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from ProcessingClasses import FileProcessor as Fp  #ProcessingClasses.py
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

file_name_str = "EmployeeData.txt"
list_of_rows = []
#Main Body of Script  ---------------------------------------------------- #

#load data from file into a list of employee objects when script starts
employee_objects_list = Fp.read_data_from_file(file_name = file_name_str)

while(True):
    #show main menu to user
    Eio.print_menu_items()
    
    #get user's menu option choice
    user_choice = Eio.input_menu_options()
    
    #show user current data in the list of employee objects
    if(user_choice.strip() == "1"):
        Eio.print_current_list_items(list_of_rows=employee_objects_list)
        continue
    
    #let user add data to the list of employee objects
    if(user_choice.strip() == "2"):
        try:
            employee_data = Eio.input_employee_data()
            employee_objects_list.append(employee_data)
        except UnboundLocalError:
            print("Something went wrong with the input!")
        continue
    
    #let user save current data to file
    if(user_choice.strip() == "3"):
        Fp.save_data_to_file(file_name=file_name_str, list_of_objects=employee_objects_list)
        print("Your data has been saved!")
        continue
    
    #let user exit program
    if(user_choice.strip() == "4"):
        print("Exit script!")
        break
#Main Body of Script  ---------------------------------------------------- #
