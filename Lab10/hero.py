# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 29, 2025

from entity import Entity
from map import Map
import random

class Hero(Entity):
    '''
    Attributes:
        Inherited from Entity:
            _name (str): The name of the hero.
            _max_hp (int): The maximum health points of the hero.
            _hp (int): The current health points of the hero.
        Additional:
            _loc (list): The current location of the hero in the dungeon as [row, col].
    Methods:
        go_north(): Moves the hero north if possible.
        go_south(): Moves the hero south if possible.
        go_east(): Moves the hero east if possible.
        go_west(): Moves the hero west if possible.
        attack(entity): Attacks another entity, dealing random damage.
    '''
    def __init__(self, name):
        '''Initializes the Hero with a name, maximum health points, and starting location.'''
        super().__init__(name, 25)
        self._loc = [0, 0]
        self._map = Map()

    @property
    def loc(self):
        '''Returns the current location of the hero.'''
        return self._loc
    
    def attack(self, entity):
        '''Attacks another entity, dealing random damage.'''
        dmg = random.randint(2, 5)
        entity.take_damage(dmg)
        print(f"{self.name} attacks {entity._name} for {dmg} damage!")

    def go_north(self):
        '''Moves the hero north if possible.'''
        if(self.loc[0] > 0):
            self.loc[0] -= 1
            return self._map[self.loc[0]][self.loc[1]]
        else:
            return 'o'

    def go_south(self):
        '''Moves the hero south if possible.'''
        if(self.loc[0] < 4):
            self.loc[0] += 1
            return self._map[self.loc[0]][self.loc[1]]
        else:
            return 'o'

    def go_east(self):
        '''Moves the hero east if possible.'''
        if(self.loc[1] < 4):
            self.loc[1] += 1
            return self._map[self.loc[0]][self.loc[1]]
        else:
            return 'o'

    def go_west(self):
        '''Moves the hero west if possible.'''
        if(self.loc[1] > 0):
            self.loc[1] -= 1
            return self._map[self.loc[0]][self.loc[1]]
        else:
            return 'o'