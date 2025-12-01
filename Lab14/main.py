# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025
# Description:  A puppy simulator program that has two basic functions: to feed 
# or play with the puppy. The puppy will react differently to these functions
# based on which state it is currently in. The puppy has three possible 
# states: asleep, eating, or playing.

from check_input import get_int_range
from puppy import Puppy

def main():
    print("Congratulations on your new puppy!")
    pup = Puppy()

    user_choice = 0
    # Loops until user quits
    while user_choice != 3:
        print("What would you like to do?")
        print("1. Feed the puppy\n2. Play with the puppy\n3. Quit")
        user_choice = get_int_range("Enter choice: ", 1, 3)
        print()

        # Display the puppy’s reaction to the user’s choice
        if user_choice == 1:
            print(pup.give_food())
        elif user_choice == 2:
            print(pup.throw_ball())

if __name__ == "__main__":
    main()