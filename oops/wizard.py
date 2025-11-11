class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


# Student is subclass of Wizard
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


# StudProfessorent is subclass of Wizard
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the Dark Arts")
