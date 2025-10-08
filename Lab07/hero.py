# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from entity import Entity
import random

# Inherits from Entity 
class Hero(Entity):
    def sword_attack(self, dragon):
        """ 
        Deals a random amount of damage in the range 2D6 (1-6 + 1-6) to the dragon

        Args:
            dragon (Dragon object): the dragon to subtract the damage from

        Returns: 
            A string with the description of the attack
        """
        dmg = random.randint(1, 6) + random.randint(1, 6)
        dragon.take_damage(dmg)
        return (f"{self.name} swings at {dragon.name} and deals {dmg} damage.")

    def arrow_attack(self, dragon):
        """ 
        Deals a random amount of damage in the range 1D12 (1-12) to the dragon

        Args:
            dragon (Dragon object): the dragon to subtract the damage from

        Returns: 
            A string with the description of the attack
        """
        dmg = random.randint(1, 12)
        dragon.take_damage(dmg)
        return (f"{self.name} aims an arrow and hits {dragon.name} for {dmg} damage.")