# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from dragon import Dragon
import random

class FireDragon(Dragon):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._fire_shots = 3

    def special_attack(self, hero):
        if self._fire_shots > 0:
            dmg = random.randint(6, 9)
            hero.take_damage(dmg)
            self._fire_shots -= 1
            return (f"{self.name} breathes fire on {hero.name} for {dmg} damage.")
        else:
            return (f"{self.name} tries to breathe fire, but has no fire shots left")
        
    def __str__(self):
        return super().__str__() + (f"\nFire shots remaining: {self._fire_shots}")
