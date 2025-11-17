# Define the Room class.

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
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
