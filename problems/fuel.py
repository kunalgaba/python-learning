def main():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            fuel = get_fuel(x, y)
        except (ValueError, ZeroDivisionError, ArithmeticError) as e:
            continue
        if fuel <= 1:
            print("E")
            return
        elif fuel >= 99:
            print("F")
            return
        else:
            print(f"{fuel}%")
            return


def get_fuel(x, y):
    result = 0
    try:
        num = int(x)
        denom = int(y)
        if num > denom or num < 0:
            raise ArithmeticError("Num > denom")
        result = round((num * 100) / denom, 1)
    except ValueError:
        raise ValueError("The fraction should have integer num and denom")
    except ZeroDivisionError:
        raise ZeroDivisionError("Denom is zero")
    return int(result)


if __name__ == "__main__":
    main()
