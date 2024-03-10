import random


class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOffStuddy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOffStuddy)

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentslist = []
        self.fieldsOffStudy = ["IT", "Math", "Robotics"]

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentslist.append(student)
            student.schoolName = self.name
            student.fieldOffStuddy = random.choice(self.fieldsOffStudy)

    def printSchoolInfo(self):
        print("School name :", self.name, " City: ", self.city)
        print("Students:")
        for i in self.studentslist:
            i.printInfo()

student1 = Student("Kasia", "Lis", 20, "Krk")
student1.schoolName = "Tech School 1"
student1.country = "Poland"
student1.printInfo()
print(student1.country)

student2 = Student("Adam", "Kowalski", 21, "Gda")

school = School("Tech School", "Waw")
school.addStudent(student1)
school.addStudent(student2)
print("----------------")
school.printSchoolInfo()