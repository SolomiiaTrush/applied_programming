from User import User
from Speciality import Specialty

class Doctor(User):
    def __init__(self, ID: str, first_name: str, last_name: str, sex: str, birth_date: str,
                 rate: float, specialty: Specialty):
        super().__init__(ID, first_name, last_name, sex, birth_date)

        self.__rate = rate
        self.__specialty = specialty

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, rate):
        self.__rate = rate

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, specialty):
        self.__specialty = specialty

    def display_info(self):
        print(f"ID : {self.id}\nName: {self.first_name} {self.last_name}\n"
              f"Sex : {self.sex}\nDate of birth : {self.birth_date}\n"
              f"Rate : {self.rate}\nSpecialty : {self.specialty.name}")