from Organization import Organization as org
from typing import List

class System:
    def __init__(self, name: str, type: str, access_level: int, license_count: int, organizations: str):
        self._name = name
        self._type = type
        self._access_level = access_level
        self._license_count = license_count
        self._organizations = organizations

    def get_system_name(self) -> str:
        return self._name

    def get_system_type(self) -> str:
        return self._type

    def get_system_access_level(self) -> int:
        return self._access_level

    def get_system_license_count(self) -> int:
        return self._license_count

    def get_system_organization(self) -> str:
        return self._organizations

    def set_system_name(self, name: str):
        self._name = name

    def set_system_type(self, type: str):
        self._type = type

    def set_system_access_level(self, access_level: int):
        self._access_level = access_level

    def set_system_license_count(self, license_count: int):
        self._license_count = license_count

    def set_organization(self, org1: str):
        self._organizations = org1

