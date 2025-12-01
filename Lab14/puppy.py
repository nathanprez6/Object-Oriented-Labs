# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from state_asleep import StateAsleep

class Puppy():
    def __init__(self):
        self._state = StateAsleep()
        self._feed = 0
        self._play = 0

    @property
    def feed(self):
        return self._feed
    
    @property
    def play(self):
        return self._play
    
    def change_state(self, new_state):
        self._state = new_state

    def throw_ball(self):
        self._state.play()

    def give_food(self):
        self._state.feed()

    def inc_feeds(self):
        self._feed += 1

    def inc_plays(self):
        self._play += 1

    def reset(self):
        self._feed = 0
        self._play = 0