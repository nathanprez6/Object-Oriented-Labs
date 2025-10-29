# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 29, 2025

class Map():
    '''
    Attributes:
        _map (list): A 2D list representing the dungeon map.
        _revealed (list): A 2D list tracking revealed locations.
    Methods:
        show_map(loc): Returns a string representation of the map with the hero's location.
        reveal(loc): Marks the location as revealed.
        remove_at_loc(loc): Removes a monster at the specified location.
    '''
    _instance = None
    _initialized = False

    def __new__(cls):
        '''Implements the singleton pattern to ensure only one instance of Map exists.'''
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        '''Initializes the Map by reading from map.txt and setting up the revealed locations.'''
        if getattr(self, '_initialized', False):
            return
        with open("map.txt") as map_file:
            self._map = [list(line.strip()) for line in map_file]
        self._revealed = [[False for _ in row] for row in self._map]
        self._initialized = True

    def __getitem__(self, row):
        '''Allows indexing into the map to get a specific row.'''
        return self._map[row]

    def __len__(self):
        '''Returns the number of rows in the map.'''
        return len(self._map)
    
    def show_map(self, loc):
        '''Returns a string representation of the map with the hero's location.'''
        result = ""
        num_rows = len(self._map)
        num_cols = len(self._map[0])

        for r in range(num_rows):
            for c in range(num_cols):
                if [r, c] == loc:
                    result += '*'
                elif [r, c] == [0, 0]:
                    result += 's'
                elif self._revealed[r][c]:
                    result += self._map[r][c]
                else:
                    result += 'x'
            result += '\n'

        return result
    
    def reveal(self, loc):
        '''Marks the location as revealed.'''
        row, col = loc
        self._revealed[row][col] = True

    def remove_at_loc(self, loc):
        '''Removes a monster at the specified location by setting it to 'n'.'''
        row, col = loc
        self._map[row][col] = 'n'