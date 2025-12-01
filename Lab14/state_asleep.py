# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from puppy_state import PuppyState

class StateAsleep(PuppyState):
    '''Overrides feed and play. Increments and resets counters correctly and changes state accordingly.
    feed(self, puppy) - Returns a string describing the puppy's reaction.
    play(self, puppy) - Returns a string describing the puppy's reaction
    '''
    def feed(self, puppy):
        puppy.inc_feeds()
        from state_eat import StateEat
        puppy.change_state(StateEat())
        return "The puppy wakes up and comes running to eat."
    
    def play(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now."