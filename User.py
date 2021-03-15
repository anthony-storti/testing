from Organization import Organization as org
from System import System as sys
from typing import List

class User:

    def __init__(self, name: str, role: str, privilege: int, organizations: List[org], online: bool, assigned_systems: List[sys]):
        self._name = name
        self._role = role
        self._privilege_level = privilege
        self._organizations = organizations
        self._online = online
        self._assigned_systems = assigned_systems

    def get_user_name(self) -> str:
        return self._name

    def get_user_role(self) -> str:
        return self._role

    def get_user_privilege_level(self) -> int:
        return self._privilege_level

    def get_user_organizations(self) -> List[org]:
        return self._organizations

    def get_user_online(self) -> bool:
        return self._online

    def get_user_assigned_systems(self) -> List[sys]:
        return self._assigned_systems

    def set_user_name(self, name: str):
        self._name = name

    def set_user_role(self, role: str):
        self._role = role

    def set_user_privilege_level(self, privilege_level: int):
        self._privilege_level = privilege_level

    def add_user_organizations(self, organization: org):
        self._organizations.append(organization)

    def remove_user_organizations(self, organization: org):
        # add code to remove all assigned systems from this organization
        self._organizations.remove(organization)

    def set_user_online(self, online: bool):
        if online == False :
            self.terminate()
        self._online = online

    def allocate_system(self, assigned_system: sys):
        # add checks to make sure user can have system
        # check to make sure user has correct priv level for the system
        # check to make user the user is online
        # check to make sure the user's organization has access to the system
        # check to see if enough licenses exist
        # add checks to make sure user can have system
        assigned_system.set_system_license_count(assigned_system.get_system_license_count() - 1)
        self._assigned_systems.append(assigned_system)

    def return_system(self, assigned_system: sys):
        self._assigned_systems.remove(assigned_system)

    def terminate(self):
        assigned_systems = self.get_user_assigned_systems()
        for system in assigned_systems:
            system.set_system_license_count(system.get_system_license_count() + 1)
            self.return_system(system)
