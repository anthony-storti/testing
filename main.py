from Organization import Organization as org
from System import System as sys
from User import User as usr
import main_helper as helper

divisions = ["accounting", "sales", "marketing", "shipping", "executive", "management", "BOD"]

org1 = org("Dunder Mifflin", "Scranton, PA", "Paper Sales", divisions)
org2 = org("Nakatomi Corporation", "Toyko Japan", "Investments", divisions)

sys1 = sys("", "", 0, 0, "")
sys2 = sys("", "", 0, 0, "")
sys3 = sys("", "", 0, 0, "")
sys4 = sys("", "", 0, 0, "")
sys5 = sys("", "", 0, 0, "")
sys6 = sys("", "", 0, 0, "")
sys7 = sys("", "", 0, 0, "")
sys_list = [sys1, sys2, sys3, sys4, sys5, sys6, sys7]

helper.init_system(org1, sys_list, sys1)
sys8 = sys("", "", 0, 0, "")
helper.init_system(org1, sys_list, sys8, "accounting")

for s in sys_list:
    print(s.get_system_name())

print(sys8.get_system_type())


# usr1 = usr("Dwight Shrute", "Assistant to the Regional Manager", 4, "", True, list())
#
# usr1.allocate_system(sys1)
# print(sys1.get_system_organization())
# print(org1.get_org_name())
# print(org1.get_org_location())
# print(org1.get_org_type())
# print(sys1.get_system_name())
# print(sys1.get_system_type())
# print(sys1.get_system_access_level())
# print(sys1.get_system_license_count())
# # print(usr1.get_user_name())
# # usr1.terminate()
# print(sys1.get_system_license_count())
