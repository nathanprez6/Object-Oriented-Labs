# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025
# Description: A program that simulates a Thanksgiving dinner buffet where users can choose a 
# plate and add food items to it without going over the weight or area limit of the paper plate,

import small_plate
import large_plate
import plate_decorator
import stuffing
import turkey
import potatoes
import pie
import green_beans
import Lab14.check_input as check_input

def examine_plate(p):
    '''Examines the plate to see if it can hold the food added.
    Prints the description, weight, area, sturdiness, and space available.
    
    Arguments:
        p -- Plate object being examined
    
    Returns:
        True if the plate cannot hold the food, False otherwise.'''
    print(p.description())

    # Get the weight and area of the plate after adding food items.
    weight = p.weight()
    area = p.area()
    if(weight <= 0):
        print("Your Plate can't hold this much food! Your food spills over the edge.")
        return True
    elif(area <= 0):
        print("Your Plate isn't big enough for this much food! Your food spills over the edge.")
        return True
    
    print("Sturdiness: ", end="")

    # Determine sturdiness based on remaining weight capacity.
    if(weight <= 6): 
        print("Bending")
    elif(weight <= 12):
        print("Weak")
    else:
        print("Strong")
    
    print("Space available: ", end="")
    
    # Determine space available based on remaining area.
    if(area <= 20): 
        print("Tiny bit")
    elif(weight <= 40):
        print("Some")
    else:
        print("Plenty")

    return False


def main():
    # Main function to run the Thanksgiving dinner buffet simulation.
    print("- Thanksgiving Dinner -\nServe yourself as much food as you\nlike from the buffet, but make sure\nthat your plate will hold without\nspilling everywhere!")
    choice = check_input.get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n", 1, 2)

    if choice == 1:
        p = small_plate.SmallPlate()
        p = plate_decorator.PlateDecorator(p)
    else:
        p = large_plate.LargePlate()
        p = plate_decorator.PlateDecorator(p)

    stop = False
    # Loop to allow user to add food items until they choose to quit or the plate overflows.
    while not stop:
        choice = check_input.get_int_range("\nChoose food to add:\n1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n", 1, 6)

        if choice == 1:
            p = turkey.Turkey(p)
        elif choice == 2:
            p = stuffing.Stuffing(p)
        elif choice == 3:
            p = potatoes.Potatoes(p)
        elif choice == 4:
            p = green_beans.GreenBeans(p)
        elif choice == 5:
            p = pie.Pie(p)
        else:
            print("\nFinal Plate:")
            examine_plate(p)
            break
        
        p.description()
        stop = examine_plate(p)

    if not stop:
        print(f"Good job! You made it to the table with {p.count()} items on your plate.")
        print(f"There was still {p.area()} square inches left on your plate.")
        print(f"Your plate could have held {p.weight()} more ounces of food.")
        print("Don't worry, you can always get another plate! Happy Thanksgiving!")

main()