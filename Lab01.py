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

    randomValue = random.randint(1, 100)

    guessValue = int(input("I'm thinking of a number. Make a guess (1-100): "))

    guessCount = 1

    while guessValue != randomValue:
        if guessValue < randomValue:
            guessValue = int(input("Too low! Guess again: "))
            guessCount += 1
        elif guessValue > randomValue:
            guessValue = int(input("Too high! Guess again: "))
            guessCount += 1
        elif guessValue < 1 or guessValue > 100:
            print("Invalid input – should be within range 1-100.")
            guessValue = int(input("Guess again (1-100): "))
        else:
            print("Invalid input – should be an integer.")
            guessValue = int(input("Guess again (1-100): "))

    print("Correct! You got it in", guessCount,  "tries.")

main()
