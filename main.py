from Organization import Organization as org
from System import System as sys
from User import User as usr
import main_helper as helper


divisions = ["accounting", "sales", "marketing", "shipping", "executive", "management", "BOD"]

org1 = org("Dunder Mifflin", "Scranton, PA", "Paper Sales", divisions)

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

print(f'systems created for {org1.get_org_name()}:')
for s in sys_list:
    print(s.get_system_name())

usr1 = usr("Michal Scott", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr2 = usr("Jim Halpert", "Sales Associate", 2, "Dunder Mifflin", True, list(), sys_list)

usr3 = usr("Dwight Shrute", "Assistant to the Regional Manager", 2, "Dunder Mifflin", True, list(), sys_list)


print(usr1.get_user_name())
usr1.allocate_system("accounting")

print(usr2.get_user_name())
usr2.allocate_system("accounting")

print(usr3.get_user_name())
usr3.allocate_system("management")

sys1.set_organization(org1.get_org_name())

print(f"{sys8.get_system_name()} type is {sys8.get_system_type()}")

print(f"System 1 users: {sys1.get_username_list()}")

print(f"System 6 users: {sys6.get_username_list()}")

print(usr3.get_user_name())
usr3.terminate()




