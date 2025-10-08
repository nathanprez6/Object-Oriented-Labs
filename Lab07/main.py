# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025
# Description: A game where the user must defeat three dragons to pass the trails

from hero import Hero
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon
import check_input
import random

def main():
    # Constructs a hero object
    player_name = input("What is you name, challenger? ")

    player = Hero(player_name, 50)

    # Creates a list containing one of each dragon to defeat
    print(f"Welcome to dragon training, {player_name}\nYou must defeat 3 dragons.")
    dragon = Dragon("Garchomp", 10)
    fireDragon = FireDragon("Charizard", 15)
    flyingDragon = FlyingDragon("Salamence", 20)
    enemies = [dragon, fireDragon, flyingDragon]

    # Loops for as long as the hero and dragons are still alive
    while player._hp > 0 and len(enemies) > 0:
        print(player)
        for i, dragon in enumerate(enemies, start = 1):
            print (f"{i}. Attack {str(dragon)}")

        # Prompts hero to pick which dragon to attack
        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(enemies)) - 1

        # Prompts hero to decide what weapon to attack with
        prompt = f"Attack with: \n1. Arrow (1 D12) \n2. Sword (2 D6) \nEnter weapon: "
        attack_choice = check_input.get_int_range(prompt, 1, 2)

        match attack_choice:
            case 1: 
                print(player.arrow_attack(enemies[dragon_choice]))
            case 2:
                print(player.sword_attack(enemies[dragon_choice]))

        # Pops dragon from list if defeated
        if enemies[dragon_choice]._hp <= 0:
            print(f"You have defeated {enemies[dragon_choice].name}!")
            enemies.pop(dragon_choice)

        if player.hp == 0:
            print("You died")

        if(len(enemies) > 0):
            # A random dragon will attack back if any still remain
            enemy_choice = random.randint(0, len(enemies) - 1)
            dragon_attack = random.randint(1, 2)
            match dragon_attack:
                case 1:
                    print(enemies[enemy_choice].basic_attack(player))
                case 2:
                    print(enemies[enemy_choice].special_attack(player))
        else:
            print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")
        
main()