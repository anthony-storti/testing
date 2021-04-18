from Organization import Organization as org
from System import System as sys
from User import User as usr
from typing import List

# implementing a psydo overriding function with two different ways to initialize the system


def init_system(o: org, sy: List[sys], sy1: sys, s_str="null"):
    if s_str == "null":
        for i in range(len(sy)):
            if o.get_department()[i] == "accounting":
                sy[i].set_system_name("accounting")
                sy[i].set_system_type("accountancy")
                sy[i].set_system_access_level(3)
                sy[i].set_system_license_count(2)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(2)
            elif o.get_department()[i] == "sales":
                sy[i].set_system_name("sales")
                sy[i].set_system_type("sealer")
                sy[i].set_system_access_level(4)
                sy[i].set_system_license_count(5)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(5)
            elif o.get_department()[i] == "marketing":
                sy[i].set_system_name("marketing")
                sy[i].set_system_type("marketer")
                sy[i].set_system_access_level(4)
                sy[i].set_system_license_count(5)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(5)
            elif o.get_department()[i] == "shipping":
                sy[i].set_system_name("shipping")
                sy[i].set_system_type("shipper")
                sy[i].set_system_access_level(5)
                sy[i].set_system_license_count(10)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(10)
            elif o.get_department()[i] == "executive":
                sy[i].set_system_name("executive")
                sy[i].set_system_type("executor")
                sy[i].set_system_access_level(4)
                sy[i].set_system_license_count(5)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(5)
            elif o.get_department()[i] == "management":
                sy[i].set_system_name("management")
                sy[i].set_system_type("manager")
                sy[i].set_system_access_level(2)
                sy[i].set_system_license_count(5)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(5)
            elif o.get_department()[i] == "BOD":
                sy[i].set_system_name("BOD")
                sy[i].set_system_type("BOD_border")
                sy[i].set_system_access_level(1)
                sy[i].set_system_license_count(2)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(2)
            else:
                sy[i].set_system_name(o.get_department()[i])
                sy[i].set_system_type(o.get_department()[i])
                sy[i].set_system_access_level(5)
                sy[i].set_system_license_count(10)
                sy[i].set_organization(o.get_org_name())
                sy[i].set_max_license_number(10)

    else:
        if s_str == "accounting":
            sy1.set_system_name("accounting")
            sy1.set_system_type("accountancy")
            sy1.set_system_access_level(3)
            sy1.set_system_license_count(2)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(2)
        elif s_str == "sales":
            sy1.set_system_name("sales")
            sy1.set_system_type("sealer")
            sy1.set_system_access_level(4)
            sy1.set_system_license_count(5)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(5)
        elif s_str == "marketing":
            sy1.set_system_name("marketing")
            sy1.set_system_type("marketer")
            sy1.set_system_access_level(4)
            sy1.set_system_license_count(5)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(5)
        elif s_str == "shipping":
            sy1.set_system_name("shipping")
            sy1.set_system_type("shipper")
            sy1.set_system_access_level(5)
            sy1.set_system_license_count(10)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(10)
        elif s_str == "executive":
            sy1.set_system_name("executive")
            sy1.set_system_type("executor")
            sy1.set_system_access_level(4)
            sy1.set_system_license_count(5)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(5)
        elif s_str == "management":
            sy1.set_system_name("management")
            sy1.set_system_type("manager")
            sy1.set_system_access_level(2)
            sy1.set_system_license_count(5)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(5)
        elif s_str == "BOD":
            sy1.set_system_name("BOD")
            sy1.set_system_type("BOD_border")
            sy1.set_system_access_level(1)
            sy1.set_system_license_count(2)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(2)
        else:
            sy1.set_system_name(s_str)
            sy1.set_system_type(s_str)
            sy1.set_system_access_level(5)
            sy1.set_system_license_count(10)
            sy1.set_organization(o.get_org_name())
            sy1.set_max_license_number(10)