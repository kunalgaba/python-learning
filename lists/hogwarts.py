"""
students = ["Hermoine", "Harry", "Ron"]

houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
for student in students:
    print(student)

for i in range(len(students)):
    print(i + 1, students[i])
"""

# dictionary data type
students = {"Hermoine": "Gryffindor", "Harry": "Gryffindor", "Ron": "Slytherin"}

# print(students["Hermoine"])
# iterates all the keys
for student in students:
    print(student, students[student], sep=", ")

# What if I have another column called as "patronus". How will I represent it?
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronous": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None},
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")
