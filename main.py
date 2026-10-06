# patient class
class patient:
    def __init__(self, name, patient_id, age, gender, diagnosis):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("/n----------patient information----------")    
        print(f"ID : {self.patient_id}")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Diagnosis :{self.diagnosis}")

# Hospital Class
class hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        
        self.patients = [] # List to store patients objects

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"patient added successfully.")

    def display_patients(self):
        print ("\n **********All patients**********")
        print (f"\n ***** {self.hospital_name}*****")

        # check if there are patients
        if len(self.patients) == 0:
            print("No patients Records found.")
        else:
            for patient in self.patients:
                patient.display_info()
# patient objects
patient1 = patient("saidu", "101", 23, "male", "poverty")
patient2 = patient("Abu Turay", "102", 30, "male", "Malaria")
patient3 = patient("Yabom Turay", "103", 21, "male", "poverty")

# Hospital object
hospital1 = hospital("City Hospital")

# Adding patients to the hospital using the add_patientmethod in the Hospital class
hospital1.add_patient(patient1)
hospital1.add_patient(patient2)
hospital1.add_patient(patient3)

# displaying all patients in the hospital
hospital1.display_patients()