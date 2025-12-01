# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from puppy_state import PuppyState
from state_eat import StateEat

class StateAsleep(PuppyState):
    def feed(self, puppy):
        puppy.inc_feeds()
        puppy.change_state(StateEat())
        return "The puppy wakes up and comes running to eat."
    
    def play(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now."