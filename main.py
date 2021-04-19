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


for s in sys_list:
    print(s.get_system_name())


sys8.get_system_type()

sys1.get_username_list()

sys1.set_organization(org1.get_org_name())

usr1 = usr("Michal Scott", "Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr1.allocate_system("accounting")

usr2 = usr("Jim Halpert", "Sales Associate", 2, "Dunder Mifflin", True, list(), sys_list)

org2.add_user(usr2)

usr2.allocate_system("accounting")

print(sys1.get_username_list())

usr3 = usr("Dwight Shrute", "Assistant to the Regional Manager", 2, "Dunder Mifflin", True, list(), sys_list)

usr3.allocate_system("management")

print(sys6.get_username_list())

usr3.terminate()

org1.get_org_name()


