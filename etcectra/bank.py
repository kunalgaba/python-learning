# "": int" is just a hint or annotation to describe the expected type
balance: int = 0


def main():
    # balance is accessible inside main
    print(f"Balance : {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance : {balance}")


# "": int" is just a hint or annotation to describe the expected type
def deposit(n: int):
    # balance variable can not be accessed
    # If a variable has to change then you can not do it on global variable. It can only be read
    global balance  # clue to python that this method can edit global variable
    balance = balance + n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
