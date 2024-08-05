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

    def viewStudents(self):
        if(len(self.students) == 0):
            print("NO STUDENTS FOUND")
        else:
             view_type = input("All students or one students: (all/one)")
             if(view_type == "all"):
                  for student in self.students:
                      print(f"Name: {student.name} \n Address:{student.address} \n Age:{student.age} \n Marks:{student.marks} \n")
             if(view_type=="one"):
                 name = input("Enter Name Of The student:")
                 for student in self.students:
                     if(name == student.name):
                         print(f"Name: {student.name} \n Address:{student.address} \n Age:{student.age} \n Marks:{student.marks} \n")
    
    def deleteStudents(self):
         name = input("Enter Name Of The student:")
         for student in self.students:
            if(name == student.name):
                self.students.remove(student)
                print("Student Removed Successfully")
                return self.students
    
    def updateStudent(self):
         name = input("Enter Name Of The student:")
         for student in self.students:
            if(name == student.name):
                 student.name = input("Enter Name:")
                 student.address = input("Enter Address:")
                 student.age = int(input("Enter Age:"))
                 student.marks = int(input("Enter Marks:"))
                 print("Student Successfully updated")
                 return student
            print("Student Not Found")
            


                
                         
    
    



        