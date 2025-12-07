import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    match = re.search(r"^[A-Z]{2}[A-Z]*([0-9]*)$", s)
    if match and not match.group(1).startswith("0") and len(s) <= 6:
        return True
    else:
        return False


main()
