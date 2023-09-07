from Patient import patients


class ClinicHistory:
    """Class representing ClinicHistory"""

    def __init__(self, patient, blood_pressure, temperature, oxygen_saturation,
                 respiratory_rate, evolution_notes, diagnostic_images,
                 lab_results):
        self.patient = patient
        self.blood_pressure = blood_pressure
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.respiratory_rate = respiratory_rate
        self.evolution_notes = evolution_notes
        self.diagnostic_images = diagnostic_images
        self.lab_results = lab_results

    def add_clinic_history(self):
        for patient in patients:
            patient['blood pressure'] = str(input("Enter the blood pressure: "))
            patient['temperature'] = int(input("Enter the temperature: "))
            patient['oxygen saturation'] = int(input("Enter the oxygen saturation: "))
            patient['respiratory rate'] = str(input("Enter the respiratory rate: "))
            patient['notes'] = str(input("Enter evolution notes: "))
            patient['images'] = str(input("Enter image URL: "))
            patient['lab results'] = str(input("Enter lab results: "))
            print("-----------------------------------------------")

    def show_clinic_history(self):
        for patient in patients:
            print(patient)

