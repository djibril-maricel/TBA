# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        pont_superieur = Room("Pont_superieur", "sur le pont supérieur. D'ici, vous pouvez contempler la nuit étoilée et la plaine lune.")
        self.rooms.append(pont_superieur)
        salle_de_video_surveillance = Room("Salle_de_video_surveillance", "dans la salle de vidéo-surveillance. Il y a deux employés regardant les dizaines de caméras suveillant la soirée.")
        self.rooms.append(salle_de_video_surveillance)
        pont_exterieur = Room("Pont_exterieur", "sur le pont extérieur. Vous sentez une légère brise maritime au milieu des autres convives.")
        self.rooms.append(pont_exterieur)
        salle_de_reception = Room("Salle_de_reception", "dans la salle de réception. Il y a beaucoup de beau monde qui festoie autour de tables recouvertes d'amuses-bouches.")
        self.rooms.append(salle_de_reception)
        restaurant = Room("Restaurant", "dans le restaurant ouvert pour la soirée. L'ambiance est plus calme, homard et champagne sont au menu du soir.")
        self.rooms.append(restaurant)
        chambre = Room("Chambre", "dans votre chambre. Quelques affaires sont posés au pied de votre lit et dans vos rangements.")
        self.rooms.append(chambre)
        salle_de_bains = Room("Salle_de_bains", "dans votre salle de bains. vous avez à votre disposition une baignoire et un lavabo.")
        self.rooms.append(salle_de_bains)
        chambre_John_Dupont = Room("Chambre_John_Dupont", "dans la chambre de John Dupont. Similaire à la vôtre, mais en plus grand et avec du mobilier en marbre.")
        self.rooms.append(chambre_John_Dupont)
        salle_des_machines = Room("Salle_des_machines", "dans la salle des machines. Il y a beaucoup de grosses machines et de gros tuyaux les reliant. Il y a une porte au fond.")
        self.rooms.append(salle_des_machines)
        salle_des_serveurs = Room("Salle_des_serveurs", "dans la salle des serveurs. Ces gigantesques machines contiennent les données qui vous intéressent.")
        self.rooms.append(salle_des_serveurs)

        # Create exits for rooms

        chambre.exits = {"N" : None, "E" : chambre_John_Dupont, "S" : salle_de_bains, "O" : None, "U" : salle_de_reception, "D" : salle_des_machines}
        salle_de_bains.exits = {"N" : chambre, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        chambre_John_Dupont.exits = {"N" : None, "E" : None, "S" : None, "O" : chambre, "U" : None, "D" : None}
        salle_de_reception.exits = {"N" : pont_exterieur, "E" : restaurant, "S" : None, "O" : None, "U" : pont_superieur, "D" : chambre}
        pont_exterieur.exits = {"N" : None, "E" : restaurant, "S" : None, "O" : salle_de_reception, "U" : None, "D" : None}
        restaurant.exits = {"N" : pont_exterieur, "E" : None, "S" : None, "O" : salle_de_reception, "U" : None, "D" : None}
        pont_superieur.exits = {"N" : None, "E" : None, "S" : salle_de_video_surveillance, "O" : None, "U" : None, "D" : salle_de_reception}
        salle_de_video_surveillance.exits = {"N" : pont_superieur, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        salle_des_machines.exits = {"N" : None, "E" : None, "S" : salle_des_serveurs, "O" : None, "U" : chambre, "D" : None}
        salle_des_serveurs.exits = {"N" : salle_des_machines, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = chambre

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is void, print nothing
        if command_word == '':
            return False

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'espionnage !\
              \nVous êtes invité à la grande réception qui se tient ce soir dans la salle de réception.\
              \nIl s'y trouve quelques milliardaires et des ministres des deux villes que relient ce paquebot : Paris et Londres.\
              \nVotre objectif est de vous rendre dans la salle des machines, et de télécharger des données concernant un complot entre \
              \nle milliardaire parisien John Dupont et le 1er ministre du Royaume-uni sans vous faire repérer. Bonne chance !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
