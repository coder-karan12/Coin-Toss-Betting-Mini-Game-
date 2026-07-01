import random

print("=" * 20)
print(" Coin Toss Betting ")
print("=" * 20)

balance = 100
coin = ["Heads", "Tails"]

while balance > 0:

    result = random.choice(coin)

    print(f"\nCurrent Balance: ₹{balance}")

    amount = int(input("Enter Bet Amount: "))

    if amount > balance:
        print(" Insufficient Balance")
        continue

    elif amount == 0:
        print(" Betting amount can't be 0")
        continue

    elif amount < 0:
        print(" Please enter a valid amount")
        continue

    choice = input("Choose Heads or Tails: ").strip().capitalize()

    print(f" Coin Landed On: {result}")

    if choice == result:
        print(" Congratulations! You guessed it right.")
        balance += amount

    else:
        print(" You guessed it wrong.")
        balance -= amount

    print(f" Current Balance: ₹{balance}")