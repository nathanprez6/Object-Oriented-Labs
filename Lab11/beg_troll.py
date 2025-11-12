# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025

from entity import Entity
from random import randint

class BegTroll(Entity):
    '''Extend from Entity - a type of monster that the factories construct'''
    def __init__(self):
        '''Initializes entity with a name and random hitpoints'''
        hp = randint(8, 10)
        super().__init__("Troll", hp)

    def melee_attack(self, enemy):
        '''randomizes the damage, deal the damage to the enemy (the hero),
        and returns a string describing the attack.'''
        dmg = randint(5, 9)
        enemy.take_damage(dmg)
        return f"The {self._name} bonks {enemy._name} with its club for {dmg} damage."