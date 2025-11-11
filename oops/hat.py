import random


class Hat:
    houses = ["Gryffindor", "Ravenclaw", "Slytherin"]

    # class level method
    # cls is reference to class itself
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
