# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 29, 2025

import die

class Player:
    def __init__(self):
        self._dice = [die.Die(6), die.Die(6), die.Die(6)]
        self._points = 0

    def points(self):
        return self._points
    
    def roll_dice(self):
        self._dice[0].roll()
        self._dice[1].roll()
        self._dice[2].roll()
        self._dice.sort(reverse=True)

    def has_pair(self):
        if(self._dice[0] == self._dice[1] or
           self._dice[0] == self._dice[2] or
           self._dice[1] == self._dice[2]):
            self._points += 1
            return True
        return False
    
    def has_three_of_a_kind(self):
        if(self._dice[0] == self._dice[1] and
           self._dice[0] == self._dice[2]):
            self._points += 3
            return True
        return False
    
    def has_series(self):
        if((self._dice[2] - self._dice[1]) == 1 and
           (self._dice[1] - self._dice[0]) == 1):
            self._points += 2
            return True
        return False
    
    def __str__(self):
        return (f"D1={self._dice[0]}, D2={self._dice[1]}, D3={self._dice[2]}")