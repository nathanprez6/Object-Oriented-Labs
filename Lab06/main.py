# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 22, 2025
# Description: 

import check_input
from player import Player

def take_turn(player_obj):
    player_obj.roll_dice()
    print(str(player_obj))
    if(Player.has_pair(player_obj)):
        print("You got a pair!")
    elif(Player.has_three_of_a_kind(player_obj)):
        print("You got 3 of a kind!")
    elif(Player.has_series(player_obj)):
        print("You got a series of 3!")
    print(f"Score = {player_obj.points()}")

def main():
    print("-Yahtzee-\n")

    player_obj = Player()

    play_again = True
    while play_again:
        take_turn(player_obj)
        play_again = check_input.get_yes_no("Play again? (Y/N): ")

    print("Game Over.")
    print(f"Final Score = {player_obj.points()}")



main()