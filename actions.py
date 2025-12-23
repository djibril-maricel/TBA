# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
from item import Item

class Actions:
    """
    The Actions class contains static methods that define the actions
    that can be performed in the game.
    """

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.go(game, ["go", "N"], 1)
        <BLANKLINE>
        Vous êtes dans une immense tour en pierre qui s'élève au dessus des nuages.
        <BLANKLINE>
        Sorties: N, S, O
        <BLANKLINE>
        True
        >>> Actions.go(game, ["go", "N", "E"], 1)
        <BLANKLINE>
        La commande 'go' prend 1 seul paramètre.
        <BLANKLINE>
        False
        >>> Actions.go(game, ["go"], 1)
        <BLANKLINE>
        La commande 'go' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        # match the upper of direction to put the 1st letter of the direction
        match direction.upper():
            case "N" | "NORD":
                direction = "N"
            case "S" | "SUD":
                direction =  "S"
            case "E" | "EST":
                direction = "E"
            case "O" | "OUEST":
                direction = "O"
            case "U" | "UP":
                direction = "U"
            case "D" | "DOWN":
                direction = "D"

        # Compare the direction with the list of directions acccepted
        directions = set(['N', 'E', 'S', 'O', 'U', 'D'])
        if not direction in directions :
            print(f"\nLa direction ' {direction} ' n'est pas valide.\n")
            return False
        
        # Move the player in the direction specified by the parameter.
        player.move(direction, game)
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quit(game, ["quit"], 0)
        <BLANKLINE>
        Merci TestPlayer d'avoir joué. Au revoir.
        <BLANKLINE>
        True
        >>> Actions.quit(game, ["quit", "N"], 0)
        <BLANKLINE>
        La commande 'quit' ne prend pas de paramètre.
        <BLANKLINE>
        False
        >>> Actions.quit(game, ["quit", "N", "E"], 0)
        <BLANKLINE>
        La commande 'quit' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.help(game, ["help"], 0) # doctest: +NORMALIZE_WHITESPACE
        <BLANKLINE>
        Voici les commandes disponibles:
            - help : afficher cette aide
            - quit : quitter le jeu
            - go <direction> : se déplacer dans une direction cardinale (N, E, S, O)
            - quests : afficher la liste des quêtes
            - quest <titre> : afficher les détails d'une quête
            - activate <titre> : activer une quête
            - rewards : afficher vos récompenses
        <BLANKLINE>
        True
        >>> Actions.help(game, ["help", "N"], 0)
        <BLANKLINE>
        La commande 'help' ne prend pas de paramètre.
        <BLANKLINE>
        False
        >>> Actions.help(game, ["help", "N", "E"], 0)
        <BLANKLINE>
        La commande 'help' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    @staticmethod
    def history(game, list_of_words, number_of_parameters):

        """
        Print the list of previous rooms.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> history(game, ["history"], 0)
        True
        >>> history(game, ["history", "N"], 0)
        False
        >>> history(game, ["history", "chambre"], 0)
        False

        """

        
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the history of the player.
        player = game.player
        if not player.history:
            print("\nVous n'avez visité aucune salle précédemment\n")
            return False
        else:
            print("\nVoici l'historique des pièces visitées :")
            for room in player.history :
                print(f"\t- '{room.description}'")

            print()
            return True

    @staticmethod    
    def get_history(game):

        """
        return a string with the list of previous rooms.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            string: the list of previous rooms

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> history(game)
        True
        >>> history(game, ["history", "N"], 0)
        False
        >>> history(game, ["history", "chambre"], 0)
        False

        """
        
        # Print the history of the player.
        player = game.player
        if not player.history:
            return "Vous n'avez visité aucune salle précédemment."
        
        text = "Historique des pièces visitées :\n"
        for room in player.history:
            text += f"- {room.description}\n"
        return text
        
    @staticmethod
    def back(game, list_of_words, number_of_parameters):

        """
        Print the list of previous rooms.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Move the player back to the previous room in history.
        player = game.player
        # If there is no previous room in history, print a message and return False.
        if not player.history:
            print("\nVous n'avez visité aucune salle précédemment.\n")
            return False

        # Pop the last visited room and set it as the current room.
        previous_room = player.history.pop()
        player.current_room = previous_room
        print(player.current_room.get_long_description(game))
        return True
    
    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the inventory of the player ,or nothing if the inventory is empty
        player = game.player
        if not player.inventory:
            print("Votre inventaire est vide.")
        else:
            print("\nVous disposez des items suivants :")
            for values in player.inventory.values():
                print("\t- " + str(values))
            print()
        return True
    
    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the inventory of the room, or nothing if the room is empty
        player = game.player
        room = player.current_room
        if not room.inventory and not room.characters:
            print("\nil n'y a rien ici.")
        else:
            print("\nLa pièce contient :")
            for values in room.inventory.values():
                print("\t- " + str(values))
            for values in room.characters.values():
                print("\t- " + str(values))
            print()
        return True
    
    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        obj = list_of_words[1]

        # if the room is empty, print an error message
        if not room.inventory:
            print("Vous ne pouvez pas récupérer d'objet : la pièce est vide.")
            return False
        # if the name of the object isn't in the room, print an error message
        elif not (obj in room.inventory.keys()):
            print("L'objet '" +obj+ "' n'est pas présent dans la pièce.")
            return False
        # if the player's max weight limit is reach, print an error message
        elif player.max_weight < (player.sum_weight() + Item.get_weight(room.inventory.get(obj))):
            print("Vous ne pouvez pas récupérer 'objet '" +obj+ "' : votre inventaire est plein.")
            return False
        # else, take the object in the inventory
        else:
            player.inventory[obj] = room.inventory.pop(obj)
            print("\nl'objet '"+ obj +"' est maintenant dans votre inventaire.")
            return True

    @staticmethod 
    def drop(game, list_of_words, number_of_parameters):
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        obj = list_of_words[1]

        # if the inventory is empty, print an error message
        if not player.inventory:
            print("Vous ne pouvez pas déposer d'objets : votre inventaire est vide.")
            return False
        # if the name of the object isn't in the room, print an error message
        elif not (obj in player.inventory.keys()):
            print("L'objet '" +obj+ "' n'est pas présent dans votre inventaire.")
            return False
        # else, take the object in the inventory
        else:
            room.inventory[obj] = player.inventory.pop(obj)
            print("\nl'objet '"+ obj +"' a été déposé dans la pièce.")
            return True

    @staticmethod 
    def talk(game, list_of_words, number_of_parameters):
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        player = game.player
        room = player.current_room
        character = list_of_words[1]

        # if the name of the character isn't in the room, print an error message
        if not (character in room.characters.keys()):
            print("Le personnage '" +character+ "' n'est pas présent dans la pièce.")
            return False
        # else, take the object in the inventory
        else:
            print(room.characters[character].get_msg())
            return True
        
    @staticmethod
    def quests(game, list_of_words, number_of_parameters):
        """
        Show all quests and their status.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quests(game, ["quests"], 0)
        <BLANKLINE>
        📋 Liste des quêtes:
          ❓ Grand Explorateur (Non activée)
          ❓ Grand Voyageur (Non activée)
          ❓ Découvreur de Secrets (Non activée)
        <BLANKLINE>
        True
        >>> Actions.quests(game, ["quests", "param"], 0)
        <BLANKLINE>
        La commande 'quests' ne prend pas de paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all quests
        game.player.quest_manager.show_quests()
        return True

    @staticmethod
    def quest(game, list_of_words, number_of_parameters):
        """
        Show details about a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.quest(game, ["quest", "Grand", "Voyageur"], 1)
        <BLANKLINE>
        📋 Quête: Grand Voyageur
        📖 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        Objectifs:
          ⬜ Se déplacer 10 fois (Progression: 0/10)
        <BLANKLINE>
        🎁 Récompense: Bottes de voyageur
        <BLANKLINE>
        True
        >>> Actions.quest(game, ["quest"], 1)
        <BLANKLINE>
        La commande 'quest' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Prepare current counter values to show progress
        current_counts = {
            "Se déplacer": game.player.move_count
        }

        # Show quest details
        game.player.quest_manager.show_quest_details(quest_title, current_counts)
        return True

    @staticmethod
    def activate(game, list_of_words, number_of_parameters):
        """
        Activate a specific quest.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.activate(game, ["activate", "Grand", "Voyageur"], 1) # doctest: +ELLIPSIS
        <BLANKLINE>
        🗡️  Nouvelle quête activée: Grand Voyageur
        📝 Déplacez-vous 10 fois entre les lieux.
        <BLANKLINE>
        True
        >>> Actions.activate(game, ["activate"], 1)
        <BLANKLINE>
        La commande 'activate' prend 1 seul paramètre.
        <BLANKLINE>
        False

        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n < number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the quest title from the list of words (join all words after command)
        quest_title = " ".join(list_of_words[1:])

        # Try to activate the quest
        if game.player.quest_manager.activate_quest(quest_title):
            return True

        msg1 = f"\nImpossible d'activer la quête '{quest_title}'. "
        msg2 = "Vérifiez le nom ou si elle n'est pas déjà active.\n"
        print(msg1 + msg2)
        # print(f"\nImpossible d'activer la quête '{quest_title}'. \
        #             Vérifiez le nom ou si elle n'est pas déjà active.\n")
        return False

    @staticmethod
    def rewards(game, list_of_words, number_of_parameters):
        """
        Display all rewards earned by the player.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup("TestPlayer")
        >>> Actions.rewards(game, ["rewards"], 0)
        <BLANKLINE>
        🎁 Aucune récompense obtenue pour le moment.
        <BLANKLINE>
        True
        >>> Actions.rewards(game, ["rewards", "param"], 0)
        <BLANKLINE>
        La commande 'rewards' ne prend pas de paramètre.
        <BLANKLINE>
        False
        """
        # If the number of parameters is incorrect, print an error message and return False.
        n = len(list_of_words)
        if n != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Show all rewards
        game.player.show_rewards()
        return True
