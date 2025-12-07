"""
#simple unpacking
first, last = input("What's your name: ").split(" ")
print(f"hello, {first}")
"""

coins = [100, 50, 25]


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# one option to pass the list values
# print(total(coins[0],coins[1],coins[2]), " Knuts")

# Python unpacks the list automatically
print(total(*coins), "Knuts")

coins_fresh = {"galleons": 100, "sickles": 50, "knuts": 25}
print(
    total(coins_fresh["galleons"], coins_fresh["sickles"], coins_fresh["knuts"]),
    "Knuts",
)
print(total(**coins_fresh), "Knuts")
# the above **coins_fresh is same as - total(galleons=100, sickles=50, knuts=25)
