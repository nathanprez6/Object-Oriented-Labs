# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 13, 2025

from vehicle import Vehicle
import random

class Car(Vehicle):
    ''' An subclass of vehicle that represents a car
    Attributes:
        same as superclass
    '''
    def special_move(self, obs_loc):
        ''' lets the car move forward with a special ability, nitro boost
        Args:
            obs_loc (int): the position of the next obstacle
        '''
        if self._energy >= 15:
            distance = int(self._speed * 1.5 + random.randint(-1, 1))
            self._energy -= 15
            if obs_loc == None:
                self._position += distance
                return (f"{self._name} uses nitro boost and moves {distance} units!")
            elif self._position + distance < obs_loc:
                self._position += distance
                return (f"{self._name} uses nitro boost and moves {distance} units!")
            else:
                self._position = obs_loc
                return (f"{self._name} CRASHED into an obstacle!")
        else:
            self._position += 1
            return (f"{self._name} tries to use nitro boost but, but is all out of energy!")