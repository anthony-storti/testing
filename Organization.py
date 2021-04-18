from typing import List
from System import System
from User import User

class Organization:
    organization_list = []

    def __init__(self, name: str, location: str, org_type: str, department: List[str]):
        self._name = name
        self._location = location
        self._org_type = org_type
        self._department = department
        self.organization_list.append(name)
        self.systems: List[System] = []
        self.users: List[User] = []

    def __del__(self):
        for i in self._department:
            self._department.remove(i)
        for i in self.organization_list:
            self.organization_list.remove(i)

    # Getters
    def get_org_name(self) -> str:
        return self._name

    def get_org_location(self) -> str:
        return self._location

    def get_org_type(self) -> str:
        return self._org_type

    def get_department(self) -> List[str]:
        return self._department

    # Setters
    def set_org_name(self, name: str):
        self._name = name

    def set_org_location(self, location: str):
        self._location = location

    def set_org_type(self, org_type: str):
        self._org_type = org_type

    def add_department(self, dep: str):
        self._department.append(dep)

    def remove_department(self, dep: str):
        self._department.remove(dep)

    def add_system(self, system: System):
        self.systems.append(system)

    def remove_system(self, system: System):
        self.systems.remove(system)

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, idx: int):
        return self.users[idx]

    def remove_user(self, user: User):
        self.users.remove(user)
