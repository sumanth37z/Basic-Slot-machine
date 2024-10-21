# PYTHON SLOT MACHINE
import random


def spin_row():
    symbols = ['🌸','🔔','🍖','🧨','💸']
    return[random.choice(symbols)  for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🌸':
            return bet * 3
        elif row[0] == '🔔':
            return bet * 5
        elif row[0] == '🍖':
            return bet * 10
        elif row[0] == '🧨':
            return bet * 15
        elif row[0] == '💸':
            return bet * 25
    return 0

def main():
    balance = 10000
    print("Welcome to slot machine 🎰")
    print("Symbols: 🌸 🔔 🍖 🧨 💸")

    while balance > 0:
        print(f"Current balance: ₹{balance}")

        bet = input("Enter the bet amount: ")
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue
        if bet <= 0:
            print("Bet should be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning....\n")

        print("-------------")
        print_row(row)
        print("-------------")

        payout = get_payout(row,bet)


        if payout > 0:
            print(f"You won ₹{payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break
            
    print(f" Game over, your final balance is ₹{balance}")


if __name__ == '__main__':
    main()