# Authors: Nathan Nguyen, Maximus Cirson
# Date: Sept. 3, 2025
# Description: 

import check_input
import random

def get_users_bet(money):
    """ 
    Display the total amount of money to the user, then prompts the user to 
    enter their bet. Checks that the bet amount is valid and returns it.

    Args:
        money (int): the user's total money remaining

    Returns: the amount the user wants to bet.
    """
    print("You have $" + str(money) + ".")
    bet_amount = check_input.get_int_range("How much you wanna bet? ", 1, money)
    return bet_amount

def get_users_choice():
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")

    queen_guess = check_input.get_int_range("Find the queen: ", 1, 3)
    return queen_guess

def display_queen_loc(queen_loc):
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