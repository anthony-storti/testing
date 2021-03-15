from Organization import Organization as org
from System import System as sys
from User import User as usr
import main_helper as helper

divisions = ["accounting", "sales", "marketing", "shipping", "executive", "management", "BOD"]

org1 = org("Dunder Mifflin", "Scranton, PA", "Paper Sales", divisions)
org2 = org("Nakatomi Corporation", "Toyko Japan", "Investments", divisions)

sys1 = sys("", "", 0, 0, "", list())
sys2 = sys("", "", 0, 0, "", list())
sys3 = sys("", "", 0, 0, "", list())
sys4 = sys("", "", 0, 0, "", list())
sys5 = sys("", "", 0, 0, "", list())
sys6 = sys("", "", 0, 0, "", list())
sys7 = sys("", "", 0, 0, "", list())
sys_list = [sys1, sys2, sys3, sys4, sys5, sys6, sys7]

helper.init_system(org1, sys_list, sys1)
sys8 = sys("", "", 0, 0, "", list())
helper.init_system(org1, sys_list, sys8, "accounting")

for s in sys_list:
    print(s.get_system_name())

print(sys8.get_system_type())

print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

usr1 = usr("Dwight Shrute", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr1.allocate_system("accounting")

usr2 = usr("Dwight Shrute", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr2.allocate_system("accounting")

usr3 = usr("Dwight Shrute", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr3.allocate_system("management")

usr4 = usr("Harry Potter", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr4.allocate_system("accounting")

usr5 = usr("Tomas Edison", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr5.allocate_system("accounting")

usr0 = usr("Ben J", "Cooker", 5, "Dunder Mifflin", True, list(), sys_list)

usr0.allocate_system("accounting")

print("\nusername that assigned to system 6:")
print(sys6.get_username_list())

print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

usr1.de_allocate_system('accounting')

print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

usr1.allocate_system("accounting")

print("\nusername that assigned to system 1:")
print(sys1.get_username_list())

usr1.allocate_system("Financial")

usr1.terminate()

usr2.terminate()

usr3.terminate()

print(sys1.get_username_list())
