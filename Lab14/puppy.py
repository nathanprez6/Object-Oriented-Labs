# Authors: Tony Gianformaggio, Nathan Nguyen
# Date: December 1, 2025

from state_asleep import StateAsleep

class Puppy():
    '''the object that the user interacts with
    Attributes:
        _state(PuppyState): the state the puppy is in
        _feeds, _plays(int): number of times puppy is fed or played with in a row
    Methods:
        __init__(self) - initializes the state to the asleep state, and then initializes the number of feeds and plays.
        get properties for feed and plays.
        change_state(self, new_state) - updates the puppy's state to the new state.
        throw_ball(self) - calls the play method for whichever state the puppy is in.
        give_food(self) - calls the feed method for whichever state the puppy is in.
        inc_feeds(self) - increments the number of times the puppy has been fed in a row.
        inc_plays(self) - increments the number of times the puppy has played in a row.
        reset(self) - reinitializes the feeds and plays attributes.
    '''
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
        return self._state.play(self)

    def give_food(self):
        return self._state.feed(self)

    def inc_feeds(self):
        self._feed += 1

    def inc_plays(self):
        self._play += 1

    def reset(self):
        self._feed = 0
        self._play = 0