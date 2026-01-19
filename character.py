from random import choice
from debug import DEBUG

class Character:
    """
    This class represents a non playable character. A character is composed of a name, a description, a current room and a list of messages.

    Attributes:
        name (str): The character's name.
        description (str): A description of the character
        current_room (Room): The actual room where the character is standing
        msgs (list <str>): The list of messages that can be spoken by the player
        inventory (dict <Item>)

    Methods:
        __init__(self, name) : The constructor.
        __str__(self) : The string representation of the command.
        move(self) : Permit to the character to move in another room.

    Examples:

    >>> from Room import room
    >>> salle de reception = Room()
    >>> character = Character("Character", "A character for the doctest", salle_de_reception, ["Message 1", "Message 2"])
    >>> character.name
    'Character'
    >>> type(character.name)
    <class 'str'>

    """

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.inventory = {}

    def __str__(self):
        return f"{self.name} : {self.description}.\n"
    
    def move(self):
        if choice((0, 1)) == 1:
            exits = [room for room in self.current_room.exits.values() if room is not None]
            if exits:
                #if DEBUG:
                #    print("DEBUG: le personnage se déplace")
                del self.current_room.characters[self.name]
                self.current_room = choice(exits)
                self.current_room.characters[self.name] = self
            
                return True
        return False
   
    def get_msg(self):
        if not self.msgs:
            return

        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return(f"{msg}")