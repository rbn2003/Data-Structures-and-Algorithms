class Student:
    def _init_(self, name, average):
        self.name = name
        self.average = average
        
def find_two_top_students(students_list):    #function to find two top students 
    if len(students_list) < 2:     #checking if the list has more than 2 students or not
        print("Not enough students in the list.")
        return 
        
    #sorting students in the descending order using averge as a attribute
    sorted_students = sorted(students_list, key = lambda s:s.average, reverse = True )
    
    #prinitng top two students 
    print("Top two students with the highest average are: ")
    print(f"1. {sorted_students[0].name} - {sorted_students[0].average}")
    print(f"2. {sorted_students[1].name} - {sorted_students[1].average}")
        
        
#example of a  list 
studentlist = [
    Student("Bob" , 87),
    Student("Mark", 90),
    Student("Wood", 89),
    Student("Arne", 91),
    Student("Klopp", 94),
    Student("Arteta", 84)]
    
find_two_top_students(students_list)  #runnning the function to work