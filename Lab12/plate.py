
# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import abc

class Plate(abc.ABC):
    '''Abstract Base Class representing a Plate.
    Methods:
        description() -- Returns the description of the plate.
        area() -- Returns the area of the plate.
        weight() -- Returns the weight capacity of the plate.
        count() -- Returns the count of food items on the plate.
    '''
    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def weight(self):
        pass

    @abc.abstractmethod
    def count(self):
        pass