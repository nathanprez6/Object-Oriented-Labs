# Authors: Nathan Nguyen, Max Cirson
# Date: Aug 25, 2025
# Description: 

import random

def main():
    """ Function generates a random number between 1 and 100,
        then prompts the user to guess it.

        Args:
            None

        Returns:
            Number of guesses

        Raises:
        
    """
    
    print("- Guessing Game –")

    random_value = random.randint(1, 100)

    guess_value = int(input("I'm thinking of a number. Make a guess (1-100): "))

    guess_count = 1

    while guess_value != random_value:
        if guess_value < random_value:
            guess_value = int(input("Too low! Guess again: "))
            guess_count += 1
        elif guess_value > random_value:
            guessValguess_valueue = int(input("Too high! Guess again: "))
            guess_count += 1
        elif guess_value < 1 or guess_value > 100:
            print("Invalid input – should be within range 1-100.")
            guess_value = int(input("Guess again (1-100): "))
        else:
            print("Invalid input – should be an integer.")
            guess_value = int(input("Guess again (1-100): "))

    print("Correct! You got it in", guess_count,  "tries.")

main()
