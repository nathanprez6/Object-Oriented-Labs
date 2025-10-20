# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 20, 2025

from door import Door
import random

class BasicDoor(Door):
    def __init__(self):
        '''Randomizes the initial state of the door,
        1 for push and 2 for pull'''
        self._state = random.randint(1,2)
        self._input = 0

    def examine_door(self):
        return "A door that is either pushed to open, or pulled."
        
    def menu_options(self):
        return "1. Push\n2. Pull\n"

    def get_menu_max(self):
        return 2

    def attempt(self, option):
        self._input = option
        if option == 1:
            return "You push the door."
        else:
            return "You pull the door."

    def is_unlocked(self):
        if self._input == self._state:
            return True
        else:
            return False

    def clue(self):
        return "Try the other way."

    def success(self):
        return "Congratulations, you opened the door.\n"
