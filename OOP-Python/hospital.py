import hashlib

class Patient(object):
    def __init__(self, name, allergies):
        self.idn = hashlib.md5(name + allergies).hexdigest()[-8:] 
        self.name = name
        self.allergies = allergies
        self.bed_num = None
    
    def patient_info(self):
        print "Patient ID: \t{}\nName:\t\t{}\nAllergies: \t{}\nBed Number: \t{}".format(self.idn, self.name, self.allergies, self.bed_num)

class Hospital(object):
    def __init__(self, location, capacity):
        self.patients = []
        self.location = location
        self.capacity = capacity
        self.beds = range (1, self.capacity + 1) #You have to use +1 because the index is counting from 0-length. But we need beds from 1 until available beds
    
    def new_patient(self, patient):
        if len(self.patients) >= self.capacity:
            print "Sorry, this hospital is full. Search for another one. Have fun"
        else:
            self.patients.append(patient)
            self.capacity -= 1
            self.bed_num = self.beds.pop()
            print "Hello {}. You are submitted! Your Bed Number is: {}".format(patient.name, self.bed_num)

    def discharge(self, name):
        for i in range (len(self.patients)-1):
            if name == self.patients[i].name:
                self.capacity += 1
                self.patients.pop(i)
                self.bed_num = 'None'
                print "Sucesfully Discharged. Enjoy your freetime now"
        return self
        
    def all_patients(self):
        for i in range (len(self.patients)):
            print "Patient ID: \t\t{}".format(self.patients[i].idn) 
            print "Patient Name: \t\t{}".format(self.patients[i].name)
            print "Patient Allergies: \t{}".format(self.patients[i].allergies)
            print "Patient Bed Number: \t{}".format(self.bed_num)
            print

ibk_hospital = Hospital('Innsbruck', 150)
sf_hospital = Hospital('San Francisco', 40)

ibk_hospital.new_patient(Patient('Manuel', 'No'))
ibk_hospital.new_patient(Patient('Isabell', 'Peanuts'))
ibk_hospital.new_patient(Patient('Lucas', 'Chicken'))
ibk_hospital.all_patients()
ibk_hospital.discharge('Isabell')
ibk_hospital.all_patients()


