# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: November 12, 2025

class Task():
    ''' 
    Attributes:
        1. description - string description of the task.
        2. date - due date of the task. A string in the format: MM/DD/YYYY
        3. time - time the task is due. A string in the format: HH:MM
    Methods:
        1. __init__(self, desc, date, time) - assign the parameters to the attributes.
        2. __str__(self) - returns a string used to display the task's information to the user.
        3. __repr__(self) - returns a string used to write the task to the file.
        4. __lt__ (self, other) - returns true if the self task is less than the other task.
        Compare by year, then month, then day, then hour, then minute, and then the task
        description by alphabetical order.
    '''
    def __init__(self, desc, date, time):
        self._description = desc
        self._date = date
        self._time = time

    @property
    def date(self):
        return self._date

    def __str__(self):
        return f"{self._description} - Due: {self._date} at {self._time}"
    
    def __repr__(self):
        return  f"{self._description},{self._date},{self._time}"
    
    def __lt__(self, other):
        date = list(map(int, self._date.split('/')))
        other_date = list(map(int, other._date.split('/')))
        time = list(map(int, self._time.split(':')))
        other_time = list(map(int, other._time.split(":")))

        if date[2] != other_date[2]:
            return date[2] < other_date[2]
        if date[0] != other_date[0]:
            return date[0] < other_date[0]
        if date[1] != other_date[1]:
            return date[1] < other_date[1]
        if time[0] != other_time[0]:
            return time[0] < other_time[0]
        if time[1] != other_time[1]:
            return time[1] < other_time[1]
                    
        return self._description < other._desciption

