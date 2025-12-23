# Define the Room class.

from actions import Actions
class Room:
    """
    This class represents a room. A room is composed of a command word, a help string, an action and a number of parameters.

    Attributes:
        name (str): The name.
        description (str): The description.
        exits (dict): The action to exit a room.

    Methods:
        __init__(self, name, description) : The constructor.

    Examples:

    >>> room = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
    >>> room.name
    'Swamp'
    >>> room.description 
    "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux."
    >>> room.exits
    {}
    >>> type(room.name)
    <class 'str'>
    >>> type(room.description)
    <class 'str'>
    >>> type(room.exits)
    <class 'dict'>
    """

    # Define the constructor. 
    def __init__(self, name, description):
        """
        Initialize a Room with a name and description.
        
        >>> room = Room("Hall", "dans un grand hall")
        >>> room.name
        'Hall'
        >>> room.description
        'dans un grand hall'
        >>> room.exits
        {}
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Return the room in the given direction if it exists.
        
        >>> room1 = Room("Room1", "dans une pièce")
        >>> room2 = Room("Room2", "dans une autre pièce")
        >>> room1.exits["N"] = room2
        >>> room1.get_exit("N") == room2
        True
        >>> room1.get_exit("S") is None
        True
        """

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Return a string describing the room's exits.
        
        >>> room1 = Room("Room1", "dans une pièce")
        >>> room2 = Room("Room2", "dans une autre pièce")
        >>> room3 = Room("Room3", "dans une troisième pièce")
        >>> room1.exits["N"] = room2
        >>> room1.exits["E"] = room3
        >>> room1.get_exit_string() # doctest: +ELLIPSIS
        'Sorties: ...
        """
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self, game):
        """
        Return a long description of this room including exits.
        
        >>> room1 = Room("Hall", "dans un grand hall")
        >>> room2 = Room("Kitchen", "dans une cuisine")
        >>> room1.exits["N"] = room2
        >>> print(room1.get_long_description()) # doctest: +ELLIPSIS
        <BLANKLINE>
        Vous êtes dans un grand hall
        <BLANKLINE>
        Sorties: ...
        <BLANKLINE>
        Historique des pièces visitées : ...
        <BLANKLINE>
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n\n{Actions.get_history(game)}\n"
