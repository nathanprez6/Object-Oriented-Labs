# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 13, 2025

import abc
import random

class Vehicle(abc.ABC):
    """
        Abstract base class for different types of vehicles.
        Attributes:
            _name (str): The name of the vehicle.
            _initial: Vehicle's label
            _speed: Vehicle's speed
            _position: location on the track
            _energy: Vehicle's power level
            
    """
    def __init__(self, name, initial, speed):
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100  

    @property
    def initial(self):
        ''' Get property for initial'''
        return self._initial
    
    @property
    def position(self):
        ''' Get property for position'''
        return self._position
    
    @property
    def energy(self):  
        ''' Get property for energy'''
        return self._energy

    def fast(self, obs_loc):
        ''' lets the vehicle move forward fast and determines if crashes or not
        Args:
            obs_loc (int): the position of the next obstacle
        Returns:
            (string): a description of the vehicle movement
        '''
        distance = int(self._speed + random.randint(-1, 1))
        if self._energy >= 5: 
            self._energy -= 5
            if obs_loc == None:
                self._position += distance
                return f"{self._name} quickly moves {distance} units!"
            elif self._position + distance < obs_loc:
                self._position += distance
                return f"{self._name} quickly moves {distance} units!"
            else:
                dist_traveled = obs_loc - self.position
                self._position = obs_loc
                return f"{self._name} moved {dist_traveled} units and CRASHED into an obstacle!"
        else:
            self._position += 1
            return f"{self._name} moved 1 unit"

    def slow(self, obs_loc):
        ''' lets the vehicle move forward slow
        Args:
            obs_loc (int): the position of the next obstacle
        Returns:
            (string): a description of the vehicle movement
        '''
        distance = int(self._speed / 2 + random.randint(-1, 1))
        if obs_loc == None:
            self._position += distance
            return (f"{self._name} slowly moves {distance} units!")
        elif self._position + distance < obs_loc:
            self._position += distance
            return (f"{self._name} slowly moves {distance} units!")
        else:
            self._position += distance
            return (f"{self._name} slowly dodges the obstacle and moves {distance} units!")

    def __str__(self):
        ''' Method to print name, position, and remaning energy of inputted object'''
        return f"{self._name} [Position: {self._position}, Energy: {self._energy}]"
    
    @abc.abstractmethod
    def special_move(self, obs_loc):
        ''' Overridden in the subclasses'''
        pass