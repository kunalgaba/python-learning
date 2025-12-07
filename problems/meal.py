import re


def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    if converted_time >= 7.0 and converted_time <= 8.0:
        print("breakfast time")
    elif converted_time >= 12.0 and converted_time <= 13.0:
        print("lunch time")
    elif converted_time >= 18.0 and converted_time <= 19.0:
        print("dinner time")


def convert(time):
    time = time.strip()
    match = re.search(r"^([0-2]?[0-9]):([0-9][0-9])$", time)
    if match:
        (hours, minutes) = match.groups()
        converted_time = int(hours) + int(minutes) / 60
        return round(converted_time, 2)
    else:
        return 0


if __name__ == "__main__":
    main()
