# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 29, 2025

from abc import ABC, abstractmethod

class Entity(ABC):
    '''
    Attributes:
        _name (str): The name of the entity.
        _max_hp (int): The maximum health points of the entity.
        _hp (int): The current health points of the entity.
    Methods:
        take_damage(dmg): Reduces the entity's health points by dmg.
        heal(): Restores the entity's health points to maximum.
        attack(entity): Abstract method to be implemented by subclasses for attacking another entity.
    '''
    def __init__(self, name, max_hp):
        '''Initializes the Entity with a name and maximum health points.'''
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

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

    def heal(self):
        '''Restores the entity's health points to maximum.'''
        self._hp = self._max_hp

    def __str__(self):
        '''Returns a string representation of the entity's name and current/max HP.'''
        return f"Name: {self._name} \nHP: {self._hp}/{self._max_hp}"
    
    @abstractmethod
    def attack(self, entity):
        '''Abstract method to be implemented by subclasses for attacking another entity.'''
        pass