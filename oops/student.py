def main():
    student = get_student()
    # Dictionaries and Lists are mutable whereas tuples are not
    if student["name"] == "Padma":
        student["house"] = "Griffindor"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
