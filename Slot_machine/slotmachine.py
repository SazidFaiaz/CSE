import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROW = 3
COL = 3

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a number.")

    return amount

def get_number():
    while True:
        lines = input("Enter the number of lines you want to play: (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input("Enter the amount you want to bet on each line? $: ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print(f"Please enter a number between {MIN_BET}$ - {MAX_BET}$.")
        else:
            print("Please enter a number.")
    return bet

def main():
    balance = deposit()
    lines = get_number()
    bet = get_bet()
    total_bet = lines * bet
    print("You have " + str(balance) + "$ to play with.")
    print("You are playing with " + str(lines) + " lines.")
    print("You are betting " + str(bet) + "$ per line. Total bet is " + str(total_bet) + "$.")
main()