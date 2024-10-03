from Prescription import Prescription
from Payment import Payment

class Appointment(Payment, Prescription) :
    def __init__ (self, ID : str, patient_id : str, timestamp : str,
                  price : float, doctor_id : str, drug_id : str, description : str) :
        Payment.__init__(self, ID, patient_id, timestamp, price)
        Prescription.__init__(self, ID, patient_id, timestamp, doctor_id, drug_id)
        self.__description = description

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    def display_info(self):
        print(
            f"ID: {self.id}\n"
              f"Patient ID: {self.patient_id}\n"
              f"Doctor ID: {self.doctor_id}\n"
              f"Drug ID: {self.drug_id}\n"
              f"Price: {self.price}\n"
              f"Description: {self.description}\n"
              f"Date: {self.date}"
        )

    @staticmethod
    def create_appointment(ID, patient_id, timestamp,price, doctor_id, drug_id, description):
        return Appointment(ID, patient_id, timestamp, price, doctor_id, drug_id, description)


