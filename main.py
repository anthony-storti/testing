from Organization import Organization as org
from System import System as sys
from User import User as usr
import main_helper as helper

divisions = ["accounting", "sales", "marketing", "shipping", "executive", "management", "BOD"]

org1 = org("Dunder Mifflin", "Scranton, PA", "Paper Sales", divisions)
org2 = org("Nakatomi Corporation", "Toyko Japan", "Investments", divisions)

# get 7 system objects into a list
sys1 = sys("", "", 0, 0, "", list())
sys2 = sys("", "", 0, 0, "", list())
sys3 = sys("", "", 0, 0, "", list())
sys4 = sys("", "", 0, 0, "", list())
sys5 = sys("", "", 0, 0, "", list())
sys6 = sys("", "", 0, 0, "", list())
sys7 = sys("", "", 0, 0, "", list())
sys_list = [sys1, sys2, sys3, sys4, sys5, sys6, sys7]

# user the helper function to filling the contents for the system list
helper.init_system(org1, sys_list, sys1)

# using a different way to filling out the contents for sys8 (different from sys1-7)
sys8 = sys("", "", 0, 0, "", list())
helper.init_system(org1, sys_list, sys8, "accounting")

# print out the system for the system list after having some actual contents
for s in sys_list:
    print(s.get_system_name())

# print out the actual content for sys8
print(sys8.get_system_type())

# get username for system 1
print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

# user objects to allocate the system with different departments

# test case 1: assign user1 to the same department system twice
# expect result: it does not let the user to assign the same department system twice
usr1 = usr("Dwight Shrute", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr1.allocate_system("accounting")

usr2 = usr("Dwight Shrute", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr2.allocate_system("accounting")

# display result for test case 1:
print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

# test case 2: assign the same user(usr1) to a two different department system
# expect result: it should allow the user to do it
# usr1 is assigned to the department accounting already in code line 45
usr3 = usr("Dwight Shrute", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr3.allocate_system("management")

# display the result for test case 2
print("\nusername that assigned to system 6:")
print(sys6.get_username_list())

# test case 3: assign a different user to accounting system
# expect result: the accounting system allows max 2 people for access, so it should grand access
usr4 = usr("Harry Potter", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr4.allocate_system("accounting")

# display result for test case 3
print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

# test case 4: assign a different user to account system  again
# expect result: the access should deny, since there are already two users accessing the accounting system now
usr5 = usr("Tomas Edison", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr5.allocate_system("accounting")

# test case 5: assign a different user to accounting system who does not have the privilege to access it
# expect result: the access should be denied
usr0 = usr("Ben J", "Cooker", 5, "Dunder Mifflin", True, list(), sys_list)

usr0.allocate_system("accounting")

# test case 6: manually de-allocate the usr1 from account to see if his name is still on the list
# expect result: usr1 is not on the list anymore
usr1.de_allocate_system('accounting')

# display result for test case 6
print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

# test case 7: allocate usr1 to a department that does not exist
# expect result: it will display a "system not found!" sentences
usr1.allocate_system("Financial")

# test case 8: terminate automatically de-allocate users from their current working department, it is different
#              from the test case 6, because it is automatically not manually
# expect result: the list of working department for accounting should no longer has usr1's name after usr1 de-allocated
# terminates the usr1, usr2, and usr3, which is the users with the same name
# allocate the usr1 to the accounting system again to make usr1 allocates to the accounting system again
usr1.allocate_system("accounting")

usr1.terminate()

usr2.terminate()

usr3.terminate()

# display result for test case 8
print(sys1.get_username_list())
print(sys6.get_username_list())

# terminates the other users and end the process
usr4.terminate()
usr5.terminate()
usr0.terminate()