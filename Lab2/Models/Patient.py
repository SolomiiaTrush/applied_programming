from User import User

class Patient(User):
    def __init__(self, ID, first_name, last_name, sex, birth_date) : # country, city, street, zipcode):
        super().__init__(ID, first_name, last_name, sex, birth_date)

        """self.__country = country
        self.__city = city
        self.__street = street
        self.__zipcode = zipcode"""

    def display_info(self):
        print(f"ID : {self.id}\nName: {self.first_name} {self.last_name}\n"
              f"Sex : {self.sex}\nDate of birth : {self.birth_date}")
"""    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        self.__street = street

    @property
    def zipcode(self):
        return self.__zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        self.__zipcode = zipcode"""

