sentence = input("Input: ")
output = ""
for i in range(len(sentence.strip())):
    if (
        sentence[i] == "a"
        or sentence[i] == "A"
        or sentence[i] == "e"
        or sentence[i] == "E"
        or sentence[i] == "i"
        or sentence[i] == "I"
        or sentence[i] == "o"
        or sentence[i] == "O"
        or sentence[i] == "u"
        or sentence[i] == "U"
    ):
        ...
    else:
        output = output + sentence[i]
print(output)
