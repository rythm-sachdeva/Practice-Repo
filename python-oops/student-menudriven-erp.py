class Student:
    def __init__(self,name:str,address:str,age:int,marks:int) -> None:
        self.name = name
        self.address=address
        self.age = age
        self.marks = marks
    
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def addStudent(self):
        name = input("Enter Name:")
        address = input("Enter Address:")
        age = int(input("Enter Age:"))
        marks = int(input("Enter Marks:"))
        student = Student(name,address,age,marks)
        self.students.append(student)
        print("Student added successfully")
    
    



        