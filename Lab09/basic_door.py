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
        '''returns a string description of the door.'''
        return "A door that is either pushed to open, or pulled."
        
    def menu_options(self):
        '''returns a string of the menu options that user can choose 
        from whenvattempting to unlock the door.'''
        return "1. Push\n2. Pull\n"

    def get_menu_max(self):
        '''returns the number of options in the above menu.'''
        return 2

    def attempt(self, option):
        '''passes in the user's selection from the menu. Uses that value to 
        update the attributes that are needed to determine whether the user has 
        unlocked the door (which is done in the is_unlocked method below). Returns 
        a string describing what the user attempted.'''
        self._input = option
        if option == 1:
            return "You push the door."
        else:
            return "You pull the door."

    def is_unlocked(self):
        '''checks to see if the door was unlocked, returns true if it is, false otherwise.'''
        if self._input == self._state:
            return True
        else:
            return False

    def clue(self):
        '''returns the hint that is returned if the user was unsuccessful at their attempt.'''
        return "Try the other way."

    def success(self):
        '''returns the congratulatory message if the user was successful'''
        return "Congratulations, you opened the door.\n"
