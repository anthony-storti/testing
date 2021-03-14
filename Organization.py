class Organization:

    def __init__(self, name: str, location: str, type: str):
        self._name = name
        self._location = location
        self._type = type

    def get_org_name(self) -> str:
        return self._name

    def get_org_location(self) -> str:
        return self._location

    def get_org_type(self) -> str:
        return self._type

    def set_org_name(self, name: str):
        self._name = name

    def set_org_location(self, location: str):
        self._location = location

    def set_org_type(self, type: str):
        self._type = type
