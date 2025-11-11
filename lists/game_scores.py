game_scores = {
    "Ketav": ["Tower 8", "8"],
    "Saksham": ["Tower 9", "NA"],
    "Namit": ["Tower 10", "10"],
}


def get_score(player):
    if player in game_scores.keys():
        return game_scores.get(player)[1]


def main():
    game_scores.update({"Adit": ["Tower 11", "2"]})
    game_scores["Sachit"] = ["Tower 2", "NA"]
    for player in game_scores.keys():
        record = game_scores[player]
        print(f"{player} scored {record[1]}")

    print("Ketav scored ", get_score("Ketav"))


main()
