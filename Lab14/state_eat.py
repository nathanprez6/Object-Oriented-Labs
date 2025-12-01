# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from puppy_state import PuppyState

class StateEat(PuppyState):
    '''Overrides feed and play. Increments and resets counters correctly and changes state accordingly.
    feed(self, puppy) - Returns a string describing the puppy's reaction.
    play(self, puppy) - Returns a string describing the puppy's reaction
    '''
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy.feed >= 3:
            from state_asleep import StateAsleep
            puppy.change_state(StateAsleep())
            puppy.reset()
            return "The puppy ate so much it fell asleep!"
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."
    
    def play(self, puppy):
        puppy.inc_plays()
        from state_play import StatePlay
        puppy.change_state(StatePlay())
        return "The puppy looks up from its food and chases the ball you threw."
