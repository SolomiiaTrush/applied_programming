from Lab2.Models.Document import Document
from Lab2.Models.Payment import Payment
from Lab2.Models.Prescription import Prescription
from Lab2.Models.Appointment import Appointment
from Lab2.Models.Doctor import Doctor
from Lab2.Models.Doctor import Specialty
from Lab2.Models.Patient import Patient


specialty = Specialty("S001", "Cardiology", "Specializes in heart health")

# екземпляри класів
doctor = Doctor("D001", "Mary", "Smith", "F", "02/03/1980", 4.9, specialty)
patient = Patient("P001", "John", "Black", "M", "07/04/1991")

prescription = Prescription.create_prescription(
    "PR001", "P001", '02/10/2024 10:30:00', "D001", "DRUG001")

payment = Payment.create_payment("PY001", "P001", '02/10/2024 10:35:00', 200.0)

# appointment реалізовує множинне наслідування
appointment = Appointment.create_appointment(
    "AP001", "P001", '02/10/2024 10:00:00',
    300.0, "D001", "DRUG001", "Consultation")

# виклик методів і робота з властивостями
print("Doctor Info:")
doctor.display_info()
print("\nPatient Info:")
patient.display_info()

# display_info демонструє поліморфізм
print("\nPrescription Info:")
prescription.display_info()

print("\nPayment Info:")
payment.display_info()

print("\nAppointment Info:")
appointment.display_info()

# create_document статичний метод
document = Document.create_document("DOC001", "P001")
print("\nCreated Document Info:")
document.display_info()
