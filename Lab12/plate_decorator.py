# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import abc
from plate import Plate

class PlateDecorator(Plate, abc.ABC):
    '''Abstract Decorator class for Plate.
    Inherits from Plate.
    Methods:
        description() -- Returns the description of the plate.
        area() -- Returns the area of the plate.
        weight() -- Returns the weight capacity of the plate.
        count() -- Returns the count of food items on the plate.
    '''
    def __init__(self, p):
        self._plate = p

    def description(self):
        return self._plate.description()

    def area(self):
        return self._plate.area()

    def weight(self):
        return self._plate.weight()

    def count(self):
        return self._plate.count()