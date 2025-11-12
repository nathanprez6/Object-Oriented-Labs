# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import plate_decorator

class Stuffing(plate_decorator.PlateDecorator):
    '''Class representing Stuffing as a food item on a plate.
    Inherits from PlateDecorator.
    Methods:
        description() -- Returns the description of the plate with Stuffing.
        area() -- Returns the remaining area on the plate after adding Stuffing.
        weight() -- Returns the remaining weight capacity on the plate after adding Stuffing.
        count() -- Returns the count of food items on the plate after adding Stuffing.
    '''
    def description(self):
        if super().count() >= 1:
            return super().description() + " and Stuffing"
        else:
            return super().description() + " with Stuffing"

    def area(self):
        return super().area() - 18

    def weight(self):
        return super().weight() - 7

    def count(self):
        return super().count() + 1