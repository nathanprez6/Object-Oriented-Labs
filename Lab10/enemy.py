# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 29, 2025

from entity import Entity
import random

class Enemy(Entity):
    '''
    Attributes:
        Inherited from Entity:
            _name (str): The name of the enemy.
            _max_hp (int): The maximum health points of the enemy.
            _hp (int): The current health points of the enemy.
    Methods:
        attack(entity): Attacks another entity, dealing random damage.
    '''
    def __init__(self):
        '''Initializes the Enemy with a random name and maximum health points.'''
        enemy_names = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie", "Witch"]
        name = enemy_names[random.randint(0, len(enemy_names)-1)]
        max_hp = random.randint(4, 8)
        super().__init__(name, max_hp)

    def attack(self, entity):
        '''Attacks another entity, dealing random damage.'''
        dmg = random.randint(1, 4)
        entity.take_damage(dmg)
        return f"{self._name} attacks {entity.name} for {dmg} damage!"