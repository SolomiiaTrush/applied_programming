class User:
    def __init__(self, ID: str, first_name: str, last_name: str, sex: str, birth_date: str):
        self.__id = ID
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sex = sex
        self.__birth__date = birth_date

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, ID):
        self.__id = ID

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def birth_date(self):
        return self.__birth__date

    @birth_date.setter
    def birth_date(self, birth__date):
        self.__birth__date = birth__date

    def display_info(self):
        print(f"ID : {self.id}\nName: {self.first_name} {self.last_name}\n"
              f"Sex : {self.sex}\nDate of birth : {self.birth_date}")
