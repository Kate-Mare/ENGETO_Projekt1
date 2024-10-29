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
# První číslice musí být mezi 1 a 9 (aby nezačínala nulou)
first_digit = random.choice(range(1, 10))
# Zbývající číslice mohou být libovolné mezi 0 a 9
other_digits = random.sample(range(0, 10), 3)
# Spojení první číslice s ostatními
secret_number = [first_digit] + other_digits
print(secret_number)
sn = "".join(str(number) for number in secret_number)
print(sn) #Náhodně vygenerované číslo k otestování

# Ověření vstupu
def is_valid_input(user_choice):
    if any(not number.isdigit() for number in user_choice):
        print("You didn't insert a number.")
        return False
    elif len(user_choice) != 4:
        print("Your number doesn't include 4 digits.")
        return False
    elif user_choice.startswith("0"):
        print("Your number can't start with zero.")
        return False
    elif len(user_choice) != len(set(user_choice)):
        print("Your digits must be unique.")
        return False
    return True


# Funkce pro vyhodnocení býků a krav
def evaluate_bulls_and_cows(user_choice, sn):
    n_bull = sum(1 for i, number in enumerate(user_choice) if int(number) == int(sn[i]))
    n_cow = sum(1 for number in user_choice if number in sn) - n_bull
    return n_bull, n_cow


# Zahájení sledování hádání čísla
start_time = time.time()
guess_num = 0
game_statistics = []

print("Enter a number:")
print(oddelovac)

while True:
    user_choice = input(">>>  ")
    print(oddelovac := "-" * 48)

    if not is_valid_input(user_choice): #pokud je podmínka True, smyčka se pustí znovu
        continue

    guess_num += 1

    # Vyhodnocení býků a krav
    n_bull, n_cow = evaluate_bulls_and_cows(user_choice, sn)

    bull = "bull" if n_bull == 1 else "bulls"
    cow = "cow" if n_cow == 1 else "cows"
    if n_bull != 4:
        print(f"{n_bull} {bull}, {n_cow} {cow}")

    else:
        end_time = time.time()
        time_difference = end_time - start_time
        guess = "guess" if guess_num == 1 else "guesses"
        print(f"Correct, you've guessed the right number in {guess_num} {guess}!")
        print(f"Time taken: {time_difference:.2f} seconds")
        print(oddelovac)
        print("That's amazing!")

        # Statistiky
        game_statistics.append(guess_num)
        total_num_games = len(game_statistics)
        attempts_per_game = sum(game_statistics) / total_num_games
        print(f"Total games played: {total_num_games}")
        print(f"Average attempts per game: {attempts_per_game:.2f}")
        break



