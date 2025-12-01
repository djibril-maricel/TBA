# Define the Player class.

from item import Item

class Player():
    """
    This class represents a player. A player is composed of a name.

    Attributes:
        name (str): The player's name.

    Methods:
        __init__(self, name) : The constructor.
        __str__(self) : The string representation of the command.
        move(self, direction) : Permit to the player to move in another room.

    Examples:

    >>> player = Player("Antonin")
    >>> player.name
    'Antonin'
    >>> type(player.name)
    <class 'str'>

    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 1000
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def sum_weight(self):
        sum = 0
        for elem in self.inventory.values():
            sum = sum + Item.get_weight(elem)
        return sum