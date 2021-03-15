from typing import List


class Organization:
    organization_list = []

    def __init__(self, name: str, location: str, org_type: str, department: List[str]):
        self._name = name
        self._location = location
        self._org_type = org_type
        self._department = department
        self.organization_list.append(name)

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

    def get_department(self) -> list[str]:
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
