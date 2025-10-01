# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 29, 2025

import die

class Player:
    def __init__(self):
        """ 
        Constructor of the Player class

        Args:
            None

        Returns: 
            None
        """ 
        self._dice = [die.Die(6), die.Die(6), die.Die(6)]
        self._dice.sort()
        self._points = 0

    @property
    def points(self):
        """ 
        Get property that retrieves the player's points

        Args:
            None

        Returns: 
            The player's points
        """ 
        return self._points
    
    def roll_dice(self):
        """ 
        Calls roll on each of the Die objects in the list and then sorts the list

        Args:
            None

        Returns: 
            None
        """ 
        self._dice[0].roll()
        self._dice[1].roll()
        self._dice[2].roll()
        self._dice.sort()

    def has_pair(self):
        """ 
        Checks if any two dice have the same value and increments points by 1 if so

        Args:
            None

        Returns: 
            True if two dice have the same value
        """ 
        if(self._dice[0] == self._dice[1] or
           self._dice[0] == self._dice[2] or
           self._dice[1] == self._dice[2]):
            self._points += 1
            return True
        return False
    
    def has_three_of_a_kind(self):
        """ 
        Checks all three dice have the same value and increments points by 3 if so

        Args:
            None

        Returns: 
            True if all three dice have the same value
        """ 
        if(self._dice[0] == self._dice[1] and
           self._dice[0] == self._dice[2]):
            self._points += 3
            return True
        return False
    
    def has_series(self):
        """ 
        Checks if each dive value is in sequence and increments points by 2 if so

        Args:
            None

        Returns: 
            True if all three dice are in sequence
        """ 
        if((self._dice[2] - self._dice[1]) == 1 and
           (self._dice[1] - self._dice[0]) == 1):
            self._points += 2
            return True
        return False
    
    def __str__(self):
        """ 
        A method to print all values of the dice rolls in a certain format

        Args:
            None

        Returns: 
            A string formatted to display all values of the dice
        """ 
        return (f"D1={self._dice[0]}, D2={self._dice[1]}, D3={self._dice[2]}")