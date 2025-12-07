def main():
    sentence = input("Enter a sentence: ")
    print(playback(sentence))


def playback(sentence):
    output = ""
    for i in range(len(sentence)):
        if sentence[i] == " ":
            output += "..."
        else:
            output += sentence[i]
    return output


if __name__ == "__main__":
    main()
