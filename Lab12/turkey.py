
# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import plate_decorator

class Turkey(plate_decorator.PlateDecorator):
    '''Class representing Turkey as a food item on a plate.
    Inherits from PlateDecorator.
    Methods:
        description() -- Returns the description of the plate with Turkey.
        area() -- Returns the remaining area on the plate after adding Turkey.
        weight() -- Returns the remaining weight capacity on the plate after adding Turkey.
        count() -- Returns the count of food items on the plate after adding Turkey.
    '''
    def description(self):
        if super().count() >= 1:
            return super().description() + " and Turkey"
        else:
            return super().description() + " with Turkey"

    def area(self):
        return super().area() - 15

    def weight(self):
        return super().weight() - 4

    def count(self):
        return super().count() + 1