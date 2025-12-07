students = ["Hermoine", "Harry", "Ron"]
"""
gryffindors = []

for student in students:
    gryffindors.append({"name":student, "house":"Gryffindor"})
"""

# this is list comprehension
# gryffindors = [{"name":student, "house":"Gryffindor"} for student in students]

# this is dictionary comprehension
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)

for i in range(len(students)):
    print(i + 1, students[1])

for i, student in enumerate(students):
    print(i + 1, student)
