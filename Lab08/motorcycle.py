# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 13, 2025

from vehicle import Vehicle
import random 

class Motorcycle(Vehicle):
    ''' An subclass of vehicle that represents a motorcycle
    Attributes:
        same as superclass
    '''
    def slow(self, obs_loc):
        distance = int(self._speed * 0.75 + random.randint(-1, 1))
        if obs_loc == None:
            self._position += distance
            return (f"{self._name} slowly moves {distance} units!")
        elif self._position + distance < obs_loc:
            self._position += distance
            return (f"{self._name} slowly moves {distance} units!")
        else:
            self._position += distance
            return (f"{self._name} slowly dodges the obstacle and moves {distance} units!")

    def special_move(self, obs_loc):
        ''' lets the motorcycle move forward with a special ability, a wheelie
        Args:
            obs_loc (int): the position of the next obstacle
        '''
        if self._energy >= 15:
            distance = int(self._speed * 2 + random.randint(-1, 1))
            self._energy -= 15
            if random.randint(1, 100) <= 75:
                if obs_loc == None:
                    self._position += distance
                    return (f"{self._name} performs a wheelie and moves {distance} units!")
                elif self._position + distance < obs_loc:
                    self._position += distance
                    return (f"{self._name} performs a wheelie and moves {distance} units!")
                else:
                    self._position = obs_loc
                    return (f"{self._name} CRASHED into an obstacle!")
            else:
                self._position += 1
                return (f"{self._name} fails the wheelie and stumbles forward!")
        else:
            self._position += 1
            return (f"{self._name} tries to perform a wheelie but is all out of energy!")