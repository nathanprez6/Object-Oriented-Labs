# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from dragon import Dragon
import random

class FlyingDragon(Dragon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._swoops = 3

    def special_attack(self, hero):
        if self._swoops > 0:
            dmg = random.randint(6, 9)
            hero.take_damage(dmg)
            self._swoops -= 1
            return (f"{self.name} swoops down on {hero.name} for {dmg} damage.")
        else:
            return (f"{self.name} tries to swoop down, but has no swoops left!")
        
    def __str__(self):
        return super().__str__() + (f"\nSwoops remaining: {self._swoops}")