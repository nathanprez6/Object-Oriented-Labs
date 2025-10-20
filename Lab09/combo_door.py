# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 20, 2025

from door import Door
import random

class ComboDoor(Door):
    def __init__(self):
        '''Randomizes the value to a number 1-10'''
        self._correct_value = random.randint(1, 10)
        self._input = 0

    def examine_door(self):
        '''returns a string description of the door.'''
        return "A door with a combination lock. You can spin the dial to a number 1-10."
        
    def menu_options(self):
        '''returns a string of the menu options that user can choose 
        from whenvattempting to unlock the door.'''
        return "Enter # 1-10: "

    def get_menu_max(self):
        '''returns the number of options in the above menu.'''
        return 10

    def attempt(self, option):
        '''passes in the user's selection from the menu. Uses that value to 
        update the attributes that are needed to determine whether the user has 
        unlocked the door (which is done in the is_unlocked method below). Returns 
        a string describing what the user attempted.'''
        self._input = option
        return f"You turn the dial to... {option}"

    def is_unlocked(self):
        '''checks to see if the door was unlocked, returns true if it is, false otherwise.'''
        if self._input == self._correct_value:
            return True
        else:
            return False

    def clue(self):
         '''returns the hint that is returned if the user was unsuccessful at their attempt.'''
         if self._input > self._correct_value:
             return "Too high."
         elif self._input < self._correct_value:
             return "Too low."

    def success(self):
        '''returns the congratulatory message if the user was successful'''
        return "Good job, you found the correct value and opened the door.\n"