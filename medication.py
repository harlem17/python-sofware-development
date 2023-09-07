from Patient import patients

class Medication:
    def __init__(self, name, dosage, frequency):
        self.name = name
        self.dosage = dosage
        self.frequency = frequency

    def add_medication(self):
        for patient in patients:
            patient['name'] = input("Enter the medication name: ")
            patient['dosage'] = int(input("Enter the number of doses per day: "))
            patient['frequency'] = str(input("Enter the medication frequency: "))