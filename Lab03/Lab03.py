# Authors: Nathan Nguyen, Brian Gutierrez
# Date: Sept. 8, 2025
# Description: A program that replicates the game hangman with 5-letter words

import check_input
import random
from dictionary import words

def display_gallows(num_incorrect):
    """ 
    Displays the correct state of the hangman on the gallow depending on how 
    many incorrect guesses have been made

    Args:
        num_incorrect (int): The number of incorrect guesses the user has made

    Returns: 
        None
    """
    if (num_incorrect == 0):
        print("========\n||/ |\n||\n||\n||\n||\n")
    elif (num_incorrect == 1):
        print("========\n||/ |\n||  o\n||\n||\n||\n")
    elif (num_incorrect == 2):
        print("========\n||/ |\n||  o\n||  |\n||\n||\n")
    elif (num_incorrect == 3):
        print("========\n||/ |\n||  o\n||  |\n|| /\n||\n")
    elif (num_incorrect == 4):
        print("========\n||/ |\n||  o\n||  |\n|| / \\ \n||\n")
    elif (num_incorrect == 5):
        print("========\n||/ |\n|| \o\n||  |\n|| / \\ \n||\n")
    else:
        print("========\n||/ |\n|| \o/\n||  |\n|| / \\ \n||\n")
        

def display_letters(letters):
    """ 
    Displays each of the elements of a given list separated by spaces

    Args:
        letters (list): A list of letters

    Returns: 
        None
    """
    print(*letters, "\n")

def get_letters_remaining(incorrect, correct):
    """ 
    Determines how many letters of the alphabet are remaining to choose
    from given the letters already guessed

    Args:
        incorrect (list): A list of incorrect guesses
        correct (list): A list of correct guesses

    Returns: 
        A list of remaining letters in the alphabet to choose from
    """
    remaining_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for item in incorrect:
        if item in remaining_letters:
            remaining_letters.remove(item)
    for item in correct:
        if item in remaining_letters:
            remaining_letters.remove(item)

    return remaining_letters

def main():
    play_again = True
    while(play_again):
        print("-Hangman-\n")

        # Randomly chooses word from dictionary
        random_word = words[random.randint(0, len(words))]

        # Incorrect and Correct guesses list and count initialization
        incorrect_guesses = []
        correct_guesses = ['_', '_', '_', '_', '_']

        correct_guesses_made = 0
        incorrect_guesses_made = 0

        # Loops until user runs out of tries or guesses the word
        while('_' in correct_guesses and incorrect_guesses_made < 6):
            display_gallows(incorrect_guesses_made)
            display_letters(correct_guesses)

            print("Letters remaining: ", end='')
            display_letters(get_letters_remaining(incorrect_guesses, correct_guesses))

            valid = False
            # Checks if user's guess is a single letter that has not been guess yet
            user_guess = input("Enter a letter: ").upper()
            if (user_guess.isalpha() and len(user_guess) == 1):
                if (user_guess in incorrect_guesses or user_guess in correct_guesses):
                    print("You have already used that letter.")
                else:
                    valid = True
            else:
                print("That is not a letter.")

            # if user's guess is valid, check if it is in the word and place in 
            # correct location and increment correct guesses count. Otherwise, append
            # to incorrect guesses list and increment the corresponding count.
            if valid:
                if user_guess in random_word:
                    print("Correct!\n")
                    correct_guesses_made += 1
                    find_start = 0
                    letter_index = random_word.find(user_guess, 0)
                    while (find_start < len(random_word) and letter_index >= 0):
                        find_start = letter_index + 1
                        correct_guesses[letter_index] = user_guess
                        letter_index = random_word.find(user_guess, find_start)
                else:
                    print("Incorrect!\n")
                    incorrect_guesses_made += 1
                    incorrect_guesses.append(user_guess)
                
            print("Incorrect selections: ", end='')
            incorrect_guesses.sort()
            display_letters(incorrect_guesses)

        display_gallows(incorrect_guesses_made)

        # Prints the correct word
        for char in random_word:
            print(char.upper(), "", end='')
        print("\n")
        if (random_word == "".join(correct_guesses)):
            print("You win!")
        else:
            print("You lose!")

        # Prompts user to play again
        play_again = check_input.get_yes_no("Play again (Y/N)? ")

main()