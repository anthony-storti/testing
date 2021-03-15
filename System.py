class System:
    def __init__(self, name: str, s_type: str, access_level: int, license_count: int, organizations: str,
                 usr_name_on: list[str]):
        self._name = name
        self._type = s_type
        self._access_level = access_level
        self._license_count = license_count
        self._organizations = organizations
        self._usr_name_on = usr_name_on
        self._MAX_LICENSE_NUMBER = license_count

    # function prototypes
    def decrease_license_count(self):
        if self._license_count > 0:
            self._license_count -= 1
        else:
            print("Reached the maximum access, access denied!")

    def increase_license_count(self):
        if not (self._license_count >= self._MAX_LICENSE_NUMBER):
            self._license_count += 1
        else:
            print("Maximum reached, action denied!")

    def display_current_user(self):
        if not self._usr_name_on is None:
            for user in self._usr_name_on:
                print(user)
        else:
            print("There is no user working on the " + self.get_system_name() + " system.")

    # getters
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

    def get_username_list(self) -> list[str]:
        return self._usr_name_on

    def get_max_license_number(self) -> int:
        return self._MAX_LICENSE_NUMBER

    # setters
    def set_max_license_number(self, num: int):
        self._MAX_LICENSE_NUMBER = num

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

    def add_username_list(self, username: str):
        self._usr_name_on.append(username)

    def remove_username_list(self, username: str):
        found = False
        for name in self._usr_name_on:
            if username == name:
                found = True
        if found:
            self._usr_name_on.remove(username)
        else:
            print("The username you typed does not exist")
