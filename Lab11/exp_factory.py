# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025

from enemy_factory import EnemyFactory
from exp_goblin import ExpGoblin
from exp_troll import ExpTroll
from random import randint

class ExpertFactory(EnemyFactory):
    '''Creates difficult enemies, extends from EnemyFactory'''
    def create_random_enemy(self):
        '''randomly construct and return one of the expert 
        enemies (ExpGoblin or ExpTroll)'''
        random_enemy = randint(1, 2)
        if random_enemy == 1:
            enemy = ExpGoblin()
        else:
            enemy = ExpTroll()
        return enemy