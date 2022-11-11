from Student import Student

class Teacher(object):
    def __init__(self, name: str) -> None:
        self.name == name
        self.students = []
        
    def name(self) -> str:
        return self.name
    
    def add_student(self, student: Student) -> None:
        self.students.append(student)
        