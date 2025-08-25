# Authors: Nathan Nguyen, Max Cirson
# Date: Aug 25, 2025
# Description: Generates a random value between 1 and 100,
# then prompts the user to guess it.

import check_input
import random

def main():
    """ Function generates a random number between 1 and 100,
        then prompts the user to guess it.

        Args:
            None

        Returns:
            Number of guesses

        Raises:
            ValueError: Caused by trying to convert a non-numeric string
            to an integer using int()
    """
    
    print("- Guessing Game –")

    random_value = random.randint(1, 100)
   
    guess_value =  check_input.get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)
    guess_count = 1

    while guess_value != random_value:
        if guess_value < random_value and guess_value >= 1:
            guess_value = check_input.get_int_range("Too low! Guess again: ", 1, 100)
            guess_count += 1
        else: #guess_value > random_value and guess_value <= 100:
            guess_value = check_input.get_int_range("Too high! Guess again: ", 1, 100)
            guess_count += 1
    
    print("Correct! You got it in", guess_count,  "tries.")

main()
