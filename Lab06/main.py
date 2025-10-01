# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 29, 2025
# Description: A dice game that awards the user points for a pair, three-of-a-kind, or a series

import check_input
import player

def take_turn(player_obj):
    """ 
        Rolls the player's dice, displays the dice, checks for and displays any win types 
        (pair, series, three-of-a-kind), and displays the updated score

        Args:
            player_obj (Player object): An object of the Player class

        Returns: 
            None
        """ 
    player_obj.roll_dice()
    print(player_obj)
    if(player.Player.has_three_of_a_kind(player_obj)):
        print("You got 3 of a kind!")
    elif(player.Player.has_pair(player_obj)):
        print("You got a pair!")
    elif(player.Player.has_series(player_obj)):
        print("You got a series of 3!")
    else:
        print("Aww too bad.")
    print("Score = ", player_obj.points)

def main():
    print("-Yahtzee-\n")

    player_obj = player.Player()

    play_again = True
    while play_again:
        take_turn(player_obj)
        play_again = check_input.get_yes_no("Play again? (Y/N): ")
        print()

    print("Game Over.")
    print("Final Score = ", player_obj.points)

main()