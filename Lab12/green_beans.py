# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import plate_decorator

class GreenBeans(plate_decorator.PlateDecorator):
    '''Class representing Green Beans as a food item on a plate.
    Inherits from PlateDecorator.
    Methods:
        description() -- Returns the description of the plate with Green Beans.
        area() -- Returns the remaining area on the plate after adding Green Beans.
        weight() -- Returns the remaining weight capacity on the plate after adding Green Beans.
        count() -- Returns the count of food items on the plate after adding Green Beans.
    '''
    def description(self):
        if super().count() >= 1:
            return super().description() + " and Green Beans"
        else:
            return super().description() + " with Green Beans"

    def area(self):
        return super().area() - 20

    def weight(self):
        return super().weight() - 3

    def count(self):
        return super().count() + 1