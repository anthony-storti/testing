from System import System as sys
from typing import List


class User:
    def __init__(self, name: str, role: str, privilege: int, organizations: str, online: bool,
                 assigned_systems: List[sys], available_systems: List[sys]):
        self._name = name
        self._role = role
        self._privilege_level = privilege
        self._organizations = organizations
        self._online = online
        self._assigned_systems = []
        self._available_systems = available_systems

    def __del__(self):
        for i in self._assigned_systems:
            self._assigned_systems.remove(i)
        for i in self._available_systems:
            self._available_systems.remove(i)

    # function prototypes
    def _find_system(self, s_name: str) -> sys:
        for s in self._available_systems:
            if s_name == s.get_system_name():
                return s
        print("System not found!")

    def _check_privilege(self, sys_obj: sys) -> bool:
        if sys_obj.get_system_access_level() == 1:
            return True
        else:
            return self._privilege_level <= sys_obj.get_system_access_level()

    def allocate_system(self, sys_name: str):
        s_name = self._find_system(sys_name)
        if not s_name is None:
            if self._check_privilege(s_name):
                if self._online:
                    if s_name.get_system_license_count() != 0:
                        if not self.get_user_name() in s_name.get_username_list():
                            self._assigned_systems.append(s_name)
                            s_name.decrease_license_count()
                            s_name.add_username_list(self.get_user_name())
                            print("You have successfully assigned to " + s_name.get_system_name() + "!")
                        else:
                            print("You have already assigned to this system")
                    else:
                        print("Reached the maximum access for this system, please try again later!")
                else:
                    print("Please reconnect with internet and try it again!")
            else:
                print("Access Denied! Access level does not match.")
        else:
            print("The system that you are looking for does not exist")

    def allocate_system_incorrect(self, sys_name: str):
        s_name = self._find_system(sys_name)
        if not s_name is None:
            if self._check_privilege(s_name):
                if self._online:
                    if s_name.get_system_license_count() != 0:
                        self._assigned_systems.append(s_name)
                        s_name.decrease_license_count()
                        s_name.add_username_list(self.get_user_name())
                        print("You have successfully assigned to " + s_name.get_system_name() + "!")
                    else:
                        print("Reached the maximum access for this system, please try again later!")
                else:
                    print("Please reconnect with internet and try it again!")
            else:
                print("Access Denied! Access level does not match.")
        else:
            print("The system that you are looking for does not exist")

    def de_allocate_system(self, sys_name: str):
        s_name = self._find_system(sys_name)
        s_name.increase_license_count()
        s_name.remove_username_list(self.get_user_name())
        self._assigned_systems.remove(s_name)

    def terminate(self):
        if self._assigned_systems:
            for s in self._assigned_systems:
                self.de_allocate_system(s.get_system_name())
                self._online = False
                print("You have been assigned offline.")
        else:
            self._online = False
            print("You have been assigned offline.")

    def clear_available_system(self):
        self._available_systems = []

    # Getters
    def get_user_name(self) -> str:
        return self._name

    def get_user_role(self) -> str:
        return self._role

    def get_user_privilege_level(self) -> int:
        return self._privilege_level

    def get_user_organizations(self) -> str:
        return self._organizations

    def get_user_online(self) -> bool:
        return self._online

    def get_user_assigned_systems(self) -> List[sys]:
        return self._assigned_systems

    def get_available_systems(self):
        return self._available_systems



    # Setters
    def set_user_name(self, name: str):
        self._name = name

    def set_user_role(self, role: str):
        self._role = role

    def set_user_privilege_level(self, privilege_level: int):
        self._privilege_level = privilege_level

    def set_user_online(self, online: bool):
        if not online:
            self.terminate()
        self._online = online

    def set_available_systems(self, system: sys):
        self._available_systems.append(system)

