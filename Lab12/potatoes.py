# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import plate_decorator

class Potatoes(plate_decorator.PlateDecorator):
    '''Class representing Potatoes as a food item on a plate.
    Inherits from PlateDecorator.
    Methods:
        description() -- Returns the description of the plate with Potatoes.
        area() -- Returns the remaining area on the plate after adding Potatoes.
        weight() -- Returns the remaining weight capacity on the plate after adding Potatoes.
        count() -- Returns the count of food items on the plate after adding Potatoes.
    '''
    def description(self):
        if super().count() >= 1:
            return super().description() + " and Potatoes"  
        else:
            return super().description() + " with Potatoes"

    def area(self):
        return super().area() - 18

    def weight(self):
        return super().weight() - 6

    def count(self):
        return super().count() + 1