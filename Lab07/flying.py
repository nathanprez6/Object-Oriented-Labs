# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from dragon import Dragon
import random

# Inherits from Dragon
class FlyingDragon(Dragon):
    def __init__(self, name, hp):
        """ 
        Calls super to set the name and hp, then assign a default number of swoops

        Args:
            name (string): name to assign to _name
            max_hp (int): value to assign to _max_hp and _hp

        Returns: 
            None
        """
        super().__init__(name, hp)
        self._swoops = 3

    def special_attack(self, hero):
        """ 
        If the dragon has any swoops left, then apply a random amount of damage
        to the hero in the range 5-8

        Args:
            hero (Hero object): the hero to deal damage to

        Returns: 
            A string with the description of the attack, or failure to attack
        """
        if self._swoops > 0:
            dmg = random.randint(5, 8)
            hero.take_damage(dmg)
            self._swoops -= 1
            return (f"{self.name} swoops down on {hero.name} for {dmg} damage.")
        else:
            return (f"{self.name} tries to swoop down, but has no swoops left!")
        
    def __str__(self):
        """ 
        Uses super to get the __str__ from the entity class, then concatenate on the 
        number of swoops remaning

        Args:
            None

        Returns: 
            A string formatted to display the name, hp, and special attacks left of the dragon
        """
        return super().__str__() + (f"\nSwoops remaining: {self._swoops}")