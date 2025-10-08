# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 6, 2025

class Entity:
    def __init__(self, name, max_hp):
        """ 
        Sets the _name, _max_hp, and _hp attributes

        Args:
            name (string): name to assign to _name
            max_hp (int): value to assign to _max_hp and _hp

        Returns: 
            None
        """
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        """ 
        Get property to retreive entity's name

        Args:
            None

        Returns: 
            The name of the entity object
        """
        return self._name
    
    @property
    def hp(self):
        """ 
        Get property to retreive entity's hp

        Args:
            None

        Returns: 
            The hp of the entity object
        """
        return self._hp
    
    def take_damage(self, dmg):
        """ 
        Subtracts the dmg value from the entity's _hp

        Args:
            dmg (int): damage to subtract from entity's hp

        Returns: 
            None
        """
        if (self._hp - dmg < 0):
            self._hp = 0
        else:
            self._hp -= dmg

    def __str__(self):
        """ 
        A method to print the name and hp of the entity object

        Args:
            None

        Returns: 
            The entity's name and hp in the format “Name: hp/max_hp”
        """
        return (f"{self._name}: {self._hp}/{self._max_hp}")
