class Student:
    def __init__(self, name, average):
        self.name = name       #the name of a student 
        self.average = average      #the avg of a student 
        
    def __repr__(self):
        return f"Student(name= {self.name}, average = {self.average})"
            
            
#creating an instance             
student1 = Student("WENGER", 85.0)
student2 = Student("KLOPP", 92.0)
student3 = Student("ARTETA", 75.0)


students = [student1, student2, student3]    #list of students 

#sorting by descending order 
sorted_students = sorted(students, key=lambda student: student.average, reverse=True)

for student in sorted_students:
    print(student)
