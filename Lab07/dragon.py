# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

from entity import Entity
import random

class Dragon(Entity):
    def basic_attack(self, hero):
        dmg = random.randint(2, 5)
        hero.take_damage(dmg)
        return (f"{self.name} swings its tail and hits {hero.name} for {dmg} damage.")

    def special_attack(self, hero):
        dmg = random.randint(3, 7)
        hero.take_damage(dmg)
        return (f"{self.name} attacks {hero.name} with its claws for {dmg} damage.")