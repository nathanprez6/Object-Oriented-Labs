# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from abc import ABC, abstractmethod

class PuppyState(ABC):
    '''interface
    Methods:
        feed(self, puppy) - abstract (no code)
        play(self, puppy)  abstract (no code)
    '''
    @abstractmethod
    def feed(self, puppy):
        pass

    @abstractmethod
    def play(self, puppy):
        pass