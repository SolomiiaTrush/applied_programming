from datetime import date

class Document :
    def __init__ (self, ID : str, patient_id : str, timestamp : str) :
        self.__id = ID
        self.__patient_id = patient_id
        self.__date = timestamp

    @property
    def id (self) :
        return self.__id

    @id.setter
    def id(self, ID):
        self.__id = ID

    @property
    def patient_id(self):
        return self.__patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        self.__patient_id = patient_id

    @property
    def date(self):
        return self.__date

    @date.setter
    def date (self, timestamp):
        self.__date = timestamp


    # method without parameters
    # implements polymorphism
    def display_info (self) :
        print(f"ID: {self.id}\nPatient ID: {self.patient_id}\nDate: {self.date}")

    # method with parameters
    @staticmethod
    def create_document (_id, _patient_id) :
        if not _id or not _patient_id :
            raise ValueError("Every field must be filled")

        return Document(_id, _patient_id, date.today().strftime("%d/%m/%Y"))







