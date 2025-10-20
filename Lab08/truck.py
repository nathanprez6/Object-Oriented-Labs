# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 13, 2025

from vehicle import Vehicle
import random 

class Truck(Vehicle):
    ''' An subclass of vehicle that represents a truck
    Attributes:
        same as superclass
    '''
    def special_move(self, obs_loc):
        ''' lets the truck move forward with a special ability, ramming
        Args:
            obs_loc (int): the position of the next obstacle
        '''
        if self._energy >= 15:
            distance = int(self._speed * 2 + random.randint(-1, 1))
            self._energy -= 15
            self._position += distance
            if obs_loc == None:
                return (f"{self._name} rams forward {distance} units!")
            elif obs_loc < self._position + distance:
                return(f"{self._name} rams forward {distance} units through an obstacle!")
            else:
                return (f"{self._name} rams forward {distance} units!")
        else:
            self._position += 1
            return (f"{self._name} tries to ram forward, but is all out of energy!")