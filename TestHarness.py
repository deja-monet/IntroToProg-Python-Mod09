# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# dejam,220906:
#    - edited .append in for loop to append line instead of instances from Employee:
#       - error: 'Employee' object is not subscriptable
#       - solution: append line instead of specific locations from line (originally: Emp(line[0], line[1], line[2].strip()))
# ---------------------------------------------------------- #
#import modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp  #employee class only from DataClasses.py
    from ProcessingClasses import FileProcessor as Fp  #ProcessingClasses.py
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

#test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

#test processing module
Fp.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(line)
for row in lstTable:
    print(row.to_string(), type(row))

#test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())