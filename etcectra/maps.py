def main():
    yell("This", "is", "CS50")


def yell(*words):
    """
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    """
    """
    #maps the upper function to every word. This is functional programming
    uppercased=map(str.upper, words)
    print(*uppercased)
    """
    # This is list comprehension
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
