# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 20, 2025

from door import Door
import random

class LockedDoor(Door):
    def __init__(self):
        '''Randomizes the location of the key: 1. Under the mat, 
        2. Under the flower pot, 3. Under the fake rock'''
        self._key_location = random.randint(1, 3)
        self._input = 0

    def examine_door(self):
        '''returns a string description of the door.'''
        return "A locked door. The key is hidden nearby. Look around for the key"
        
    def menu_options(self):
        '''returns a string of the menu options that user can choose 
        from whenvattempting to unlock the door.'''
        return "1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock.\n"

    def get_menu_max(self):
        '''returns the number of options in the above menu.'''
        return 3

    def attempt(self, option):
        '''passes in the user's selection from the menu. Uses that value to 
        update the attributes that are needed to determine whether the user has 
        unlocked the door (which is done in the is_unlocked method below). Returns 
        a string describing what the user attempted.'''
        self._input = option
        if option == 1:
            return "You check under the mat."
        elif option == 2:
            return "You lift the flower pot to look under it."
        elif option == 3:
            return "You look under the fake rock."

    def is_unlocked(self):
        '''checks to see if the door was unlocked, returns true if it is, false otherwise.'''
        if self._input == self._key_location:
            return True
        else:
            return False

    def clue(self):
        '''returns the hint that is returned if the user was unsuccessful at their attempt.'''
        return "Look somewhere else."

    def success(self):
        '''returns the congratulatory message if the user was successful'''
        return "Congratulations, you found the key and unlocked the door.\n"