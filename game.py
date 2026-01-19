# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest
from debug import DEBUG

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

        history= Command("history", " : afficher l'historique des salles visitées", Actions.history, 0)
        self.commands["history"] = history

        back =Command("back", " : retourner à la salle précédente", Actions.back, 0)
        self.commands["back"] = back

        check = Command("check", " : afficher l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check

        look = Command("look", " : afficher Les objets présents dans la pièce", Actions.look, 0)
        self.commands["look"] = look

        take = Command("take", " <item> : prendre un objet présent dans la pièce", Actions.take, 1)
        self.commands["take"] = take

        drop = Command("drop", " <item> : reposer un objet dans la pièce", Actions.drop, 1)
        self.commands["drop"] = drop

        talk = Command("talk", " <character> : parle à un personnage dans la pièce", Actions.talk, 1)
        self.commands["talk"] = talk

        quests = Command("quests", " : afficher la liste des quêtes", Actions.quests, 0)
        self.commands["quests"] = quests
        
        quest = Command("quest", " <titre> : afficher les détails d'une quête", Actions.quest, 1)
        self.commands["quest"] = quest
        
        activate = Command("activate", " <titre> : activer une quête", Actions.activate, 1)
        self.commands["activate"] = activate

        rewards = Command("rewards", " : afficher vos récompenses", Actions.rewards, 0)
        self.commands["rewards"] = rewards
        
        
        # Setup rooms
        pont_superieur = Room("Pont_superieur",
                               "sur le pont supérieur. D'ici, vous pouvez contempler la nuit étoilée et la pleine lune."
        )
        self.rooms.append(pont_superieur)

        salle_de_video_surveillance = Room("Salle_de_video_surveillance", 
                                           "dans la salle de vidéo-surveillance. Il y a deux employés regardant les dizaines de caméras suveillant la soirée."
        )
        self.rooms.append(salle_de_video_surveillance)

        pont_exterieur = Room("Pont_exterieur", 
                              "sur le pont extérieur. Vous sentez une légère brise maritime au milieu des autres convives."
        )
        self.rooms.append(pont_exterieur)

        salle_de_reception = Room("Salle_de_reception", 
                                  "dans la salle de réception. Il y a beaucoup de beau monde qui festoie autour de tables recouvertes d'amuses-bouches."
        )
        self.rooms.append(salle_de_reception)

        restaurant = Room("Restaurant", 
                          "dans le restaurant ouvert pour la soirée. L'ambiance est plus calme, homard et champagne sont au menu du soir."
        )
        self.rooms.append(restaurant)

        chambre = Room("Chambre", 
                       "dans votre chambre. Quelques affaires sont posées au pied de votre lit et dans vos rangements."
        )
        self.rooms.append(chambre)

        salle_de_bains = Room("Salle_de_bains", 
                              "dans votre salle de bains. vous avez à votre disposition une baignoire et un lavabo."
        )
        self.rooms.append(salle_de_bains)

        chambre_Luca_Lisai = Room("Chambre_Luca_Lisai", 
                                  "dans la chambre de Luca Lisai. Similaire à la vôtre, mais en plus grand et avec du mobilier en marbre."
        )
        self.rooms.append(chambre_Luca_Lisai)

        salle_des_machines = Room("Salle_des_machines", 
                                  "dans la salle des machines. Il y a beaucoup de grosses machines et de gros tuyaux les reliant. Il y a une porte au fond."
        )
        self.rooms.append(salle_des_machines)

        salle_des_serveurs = Room("Salle_des_serveurs", 
                                  "dans la salle des serveurs. Ces gigantesques machines contiennent les données qui vous intéressent."
        )
        self.rooms.append(salle_des_serveurs)


        # Create exits for rooms
        chambre.exits = {"N" : None, "E" : chambre_Luca_Lisai, "S" : salle_de_bains, "O" : None, "U" : salle_de_reception, "D" : salle_des_machines}
        salle_de_bains.exits = {"N" : chambre, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        chambre_Luca_Lisai.exits = {"N" : None, "E" : None, "S" : None, "O" : chambre, "U" : None, "D" : None}
        salle_de_reception.exits = {"N" : pont_exterieur, "E" : restaurant, "S" : None, "O" : None, "U" : pont_superieur, "D" : chambre}
        pont_exterieur.exits = {"N" : None, "E" : restaurant, "S" : None, "O" : salle_de_reception, "U" : None, "D" : None}
        restaurant.exits = {"N" : pont_exterieur, "E" : None, "S" : None, "O" : salle_de_reception, "U" : None, "D" : None}
        pont_superieur.exits = {"N" : None, "E" : None, "S" : salle_de_video_surveillance, "O" : None, "U" : None, "D" : salle_de_reception}
        salle_de_video_surveillance.exits = {"N" : pont_superieur, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        salle_des_machines.exits = {"N" : None, "E" : None, "S" : salle_des_serveurs, "O" : None, "U" : chambre, "D" : None}
        salle_des_serveurs.exits = {"N" : salle_des_machines, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}


        # Create inventory for rooms
        telephone = Item("téléphone", "pour rester joignable durant votre mission", 0.2)
        chambre.inventory["téléphone"] = telephone

        batte = Item("batte_de_baseball", "peut servir d'arme pour assommer quelqu'un", 1.0)
        salle_de_video_surveillance.inventory["batte_de_baseball"] = batte

        cle_USB = Item("clé_USB", "Les données à récupérer seront stockées dessus", 0.01)
        chambre.inventory["clé_USB"] = cle_USB

        menu_du_restaurant = Item("menu_du_restaurant", "On y voit tous les plats beaucoup trop chers à la carte ce soir", 0.2)
        restaurant.inventory["menu_du_restaurant"] = menu_du_restaurant

        sachet_de_poudre_blanche = Item("sachet_de_poudre_blanche", "Une poudre très prisée dans ce genre d'événement", 0.05)
        salle_de_reception.inventory["sachet_de_poudre_blanche"] = sachet_de_poudre_blanche

        cle_de_session = Item("clé_de_session", "Permet de se connecter à la session de Luca Lisai dans la salle des serveurs", 0.01)
        chambre_Luca_Lisai.inventory["clé_de_session"] = cle_de_session

        
        # Create characters for rooms
        Axelle = Character("Axelle", 
                           "Jeune femme prête à tout pour réussir",
                            salle_de_reception,
                            ["Hey ! tu passes une bonne soirée ?", "Ma robe Channel ne coûte que 2000€, je suis trop pauvre !"]
        )
        salle_de_reception.characters["Axelle"] = Axelle

        Anaëlle = Character("Anaëlle", 
                            "Excellente cuisinière, cheffe du restaurant", 
                            restaurant, 
                            ["Hey, qu'est-ce qui te ferait plaisir ce soir ?", "As-tu assez d'argent pour payer ce que je proposes ?"]
        )
        restaurant.characters["Anaëlle"] = Anaëlle

        Mouhamadou = Character("Mouhamadou", 
                               "Jeune homme mystérieux contemplant les étoiles", 
                               pont_superieur, 
                               ["Quel bont vent vous amène, mon ami ?", "Y'a que la douleur qui ne ment pas quand tout le reste n'est que mensonge.", "Ma Rolex est rayé, il faut que je la change !"]
        )
        pont_superieur.characters["Mouhamadou"] = Mouhamadou

        Luca_Lisai = Character("Luca_Lisai", 
                               "Milliardaire Parisien cupide et sans scrupules", 
                               pont_exterieur, 
                               ["Hé hé hé ! Les affaires marchent en ce moment !", "Regardez-moi tous ces pauvres !"]
        )
        pont_exterieur.characters["Luca_Lisai"] = Luca_Lisai

        
        # Create inventory for Characters
        carte_de_chambre = Item("carte_de_chambre", "Permet d'accérer à la chambre de Luca Lisai", 0.01)
        Luca_Lisai.inventory["carte_de_chambre"] = carte_de_chambre


        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = chambre


        # Setup quests
        exploration_quest = Quest(
            title="Grand Explorateur <quête secondaire>",
            description="Explorez toutes les salles de ce paquebot luxueux.",
            objectives=["Visiter Pont_superieur"
                        , "Visiter Salle_de_video_surveillance"
                        , "Visiter Pont_exterieur"
                        , "Visiter Salle_de_reception"
                        , "Visiter Restaurant"
                        , "Visiter Chambre"
                        , "Visiter Salle_de_bains"
                        , "Visiter Chambre_Luca_Lisai"
                        , "Visiter Salle_des_machines"
                        , "Visiter Salle_des_serveurs"],
            reward="Titre de Grand Explorateur"
        )

        travel_quest = Quest(
            title="Grand Voyageur <quête secondaire>",
            description="Déplacez-vous 10 fois entre les lieux.",
            objectives=["Se déplacer 10 fois"],
            reward="Bottes de voyageur"
        )

        items_quest = Quest(
            title="Collectionneur <quête secondaire>",
            description="Ramassez 3 objets dans ce paquebot.",
            objectives=["Ramasser 3 objets"],
            reward="Titre de collectionneur"
        )

        interactions_quest = Quest(
            title="Grand Bavard <quête secondaire>",
            description="Discutez avec 3 personnages différents.",
            objectives=["Parler à 3 personnages différents"],
            reward="Médaille de grand bavard"
        )

        interaction1_quest = Quest(
            title="Beau parleur <quête principale>",
            description="Interragissez avec votre cible : Luca Lisai",
            objectives=["Parler à Luca_Lisai"],
            reward="Titre de beau parleur"
        )

        batte_quest = Quest(
            title="En voilà une arme ! <quête principale>",
            description="Récupérez la batte de baseball située dans la salle de vidéo-surveillance.",
            objectives=["Récupérer batte_de_baseball"],
            reward="Gants d'assassin"
        )

        item1_quest = Quest(
            title="Dérobeur amateur <quête principale>",
            description="Récupérez la carte de chambre permettant de se rendre dans la chambre de Luca Lisai",
            objectives=["Récupérer carte_de_chambre"],
            reward="Titre de dérobeur amateur"
        )

        item2_quest = Quest(
            title="Dérobeur professionnel <quête principale>",
            description="Récupérez la clé de session permettant de se connecter à la session de Luca Lisai",
            objectives=["Récupérer clé_de_session"],
            reward="médaille de dérobeur professionnel"
        )

        discovery_quest = Quest(
            title="Mission accomplie ! <quête principale>",
            description="Atteignez la salle où se trouvent les données que vous convoitez.",
            objectives=["Visiter Salle_des_serveurs"],
            reward="Clé dorée"
        )


        travel_quest = Quest(
            title="Grand Voyageur <quête secondaire>",
            description="Déplacez-vous 10 fois entre les lieux.",
            objectives=["Se déplacer 10 fois"],
            reward="Bottes de voyageur"
        )

        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(travel_quest)
        self.player.quest_manager.add_quest(items_quest)
        self.player.quest_manager.add_quest(interactions_quest)
        self.player.quest_manager.add_quest(discovery_quest)
        self.player.quest_manager.add_quest(item1_quest)
        self.player.quest_manager.add_quest(item2_quest)
        self.player.quest_manager.add_quest(interaction1_quest)
        self.player.quest_manager.add_quest(batte_quest)
        

    # Play the game
    def play(self):
        """Main game loop."""
        
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """Process the command entered by the player."""

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
            res = command.action(self, list_of_words, command.number_of_parameters)
            if command_word in ("go", "back") and res:
                all_characters = []
                for room in self.rooms:
                    all_characters.extend(room.characters.values())
                for c in all_characters:
                    c.move()
            if not self.lose():
                self.win()

    # Print the welcome message
    def print_welcome(self):
        """Print the welcome message."""

        print(f"\nBienvenue {self.player.name} dans ce jeu d'espionnage !\
              \nVous êtes invité à la grande réception qui se tient ce soir dans la salle de réception.\
              \nIl s'y trouve quelques milliardaires et des ministres des deux villes que relient ce paquebot : Paris et Londres.\
              \nVotre objectif est de vous rendre dans la salle des machines avec la clé de session de votre cible, et de télécharger des données\
              \nconcernant un complot entre le milliardaire parisien Luca Lisai et le 1er ministre du Royaume-uni sans vous faire repérer.\
              \nAttention à ne pas vous rendre dans la salle des serveurs sans la clé de session de votre cible, ou bien vous aurez perdu. Bonne chance !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description(self))

    def win(self):
        # Si il reste une quête principale non terminé, le jeu ne s'arrête pas
        if any(
            "<quête principale>" in quest.title and not quest.is_completed
            for quest in self.player.quest_manager.quests
        ):
            return False
        
        # Afficher un message de victoire, puis attendre un imput du joueur avant de finir le jeu et quitter
        print("🎉​ Vous avez réussi ! Vous avez accompli votre mission !\n" \
        "Grâce aux données que vous avez récupérées, vous allez pouvoir exposer les plans machiavéliques de Luca Lisai !\n" \
        "Merci beaucoup d'être allé au bout de ce jeu !\n\n")
        input("Appuyez sur entrée pour quitter.")
        self.finished = True
        return True

    def lose(self):
        if self.player.current_room.name == "Salle_des_serveurs" and not "clé_de_session" in self.player.inventory:
            print("Malheureusement, vous n'avez pas la clé de session de Luca_Lisai sur vous, ce qui a déclenché l'alarme !\n" \
            "La sécurité vous a attrapé, et votre couverture d'espion a été découverte.\n" \
            "Vous avez échoué à votre mission. Vous ferez mieux la prochaine fois !\n\n")
            input("Appuyer sur entrée pour quitter.")
            self.finished = True
            return True
        return False

        

def main():
    """Create a game object and play the game"""
    Game().play()
    

if __name__ == "__main__":
    main()
