# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025
# Description: A program that maintains a task list for the user. The user will be able to view the
# current task, list all of the tasks, mark the current task complete, search by date, or add a new
# task. The program will read the list from a file ('tasklist.txt') when the program begins and then
# store the updated list by overwriting the old contents when the user quits the program.

from tasklist import Tasklist
from check_input import get_int_range

def main_menu():
    '''Displays the main menu and returns the user's valid input'''
    print("1. Display current task\n2. Display all tasks\n3. Mark current task complete\n" \
            "4. Add new task\n5. Search by date\n6. Save and quit")
    return get_int_range("Enter choice: ", 1, 6)

def get_date():
    '''Prompts the user to enter the month, day, and year. Return the date in the format:
    MM/DD/YYYY. If the inputted month or day is less than 10, then add a 0 to format it
    correctly.'''
    month = get_int_range("Enter month: ", 1, 12)
    day = get_int_range("Enter day: ", 1, 31)
    year = get_int_range("Enter year: ", 2000, 2100)
    return f"{month:02d}/{day:02d}/{year}"

def get_time():
    '''Prompts the user to enter the hour (military time) and minute. Return the date in the format:
    HH:MM. If the inputted hour or minute is less than 10, then add a 0 to format it correctly'''
    hour = get_int_range("Enter hour: ", 0, 23)
    minute = get_int_range("Enter minute: ", 0, 59)
    return f"{hour:02d}:{minute:02d}"

def main():
    tasklist = Tasklist()

    user_choice = 0
    # Loops until user quits
    while user_choice != 6:
        print(f"-Tasklist-\nTasks to complete: {len(tasklist)}")
        user_choice = main_menu()

        # Display Current Task
        if user_choice == 1:
            current_task = tasklist.get_current_task()
            if current_task is not None:
                print(current_task)
            else:
                print("All tasks have been completed.")
        # Display All Tasks
        elif user_choice == 2:
            if len(tasklist) == 0:
                print("No tasks to display.")
            else:
                for i, task in enumerate(tasklist, start=1):
                    print(f"{i}. {task}")
        # Mark Current Task Complete
        elif user_choice == 3:
            current_task = tasklist.get_current_task()
            if current_task is None:
                print("No tasks to complete.")
            else:
                print("Marking current task as complete:")
                print(tasklist.mark_complete())

                current_task = tasklist.get_current_task()
                if current_task is None:
                    print("All tasks are complete!")
                else:
                    print("New current task is:")
                    print(current_task)
        # Add New Task
        elif user_choice == 4:
            desc = input("Enter a task: ")
            print("Enter due date:")
            date = get_date()
            print("Enter time:")
            time = get_time()
            tasklist.add_task(desc, date, time)
        # Search By Date
        elif user_choice == 5:
            if len(tasklist) == 0:
                print("No tasks left to search.")
            else:
                print("Enter date to search:")
                date = get_date()
                print(f"Tasks due on {date}:")
                count = 1
                for task in tasklist:
                    if task.date == date:
                        print(f"{count}. {task}")
                        count += 1
        # Save and Quit
        elif user_choice == 6:
            tasklist.save_file()
            print("Saving List..")
        print()

if __name__ == "__main__":
    main()