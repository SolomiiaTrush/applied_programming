from Document import Document

class Prescription(Document) :
    def __init__ (self, ID : str, patient_id : str, timestamp : str, doctor_id : str, drug_id : str) :
        Document.__init__(self, ID, patient_id, timestamp)
        self.__doctor_id = doctor_id
        self.__drug_id = drug_id

    # setters
    @property
    def doctor_id(self):
        return self.__doctor_id

    @doctor_id.setter
    def doctor_id(self, doctor_id):
        self.__doctor_id = doctor_id

    @property
    def drug_id(self):
        return self.__drug_id

    @drug_id.setter
    def drug_id(self, drug_id):
        self.__drug_id = drug_id

    def display_info (self) :
        print(f"ID : {self.id}\nPatient ID: {self.patient_id}\n"
              f"Doctor ID : {self.doctor_id}\nDrug ID : {self.drug_id}\nDate : {self.date}")

    @staticmethod
    def create_prescription(ID, patient_id, timestamp, doctor_id, drug_id):
        return Prescription(ID, patient_id, timestamp, doctor_id, drug_id)
