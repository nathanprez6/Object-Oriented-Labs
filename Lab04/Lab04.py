# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Sept. 15, 2025
# Description: A program that allows the user to solve a maze that is read in from a file

import check_input

def read_maze():
    """ 
    Reads in the contents of a file and stores the contents in a 2D list

    Args:
        None

    Returns: 
        A filled 2D list
    """
    maze = []
    
    with open("maze.txt", "r") as maze_file:
        for line in maze_file:
            maze.append(list(line.rstrip("\n")))

    return maze


def find_start(maze):
    """ 
    Searches through the elements in the maze using a set of nested for
    loops to find an ‘s’

    Args:
        maze (2D list): a filled 2D list containing a maze

    Returns: 
        The location as a 1D list 
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if(maze[row][col] == 's'):
                return [row, col]
            
    return None

def display_maze(maze, loc):
    """ 
    Displays each character in the maze in a matrix format

    Args:
        maze (2D list): a filled 2D list containing a maze
        loc (1D list): the user's location in the maze

    Returns: 
        None 
    """
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if([row, col] == loc):
                print('X', end='')
            else:
                print(maze[row][col], end='')
        print()

def main():
    print("-Maze Solver-")

    maze = read_maze()

    user_loc = find_start(maze)

    # Loops until user reaches the finish
    while maze[user_loc[0]][user_loc[1]] != 'f':
        display_maze(maze, user_loc)
        
        # Prompt user for their choice of direction to move        
        print("1. Go North\n2. Go South\n3. Go East\n4. Go West")
        user_choice = check_input.get_int_range("Enter choice: ", 1, 4)

        if user_choice == 1:
           if maze[user_loc[0] - 1][user_loc[1]] == '*':
               print("You cannot move there.")
           else:
               user_loc = [user_loc[0] - 1, user_loc[1]]
        elif user_choice == 2:
           if maze[user_loc[0] + 1][user_loc[1]] == '*':
               print("You cannot move there.")
           else:
               user_loc = [user_loc[0] + 1, user_loc[1]]
        elif user_choice == 3:
           if maze[user_loc[0]][user_loc[1] + 1] == '*':
               print("You cannot move there.")
           else:
               user_loc = [user_loc[0], user_loc[1] + 1]
        elif user_choice == 4:
           if maze[user_loc[0]][user_loc[1] - 1] == '*' :
               print("You cannot move there.")
           else:
               user_loc = [user_loc[0], user_loc[1] - 1]

    # Displays final maze and prints congratulatory message
    display_maze(maze, user_loc)
    print("Congratulations! You solved the maze.")

main()