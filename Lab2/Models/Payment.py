from Document import Document

class Payment(Document) :
    def __init__ (self, ID : str, patient_id : str, timestamp : str, price : float) :
        Document.__init__(self, ID, patient_id, timestamp)
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def display_info (self) :
        print(f"ID : {self.id}\nPatient ID: {self.patient_id}\nPrice : {self.price}\nDate : {self.date}")

    @staticmethod
    def create_payment(ID, patient_id, timestamp, price):
        return Payment(ID, patient_id, timestamp, price)
