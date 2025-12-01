# Authors: Nathan Nguyen, Maximus Cirson
# Date: Sept. 3, 2025
# Description: A program that allows the user to play the game Three Card Monte.
# The player places a bet and then guesses the location of the queen in a set of three cards.

import Lab14.check_input as check_input
import random

def get_users_bet(money):
    """ 
    Displays the total amount of money to the user, then prompts the user to 
    enter their bet. Checks that the bet amount is valid and returns it.

    Args:
        money (int): The user's total money remaining

    Returns: 
        The amount the user wants to bet.
    """
    print("You have $" + str(money) + ".")
    bet_amount = check_input.get_int_range("How much you wanna bet? ", 1, money)
    return bet_amount

def get_users_choice():
    """ 
    Displays three cards face down with numbers 1, 2, and 3.
    Prompt the user to choose a card. Check that the user’s choice is a number
    between 1-3 and return that value

    Args:
        None
    
    Returns: 
        The user's guess of the queen's location
    """
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")

    queen_guess = check_input.get_int_range("Find the queen: ", 1, 3)
    return queen_guess

def display_queen_loc(queen_loc):
    """ 
    Displays three cards face up to show the location of the queen

    Args:
        queen_loc (int): The location of the queen
    
    Returns: 
        None
    """
    if(queen_loc == 1):
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  Q  | |  K  | |  K  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
    elif(queen_loc == 2):
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  K  | |  Q  | |  K  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")
    else:
        print("+-----+ +-----+ +-----+")
        print("|     | |     | |     |")
        print("|  K  | |  K  | |  Q  |")
        print("|     | |     | |     |")
        print("+-----+ +-----+ +-----+")

def main():
    print("-Three card Monte-\nFind the queen to double your bet!\n")
    total_money = 100
    play_again = True

    # Loops until user quits or runs out of money
    while(play_again):
        queen_loc = random.randint(1, 3)

        bet = get_users_bet(total_money)
        total_money -= bet

        user_choice = get_users_choice()
        display_queen_loc(queen_loc)

        if(user_choice == queen_loc):
            total_money += (bet * 2)
            print("You got lucky this time...")
        else:
            print("Sorry... you lose.")
        
        if(total_money == 0):
            print("You're out of money. Beat it loser!")
            play_again = False
        else:
            play_again = check_input.get_yes_no("Play again? (Y/N): ")

main()