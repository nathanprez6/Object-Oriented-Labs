# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from entity import Entity
import random

# Inherits from Entity
class Dragon(Entity):
    def basic_attack(self, hero):
        """ 
        Tail attack that deals a random amount of damage in the range 2-5 to the hero

        Args:
            hero (Hero object): the hero to subtract damage from

        Returns: 
            A string with a description of the attack
        """
        dmg = random.randint(2, 5)
        hero.take_damage(dmg)
        return (f"{self.name} swings its tail and hits {hero.name} for {dmg} damage.")

    def special_attack(self, hero):
        """ 
        Claw attack that deals a random amount of damage in the range 3-7 to the hero

        Args:
            hero (Hero object): the hero to subtract damage from

        Returns: 
            A string with a description of the attack
        """
        dmg = random.randint(3, 7)
        hero.take_damage(dmg)
        return (f"{self.name} attacks {hero.name} with its claws for {dmg} damage.")