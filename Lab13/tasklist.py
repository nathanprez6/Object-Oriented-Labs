# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

from task import Task

class Tasklist():
    ''' 
    Attributes:
        1. tasklist - a list of Task objects.
        2. n - a counter for the iterator (not initialized in the init).
    Methods:
        1. __init__(self) - read in the list of tasks from the file and store them in the tasklist
        by opening the file, reading in each line that consists of the task description, due date,
        and time separated by commas, constructing the Task object, appending it to the list,
        and then sorting the list.
        2. add_task(self, desc, date, time) - construct a new task using the parameters,
        append it to the tasklist, and then sort the list.
        3. get_current_task(self) - return the task at the beginning of the list.
        4. mark_complete(self) - remove and return the current task from the tasklist.
        5. save_file(self) - write the contents of the tasklist back to the file using the Task's
        repr method (description, date, and time separated by commas).
        6. __len__(self) - return the number of items in the tasklist.
        7. __iter__(self) - initialize the iterator attribute n and return self.
        8. __next__(self) - iterate the iterator one position at a time. Raise a StopIteration
        when the iterator reaches the end of the tasklist, otherwise return the Task object at
        the iterator's current position.
    '''
    def __init__(self):
        self._tasklist = []
        with open("/Users/nathanprez/Object-Oriented-Labs/Lab13/tasklist.txt", "r") as file:
            for line in file:
                line = line.strip()
                desc, date, time = line.split(",")
                task = Task(desc, date, time)
                self._tasklist.append(task)
            self._tasklist.sort()

    def add_task(self, desc, date, time):
        new_task = Task(desc, date, time)
        self._tasklist.append(new_task)
        self._tasklist.sort()

    def get_current_task(self):
        if len(self._tasklist) == 0:
            return None
        return self._tasklist[0]
    
    def mark_complete(self):
        return self._tasklist.pop(0)
    
    def save_file(self):
        with open("/Users/nathanprez/Object-Oriented-Labs/Lab13/tasklist.txt", "w") as file:
            for task in self._tasklist:
                file.write(repr(task) + "\n")

    def __len__(self):
        return len(self._tasklist)
    
    def __iter__(self):
        self._n = 0
        return self
    
    def __next__(self):
        if self._n >= len(self._tasklist):
            raise StopIteration
        result = self._tasklist[self._n]
        self._n += 1
        return result