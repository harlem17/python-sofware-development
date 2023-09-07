from ClinicHistory import ClinicHistory
from Patient import Patient
from bed import Bed
from medication import Medication

def show_menu(options):
    print('Select an option:')
    for key in sorted(options):
        print(f' {key}) {options[key][0]}')

def read_option(options):
    while (choice := input('Option: ')) not in options:
        print('Incorrect option, please try again.')
    return choice

def execute_option(option, options):
    options[option][1]()

def generate_menu(options, exit_option):
    choice = None
    while choice != exit_option:
        show_menu(options)
        choice = read_option(options)
        execute_option(choice, options)
        print()

def main_menu():
    options = {
        '1': ('1. add_patients', action1),
        '2': ('2. add data to medical history', action2),
        '3': ('3. add bed', action3),
        '4': ('4. add medications', action4),
        '5': ('5 show clinic history', action5),
        '6': ('Exit', exit_program)
    }

    generate_menu(options, '6')

patient = Patient

def action1():
    print('You have chosen Option 1')
    patient.add_patient(Patient)

def action2():
    print('You have chosen Option 2')
    ClinicHistory.add_clinic_history(Patient)

def action3():
    print('You have chosen Option 3')
    Bed.add_bed(Patient)

def action4():
    print('You have chosen Option 4')
    Medication.add_medication(Patient)

def action5():
    print('You have chosen Option 5')
    ClinicHistory.show_clinic_history(Patient)

def exit_program():
    print('Exiting')

if __name__ == '__main__':
    main_menu()