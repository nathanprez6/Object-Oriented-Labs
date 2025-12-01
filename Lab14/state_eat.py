# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from puppy_state import PuppyState
from state_asleep import StateAsleep
from state_play import StatePlay

class StateEat(PuppyState):
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy.feed >= 2:
            puppy.change_state(StateAsleep())
            puppy.reset()
            return "The puppy ate so much it fell asleep!"
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."

    def play(self, puppy):
        puppy.inc_plays()
        puppy.change_state(StatePlay())
        return "The puppy looks up from its food and chases the ball you threw."
