players = {
    "Virat":["5203", "199"],
    "Sachin":["23019","399"],
    "Rohit":["NA",""]
}
def get_average(num_of_matches,total_runs):
    try:
        return int(total_runs)/int(num_of_matches)
    except:
        return "NaN" 

def main():
    for player in players.keys():
        average = get_average(players.get(player)[1],players.get(player)[0])
        print(f"{player}'s average is {average}")

main()
