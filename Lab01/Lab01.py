# Authors: Nathan Nguyen, Maximus Cirson
# Date: Aug 25, 2025
# Description: Generates a random value between 1 and 100,
# then prompts the user to guess it.

import Lab14.check_input as check_input
import random

def main():
    print("- Guessing Game -")

    random_value = random.randint(1, 100)

    guess_value = check_input.get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)
    guess_count = 1

    # Loops until number is guessed correctly
    while guess_value != random_value:
        if guess_value < random_value:
            print("Too low!", end="  ")
            guess_count += 1
        elif guess_value > random_value:
            print("Too high!", end="  ")
            guess_count += 1
        guess_value = check_input.get_int_range("Guess again (1-100): ", 1, 100)
    
    print("Correct! You got it in", guess_count,  "tries.")

main()
