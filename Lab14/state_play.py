# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from puppy_state import PuppyState

class StatePlay(PuppyState):
    '''Overrides feed and play. Increments and resets counters correctly and changes state accordingly.
    feed(self, puppy) - Returns a string describing the puppy's reaction.
    play(self, puppy) - Returns a string describing the puppy's reaction
    '''
    def feed(self, puppy):
        return "The puppy is too busy playing with the ball to eat right now."
    
    def play(self, puppy):
        puppy.inc_plays()
        if puppy.play >= 3:
            from state_asleep import StateAsleep
            puppy.change_state(StateAsleep())
            puppy.reset()
            return "The puppy played so much it fell alseep!"
        return "You throw the ball again and the puppy excitedly chases it."