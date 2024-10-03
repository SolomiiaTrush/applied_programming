class Specialty:
    def __init__(self, ID: str, name: str, description: str):
        self.__id = ID
        self.__name = name
        self.__description = description

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, ID):
        self.__id = ID

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description