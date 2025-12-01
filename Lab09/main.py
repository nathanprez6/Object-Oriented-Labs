# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 20, 2025
# Description: A program that simulates an escape room by 
# having the user open a series of three doors random chosen 
# from several different types of doors

import Lab14.check_input as check_input
import random
from basic_door import BasicDoor
from combo_door import ComboDoor
from locked_door import LockedDoor

def open_door(door):
    """
    Displays the description of the door and the menu, then gets the user's selection, then passes
    that value to the attempt method and displays the result. If the attempt was successful,
    then it should display the success message, otherwise, it should display the clue message
    and repeat from the menu until the user successfully opens the door.

    Args: 
        door (door object): door object from one of the subclasses of Door

    Returns:
        None
    """
    print(door.examine_door())

    # A loop that repeats until the door is unlocked
    while not door.is_unlocked():
        user_selection = check_input.get_int_range(door.menu_options(), 1, door.get_menu_max())

        print(door.attempt(user_selection))
        if door.is_unlocked():
            print(door.success())
        else:
            print(door.clue())

def main():
    print("Welcome to the Escape Room.\n" \
    "You must unlock 3 doors to escape...\n")

    # A loop that repeats three times for the three doors that the user will try to open
    for _ in range(3):
        # Randomly constructs a door
        door_number = random.randint(1,3)
        if door_number == 1:
            door = BasicDoor()
        elif door_number == 2:
            door = LockedDoor()
        elif door_number == 3:
            door = ComboDoor()

        open_door(door)

    print("Congratulations! You escaped...this time.")

if __name__ == '__main__':
    main()