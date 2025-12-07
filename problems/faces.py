def convert(str=""):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str


def main():
    sentence = input("Enter a sentence: ")
    print(convert(sentence))


if __name__ == "__main__":
    main()
