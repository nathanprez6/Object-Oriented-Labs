# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 29, 2025

import random

class Die:
    def __init__(self, sides=6):
        """ 
            Constructor for Die class

            Args:
                sides (int): The amount of sides on the die to be rolled

            Returns: 
                None
        """ 
        self._sides = sides
        self._value = 0
        self._value = self.roll()

    def roll(self):
        """ 
        Rolls the die and returns the number

        Args:
            None

        Returns: 
            A random value from 1 to the amount of sides on the die
        """ 
        self._value = random.randint(1, self._sides)
        return self._value
    
    def __str__(self):
        """ 
        A method to print the value of the die

        Args:
            None

        Returns: 
            The value of the die roll as a string
        """ 
        return (f"{self._value}")
    
    def __lt__(self, other):
        """ 
        Compares value of self with value of other

        Args:
            other (Die object): the object to compare with self

        Returns: 
            True if the value of self is less than the value of other
        """ 
        return (self._value > other._value)
    
    def __eq__(self, other):
        """ 
        Compares value of self with value of other

        Args:
            other (Die object): the object to compare with self

        Returns: 
            True if the value of self is equal to the value of other
        """ 
        return (self._value == other._value)
    
    def __sub__(self, other):
        """ 
        Compares value of self with value of other

        Args:
            other (Die object): the object to compare with self

        Returns: 
            The difference between the value of self and the value of other
        """ 
        return (self._value - other._value)
    