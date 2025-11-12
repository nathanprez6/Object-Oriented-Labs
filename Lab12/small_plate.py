# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import plate

class SmallPlate(plate.Plate):
    '''Class representing a small paper plate.
    Inherits from Plate.
    Methods:
        description() -- Returns the description of the small plate.
        area() -- Returns the area of the small plate.
        weight() -- Returns the weight capacity of the small plate.
        count() -- Returns the count of food items on the plate (initially 0).
        '''
    def description(self):
        return "Sturdy 10 inch paper plate"

    def area(self):
        return 78

    def weight(self):
        return 32
    
    def count(self):
        return 0