# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from entity import Entity
import random

class Hero(Entity):
    def sword_attack(self, dragon):
        dmg = random.randint(1, 6) + random.randint(1, 6)
        dragon.take_damage(dmg)
        return (f"{self.name} slashes at {dragon.name} and deals {dmg} damage.")

    def arrow_attack(self, dragon):
        dmg = random.randint(1, 12)
        dragon.take_damage(dmg)
        return (f"{self.name} aims an arrow and hits {dragon.name} for {dmg} damage.")