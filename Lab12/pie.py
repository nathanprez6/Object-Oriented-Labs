# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import plate_decorator

class Pie(plate_decorator.PlateDecorator):
    '''Class representing Pie as a food item on a plate.
    Inherits from PlateDecorator.
    Methods:
        description() -- Returns the description of the plate with Pie.
        area() -- Returns the remaining area on the plate after adding Pie.
        weight() -- Returns the remaining weight capacity on the plate after adding Pie.
        count() -- Returns the count of food items on the plate after adding Pie.
    '''
    def description(self):
        if super().count() >= 1:
            return super().description() + " and Pie"
        else:
            return super().description() + " with Pie"

    def area(self):
        return super().area() - 19

    def weight(self):
        return super().weight() - 8

    def count(self):
        return super().count() + 1