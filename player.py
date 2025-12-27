# Define the Player class.

from item import Item
from quest import QuestManager

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
        """
        Initialize a new player.
        
        Args:
            name (str): The name of the player.
            
        Examples:
        
        >>> player = Player("Antonin")
        >>> player.name
        'Antonin'
        >>> player.move_count
        0
        >>> player.rewards
        []
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 10
        self.move_count = 0
        self.collect_count = 0
        self.characters_interracted = []
        self.quest_manager = QuestManager(self)
        self.rewards = []  # List to store earned rewards
    
    # Define the move method.
    def move(self, direction, game):
        """
        Move the player in the specified direction.
        
        Args:
            direction (str): The direction to move (N, E, S, O).
            
        Returns:
            bool: True if the move was successful, False otherwise.
            
        Examples:
        
        >>> from room import Room
        >>> player = Player("Dave")
        >>> room1 = Room("Room1", "in room 1")
        >>> room2 = Room("Room2", "in room 2")
        >>> room3 = Room("Room3", "in room 3")
        >>> room1.exits = {"N": room2, "E": None, "S": None, "O": None}
        >>> room2.exits = {"S": room1, "E": room3, "S": None, "O": None}
        >>> player.current_room = room1
        >>> player.move_count
        0
        >>> player.move("N")
        <BLANKLINE>
        Vous êtes in room 2
        <BLANKLINE>
        Sorties: E
        <BLANKLINE>
        True
        >>> player.move_count
        1
        >>> player.current_room.name
        'Room2'
        >>> player.move("E")
        <BLANKLINE>
        Vous êtes in room 3
        <BLANKLINE>
        Sorties:
        <BLANKLINE>
        True
        >>> player.move_count
        2
        """
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description(game))

        # Check room visit objectives
        self.quest_manager.check_room_objectives(self.current_room.name)

        # Increment move counter and check movement objectives
        self.move_count += 1
        self.quest_manager.check_counter_objectives("Se déplacer", self.move_count)

        return True

    def sum_weight(self):
        sum = 0
        for elem in self.inventory.values():
            sum = sum + Item.get_weight(elem)
        return sum
    
    def add_reward(self, reward):
        """
        Add a reward to the player's rewards list.
        
        Args:
            reward (str): The reward to add.
            
        Examples:
        
        >>> player = Player("Bob")
        >>> player.add_reward("Épée magique") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Épée magique
        <BLANKLINE>
        >>> "Épée magique" in player.rewards
        True
        >>> player.add_reward("Épée magique") # Adding same reward again
        >>> len(player.rewards)
        1
        """
        if reward and reward not in self.rewards:
            self.rewards.append(reward)
            print(f"\n🎁 Vous avez obtenu: {reward}\n")


    def show_rewards(self):
        """
        Display all rewards earned by the player.
        
        Examples:
        
        >>> player = Player("Charlie")
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        >>> player.add_reward("Bouclier d'or") # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vous avez obtenu: Bouclier d'or
        <BLANKLINE>
        >>> player.show_rewards() # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        🎁 Vos récompenses:
        • Bouclier d'or
        <BLANKLINE>
        """
        if not self.rewards:
            print("\n🎁 Aucune récompense obtenue pour le moment.\n")
        else:
            print("\n🎁 Vos récompenses:")
            for reward in self.rewards:
                print(f"  • {reward}")
            print()
