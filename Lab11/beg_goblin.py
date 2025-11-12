# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025

from entity import Entity
from random import randint

class BegGoblin(Entity):
    '''Extend from Entity - a type of monster that the factories construct'''
    def __init__(self):
        '''Initializes entity with a name and random hitpoints'''
        hp = randint(7, 9)
        super().__init__("Goblin", hp)

    def melee_attack(self, enemy):
        '''randomizes the damage, deal the damage to the enemy (the hero),
        and returns a string describing the attack.'''
        dmg = randint(4, 6)
        enemy.take_damage(dmg)
        return f"The {self._name} pokes {enemy._name} with its dagger for {dmg} damage."