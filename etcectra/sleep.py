def main():
    n = int(input("What's n: "))
    for s in sheep(n):
        print(s)


"""
def sheep(n):
    flock = []
    for i in range(n):
        flock.append("sheep" * i)
    return flock
"""


# This technique is called generators for large data
def sheep(n):
    for i in range(n):
        # return 1 value at a time
        yield "sheep" * i


if __name__ == "__main__":
    main()
