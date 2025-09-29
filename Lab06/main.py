# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 22, 2025
# Description: 

import check_input
import player

def take_turn(player_obj):
    player_obj.roll_dice()
    print(str(player_obj))
    if(player.Player.has_pair(player_obj)):
        print("You got a pair!")
    elif(player.Player.has_three_of_a_kind(player_obj)):
        print("You got 3 of a kind!")
    elif(player.Player.has_series(player_obj)):
        print("You got a series of 3!")
    else:
        print("Aww too bad.")
    print(f"Score = {player_obj.points()}")

def main():
    print("-Yahtzee-\n")

    player_obj = player.Player()

    play_again = True
    while play_again:
        take_turn(player_obj)
        play_again = check_input.get_yes_no("Play again? (Y/N): ")
        print()

    print("Game Over.")
    print(f"Final Score = {player_obj.points()}")

main()