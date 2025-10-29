# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 29, 2025
# Description: A program that allows the user to wander through a haunted dungeon maze 
# and fight monsters that they encounter as they explore. The user wins if they reach 
# the dungeon’s exit alive. 

import check_input
import random
from hero import Hero
from enemy import Enemy
from map import Map

def main():
    # Initializes the game by creating a hero and the map
    name = str(input("What is your name, traveler? "))
    hero = Hero(name)
    game_map = Map()
    finished = False

    # Loops until the hero's HP drops to 0 or the game is finished or player quits
    while (hero.hp > 0 and not finished):
        print(hero)
        print(game_map.show_map(hero.loc))

        # Presents movement options to the user
        print("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit")
        user_choice = check_input.get_int_range("Enter choice: ", 1, 5)

        # Moves the hero based on user choice
        if user_choice == 1:
            encounter = hero.go_north()
        elif user_choice == 2:
            encounter = hero.go_south()
        elif user_choice == 3:
            encounter = hero.go_east()
        elif user_choice == 4:
            encounter = hero.go_west()
        elif user_choice == 5:
            print("You have quit the game.")
            break

        game_map.reveal(hero._loc)

        # Handles encounters based on what is at the new location
        if encounter == 'm':
            print("A monster appears!")
            monster = Enemy()
            while monster.hp > 0 and hero.hp > 0:
                print(monster)
                print("\n1. Attack\n2. Run away")
                user_action = check_input.get_int_range("Choose an action: ", 1, 2)
                if user_action == 1:
                    Hero.attack(hero, monster)
                    if monster.hp > 0:
                        monster.attack(hero)
                    else:
                        print("You defeated the monster!")
                        game_map.remove_at_loc(hero._loc)
                        break
                elif user_action == 2:
                    print("You run away!")
                    random_move = random.randint(1, 4)
                    if random_move == 1:
                        hero.go_north()
                    elif random_move == 2:
                        hero.go_south()
                    elif random_move == 3:
                        hero.go_east()
                    elif random_move == 4:
                        hero.go_west()
                    game_map.reveal(hero.loc)
                    break
        elif encounter == 'o':
            print("You can't go that way...")
        elif encounter == 'n':
            print("There is nothing here...")
        elif encounter == 's':
            print("You've returned to the start of the dungeon.")
        elif encounter == 'i':
            print("You found a health potion! You are healed.")
            hero.heal()
            game_map.remove_at_loc(hero._loc)
        elif encounter == 'f':
            print()
            print(hero)
            game_map.reveal(hero.loc)
            print(game_map.show_map(hero.loc))
            print("Congratulations! You found the exit and escaped!")
            finished = True
            break

    # Game over message
    print("Game over. Thanks for playing!")

if __name__ == '__main__':
    main()