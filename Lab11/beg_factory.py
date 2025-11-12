# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025

from enemy_factory import EnemyFactory
from beg_goblin import BegGoblin
from beg_troll import BegTroll
from random import randint

class BeginnerFactory(EnemyFactory):
    '''Creates easy enemies, extends from EnemyFactory'''
    def create_random_enemy(self):
        '''randomly construct and return one of the beginner 
        enemies (BegGoblin or BegTroll)'''
        random_enemy = randint(1, 2)
        if random_enemy == 1:
            enemy = BegGoblin()
        else:
            enemy = BegTroll()
        return enemy