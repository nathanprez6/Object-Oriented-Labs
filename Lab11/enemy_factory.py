# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025

from abc import ABC, abstractmethod

class EnemyFactory(ABC):
    '''Interface - template for all enemy factories'''
    @abstractmethod
    def create_random_enemy(self):
        '''abstract method (no code) that each concrete factory 
        overrides to create and return enemy objects'''
        pass