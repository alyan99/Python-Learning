class hospitalMang:
    def __init__(self,name,employee_id,department):
        self.name=name
        self.employee_id=employee_id
        self.department=department
    def display(self):
        print("Name:",self.name)
        print("Employee ID:",self.employee_id)
        print("Department:",self.department)
class Doctor(hospitalMang):
    def __init__(self,specialization,fee,**kwargs):
        super().__init__(**kwargs)
        self.specialization=specialization
        self.fee=fee
    def examinePatient(self,patient_name):
        print("Dr.",self.name," is examining the patient:",patient_name)
    def display(self):
        super().display()
        print("Specialization:",self.specialization)
        print("Fee:",self.fee)
class Nurse(hospitalMang):
    def __init__(self,shift_time,ward_assigned,**kwargs):
        super().__init__(**kwargs)
        self.shift_time=shift_time
        self.ward_assigned=ward_assigned
    def administratorMedication(self,patient_name,doctor_name):
        print("Nurse ",self.name," is administering medication of patient ",patient_name,"provided by Dr.",doctor_name)
    def display(self):
        super().display()
        print("Shift Time:",self.shift_time)
        print("Ward Assigned:",self.ward_assigned)
class Lab_tec(hospitalMang):
    def __init__(self,lab,equipment,**kwargs):
        super().__init__(**kwargs)
        self.lab=lab
        self.equipment=equipment
    def conductTest(self,patient_name,test_name):
        print("Lab Technician ",self.name," is conducting ",test_name," test for patient ",patient_name)
    def display(self):
        super().display()
        print("Lab:",self.lab)
        print("Equipment:",self.equipment)
d=Doctor("Dentist",1500,name="Abdul Moiz",employee_id=101,department="Dental")
n=Nurse("Day Shift", "Ward A", name="Ayesha", employee_id=102, department="Nursing")
l=Lab_tec("Biochemistry Lab", "Microscope", name="Ahmed", employee_id=103, department="Laboratory")
d.examinePatient("Ali")
d.display()
n.administratorMedication("Ali", "Abdul Moiz")
n.display()
l.conductTest("Ali", "Blood")
l.display()

