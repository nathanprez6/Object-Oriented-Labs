# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025

from abc import ABC, abstractmethod

class Entity(ABC):
    '''Abstract class that the monsters and the hero extend from'''
    def __init__(self, name, hp):
        '''Initializes the Entity with a name and maximum health points.'''
        self._name = name
        self._hp = hp

    @property
    def name(self):
        '''Returns the name of the entity.'''
        return self._name
    
    @property
    def hp(self):
        '''Returns the current health points of the entity.'''
        return self._hp
    
    def take_damage(self, dmg):
        '''Reduces the entity's health points by dmg.'''
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    def __str__(self):
        '''Returns a string representation of the entity's name and current/max HP.'''
        return f"{self._name} HP: {self._hp}"
    
    @abstractmethod
    def melee_attack(self, enemy):
        '''Abstract - the attack the entity does to another entity'''
        pass