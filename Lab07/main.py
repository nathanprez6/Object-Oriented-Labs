# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025
# Description:

from hero import Hero
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon
import check_input
import random

def main():

    player_name = input("What is you name, challenger? ")

    player = Hero(player_name, 50)

    print(f"Welcome to dragon training, {player_name}\nYou must defeat 3 dragons.")
    dragon = Dragon("Garchomp", 10)
    fireDragon = FireDragon("Charizard", 15)
    flyingDragon = FlyingDragon("Salamence", 20)
    enemies = [dragon, fireDragon, flyingDragon]

    while player._hp > 0 and len(enemies) > 0:
        print(player)
        for i, dragon in enumerate(enemies, start = 1):
            print (f"{i}. Attack {str(dragon)}")
        dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(enemies)) - 1

        attack_choice = check_input.get_int_range(f"Attack with: \n1. Arrow (1 D12) \n2. Sword (2 D6) \nEnter weapon: ", 1, 2)

        match attack_choice:
            case 1: 
                print(player.arrow_attack(enemies[dragon_choice]))
            case 2:
                print(player.sword_attack(enemies[dragon_choice]))

        if enemies[dragon_choice]._hp <= 0:
            print(f"You have defeated {enemies[dragon_choice].name}!")
            enemies.pop(dragon_choice)

        if player.hp == 0:
            print("You died")

        if(len(enemies) > 0):
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