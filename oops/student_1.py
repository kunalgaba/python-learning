class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self._house}"

    @property
    def house(self):
        return self._house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # setter, @house.setter is a decorator and tells python its a setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "1"
            case "Otter":
                return "2"
            case _:
                return "0"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)


def main():
    student = Student.get()
    print(student)
    # Python calls the setter function immediatley
    # student.house = "test"
    print(f"{student.name} from {student.house}")
    print(student.charm())


if __name__ == "__main__":
    main()
