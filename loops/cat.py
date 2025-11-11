"""
i = 3
while i != 0:
    print("meow")
    i -= 1
"""

"""
for i in range(3):
    print("meow")

print("meow\n" * 3, end="")
"""


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


"""
for i in range(n):
    print("meow")
"""


def meow(n):
    for i in range(n):
        print("meow")


def main():
    number = get_number()
    meow(number)


main()
