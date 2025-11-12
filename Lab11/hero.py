# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025

from entity import Entity
from random import randint

class Hero(Entity):
    '''The user's character, extends from Entity'''
    def __init__(self, name):
        '''Initializes the Hero with a name and maximum health points.'''
        super().__init__(name, 25)

    def melee_attack(self, enemy):
        '''Deals 2D6 damage to the enemy and returns a string description of the attack..'''
        dmg = randint(1, 6) + randint(1, 6)
        enemy.take_damage(dmg)
        return f"{self._name} slashes the {enemy._name} with a sword for {dmg} damage."
    
    def ranged_attack(self, enemy):
        '''Deals 1D12 damage to the enemy and returns a string description of the attack.'''
        dmg = randint(1, 12)
        enemy.take_damage(dmg)
        return f"{self._name} pierces the {enemy._name} with an arrow for {dmg} damage."