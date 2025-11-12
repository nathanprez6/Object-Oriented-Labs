# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Nov. 3, 2025
# Description: A game where the user must defeat three monsters to pass the trials.

from check_input import get_int_range
from hero import Hero
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory

def main():
    print("Monster Trials")
    name = str(input("What is your name? "))
    hero = Hero(name)
    
    # Constructs factories
    beg_factory = BeginnerFactory()
    exp_factory = ExpertFactory()

    # Generate a list of three monsters
    monsters = [beg_factory.create_random_enemy(), beg_factory.create_random_enemy(), exp_factory.create_random_enemy()]

    print(f"\nYou will face a series of 3 monsters, {hero.name}.\nDefeat them all to win.\n")

    # Loops until hero dies or three monsters are defeated
    while(hero.hp > 0 and len(monsters) != 0):
        print("Choose an enemy to attack:")
        for i, monster in enumerate(monsters, start=1):
            print(f"{i}. {monster}")

        # Prompts user to choose a monster to attack
        user_choice =  get_int_range("Enter choice: ", 1, len(monsters))
        print()

        if user_choice == 1:
            print(hero)
            print("1. Sword Attack\n2. Arrow Attack")
            attack_choice = get_int_range("Enter choice: ", 1, 2)
            print()

            if attack_choice == 1:
                print(hero.melee_attack(monsters[0]))
            else:
                print(hero.ranged_attack(monsters[0]))
            
            if monsters[0].hp == 0:
                print(f"You have slain the {monsters[0].name}!")
                monsters.pop(0)
            else:
                print(monsters[0].melee_attack(hero))
            print()
        elif user_choice == 2:
            print(hero)
            print("1. Sword Attack\n2. Arrow Attack")
            attack_choice = get_int_range("Enter choice: ", 1, 2)
            print()

            if attack_choice == 1:
                print(hero.melee_attack(monsters[1]))
            else:
                print(hero.ranged_attack(monsters[1]))
            
            if monsters[1].hp == 0:
                print(f"You have slain the {monsters[1].name}!")
                monsters.pop(1)
            else:
                print(monsters[1].melee_attack(hero))
            print()
        elif user_choice == 3:
            print(hero)
            print("1. Sword Attack\n2. Arrow Attack")
            attack_choice = get_int_range("Enter choice: ", 1, 2)
            print()

            if attack_choice == 1:
                print(hero.melee_attack(monsters[2]))
            else:
                print(hero.ranged_attack(monsters[2]))
            
            if monsters[2].hp == 0:
                print(f"You have slain the {monsters[2].name}!")
                monsters.pop(2)
            else:
                print(monsters[2].melee_attack(hero))
            print()

    # Prints final message based on if hero succeeded or failed
    if hero.hp == 0:
        print("You died.\nGame Over.")
    else:
        print("Congratulations! You defeated all the monsters!\nGame Over.")

if __name__ == '__main__':
    main()