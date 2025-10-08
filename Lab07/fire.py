# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from dragon import Dragon
import random

# Inherits from Dragon
class FireDragon(Dragon):
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
        self._fire_shots = 3

    def special_attack(self, hero):
        """ 
        If the dragon has any fire_shots left, then apply a random amount of damage
        to the hero in the range 6-9

        Args:
            hero (Hero object): the hero to deal damage to

        Returns: 
            A string with the description of the attack, or failure to attack
        """
        if self._fire_shots > 0:
            dmg = random.randint(6, 9)
            hero.take_damage(dmg)
            self._fire_shots -= 1
            return (f"{self.name} breathes fire on {hero.name} for {dmg} damage.")
        else:
            return (f"{self.name} tries to breathe fire, but has no fire shots left")
        
    def __str__(self):
        """ 
        Uses super to get the __str__ from the entity class, then concatenate on the 
        number of fire_shots remaning

        Args:
            None

        Returns: 
            A string formatted to display the name, hp, and special attacks left of the dragon
        """
        return super().__str__() + (f"\nFire shots remaining: {self._fire_shots}")
