from Patient import patients

class Bed:
    def __init__(self, number, service):
        self.number = number
        self.service = service

    def add_bed(self):
        for patient in patients:
            patient['number'] = int(input("Enter the bed number: "))
            patient['service'] = input("Enter the service to provide: ")