"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kateřina Marková
email: cathy.markova@gmail.com
discord: kate_marko1_54460
"""
import random
import time

print("Hi there!")
print(oddelovac := "-" * 48)
print("I've generated a random 4 digit number for you.\n"
      "Let's play a bulls and cows game.")
print(oddelovac)
# Generování tajného čísla
secret_number = random.sample(range(1, 10), 4)
sn = "".join(str(number) for number in secret_number)
#print(sn) #Náhodně vygenerované číslo k otestování
guess_num = 0
# Zahájení sledování hádání čísla
start_time = time.time()
print("Enter a number:")
print(oddelovac)
game_statistics = []
# Smyčka pro opakované zadávání čísla
while True:
    user_choice = input(">>>  ")
    print(oddelovac := "-" * 48)

    if any(not number.isdigit() for number in user_choice):
        print("You didn't insert a number.")
        continue
    elif len(user_choice) != 4:
        print("Your number doesn't include 4 digits.")
        continue
    elif "0" in user_choice:
        print("Zero not allowed in your number.")
        continue
    elif len(user_choice) != len(set(user_choice)):
        print("Your digits must be unique.")
        continue

    guess_num += 1
    n_bull = 0
    n_cow = 0
    # Hledání shody pro jednotlivé číslice
    for i, number in enumerate(user_choice):
        if int(number) == int(sn[i]):
            n_bull += 1
        elif number in sn:
            n_cow += 1
    bull = "bull" if n_bull == 1 else "bulls"
    cow = "cow" if n_cow == 1 else "cows"
    if n_bull != 4:
        print(f"{n_bull} {bull}, {n_cow} {cow}")
    else:
        end_time = time.time()  #ukončení času hádání
        time_difference = end_time - start_time
        guess = "guess" if guess_num == 1 else "guesses"
        print(f"Correct, you've guessed the right number"
              f" in {guess_num} {guess}!")
        print(f"Time taken: {time_difference:.2f} seconds")
        print(oddelovac)
        print("That's amazing!")
        # list, do kterého se ukládají jednotl. guess_num
        game_statistics.append(guess_num)
        total_num_games = len(game_statistics) #celkový počet her
        # Prům. počet pokusů na 1 hru
        attempts_per_game = sum(game_statistics)/total_num_games
        print(f"Total games played: {total_num_games}")
        print(f"Average attempts per game: {attempts_per_game}")

        break










