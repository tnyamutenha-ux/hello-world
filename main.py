import random

def play_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("I'm thinking of a number between 1 and 10.")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Correct! You found it in {attempts} tries.")
            break

play_game()