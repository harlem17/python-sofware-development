patients = []


class Patient:
    """Class representing a patient"""

    def __init__(self, name, document, sex, birthdate, vital_signs,
                 evolution_notes, diagnostic_images,
                 lab_results, prescribed_medications):
        self.name = name
        self.document = document
        self.sex = sex
        self.birthdate = birthdate
        self.vital_signs = vital_signs
        self.evolution_notes = evolution_notes
        self.diagnostic_images = diagnostic_images
        self.lab_results = lab_results
        self.prescribed_medications = prescribed_medications

    def add_patient(self):
        num_patients = int(input("Enter the number of patients to add: "))
        for i in range(num_patients):
            patient = {}
            print(f"Enter patient data for patient {i + 1}:")
            patient['name'] = str(input("Enter the patient's name: "))
            patient['document'] = int(input("Enter the patient's document number: "))
            patient['sex'] = input("Enter the patient's sex: ")
            patient['birthdate'] = str(input("Enter the patient's birthdate (dd/mm/yy): "))
            patients.append(patient)
