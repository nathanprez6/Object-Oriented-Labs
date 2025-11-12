# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

import plate

class LargePlate(plate.Plate):
    '''Class representing a large paper plate.
    Inherits from Plate.
    Methods:
        description() -- Returns the description of the large plate.
        area() -- Returns the area of the large plate.
        weight() -- Returns the weight capacity of the large plate.
        count() -- Returns the count of food items on the plate (initially 0).
    '''
    def description(self):
        return "Flimsy 12 inch paper plate"

    def area(self):
        return 113
    
    def weight(self):
        return 24
    
    def count(self):
        return 0