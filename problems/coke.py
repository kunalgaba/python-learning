amount_due = 50
while True:
    print(f"Amount Due: {amount_due}")
    payment = int(input("Insert Coin: "))
    if payment == 25 or payment == 10 or payment == 5:
        amount_due -= payment
    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
        break
