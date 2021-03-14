from Organization import Organization as org
from System import System as sys
from User import User as usr

org1 = org("Dunder Mifflin", "Scranton, PA", "Paper Sales")
org2 = org("Nakatomi Corporation", "Toyko Japan", "Investments")
sys1 = sys("Windows", "Operating System", 1, 5, list())
usr1 = usr("Dwight Shrute", "Assistant to the Regional Manager", 4, list(), True, list())
sys1.add_system_organization(org1)
sys1.add_system_organization(org2)
usr1.add_user_organizations(org1)
usr1.add_user_assigned_systems(sys1)
print(sys1.get_system_organization())
print(org1.get_business_name())
print(org1.get_business_location())
print(org1.get_business_type())
print(sys1.get_system_name())
print(sys1.get_system_type())
print(sys1.get_system_access_level())
print(sys1.get_system_license_count())
orgs = sys1.get_system_organization()
for org in orgs:
    print(org.get_business_name())
jobs = usr1.get_user_organizations()
print(usr1.get_user_name())
for job in jobs:
    print(job.get_business_name())
print(sys1.get_system_license_count())
usr1.terminate()
print(sys1.get_system_license_count())
