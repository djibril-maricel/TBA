# TBA - Jeu d'infiltration

Un jeu d'infiltration dans un paquebot luxueux allant de Paris à Londres, réunissant des puissants et des membres du gouvernements des deux pays pour un sommet aux enjeux économiques et politiques.

Ce repo contient la version finale du jeu pour évaluation.

Un jeu de MARICEL Djibril et LAYSSOL Antonin.

## Guide utilisateur

Il y a 9 modules contenant chacun une classe, sauf pour 2 d'entre eux.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : propriétés génériques du joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les interactions entre le joueur et le jeu ;
- `item.py` / `Item` : propriétés génériques d'un item ;
- `character.py` / `Character` : propriétés génériques d'un personnage non joueur (PNJ)

le module `quest.py` contient 2 classes :
- `Quest` : propriétés génériques d'une quête et gestion de ses objectifs
- `QuestManager` : gestion d'une liste de quêtes et de l'ensemble des objectifs des différents quêets

le module `debug.py` contient une variable `DEBUG` qui sert au débogage.

### Comment installer le jeu

Pour installer le jeu, il suffit de cloner le projet, puis de lancer le fichier `game.py` depuis un terminal. Les différentes commandes permettant d'interagir avec le jeu devront être saisies dans l'entrée utilisateur du terminal.

### L'univers et la quête

L'histoire se déroule sur un paquebot luxueux allant de Paris à Londres, réunissant des puissants et des membres du gouvernements des deux pays pour un sommet aux enjeux économiques et politiques. Vous êtes un espion envoyé en mission pour piéger un ennemi gouvernemental. Un soir, vous êtes invité à la grande réception qui se tient dans la salle de réception. Il s'y trouve quelques milliardaires et des ministres, mais ce qui vous intéresse, c'est votre cible : Luca Lisai, un milliardaire peu scrupuleux soupçonné de comploter avec le 1er ministre du Royaume-Uni. Votre objectif est de vous rendre dans la salle des serveurs avec la clé de session de votre cible, et de télécharger des données concernant un complot entre le milliardaire parisien Luca Lisai et le 1er ministre du Royaume-uni sans vous faire repérer. Attention à ne pas vous rendre dans la salle des serveurs sans la clé de session de votre cible sur vous, ou bien vous aurez perdu.

### Les commandes

Vous avez à votre dispositions différentes commandes pour mener à bien votre mission :

- `help` : permet d'afficher l'aide du jeu ;
- `quit` : permet de quitter le jeu ;
- `go <direction>` : permet de se déplacer dans une direction cardinale, monter ou descendre (N, E, S, O, U, D) ;
- `history` : permet d'afficher l'historique des salles visitées ;
- `back` : permet de retourner à la salle précédente ;
- `check` : permet d'afficher l'inventaire du joueur ;
- `look` : permet d'afficher les objets présents dans la pièce ;
- `take <item>` : permet de prendre un objet présent dans la pièce ;
- `drop <item>` : permet de reposer un objet dans la pièce ;
- `talk <character>` : permet de parler à un personnage présent dans la pièce ;
- `quests` : permet d'afficher la liste des quêtes ;
- `quest <titre>` : permet d'afficher les détails d'une quête ;
- `activate <titre>` : permet d'activer une quête ;
    - avec l'argument `<all>`, vous activerez d'un coup toutes les quêtes qui n'ont pas encore été activées ;
    - avec l'argument `<all_principales>`, vous activerez d'un coup toutes les quêtes principales qui n'ont pas encore été activées ;
- `rewards` : permet d'afficher vos récompenses ;

### Les lieux

Ce paquebot contient 10 salles réparties sur 4 niveaux que vous pouvez explorer librement :

Au niveau `-1`, il y a 2 salles :
- la `salle des machines` ;
- la `salle des serveurs`, salle qu'il faut atteindre avec la clé de session de votre cible sur vous pour accomplir votre mission. Atteignez-la sans la clé de session sur vous, et vous aurez perdu ;

Au niveau `0`, il y a 3 salles :
- la `chambre`, lieu d'apparittion lors d'une nouvelle partie ;
- la `salle de bains` ;
- la `chambre de Luca Lisai`, chambre de votre cible à laquelle vous pourrez accéder que si vous avec la carte de chambre de votre cible sur vous  ;

Au niveau `1`, il y a 3 salles :
- la `salle de réception` ;
- le `restaurant` ;
- le `pont extérieur` ;

Au niveau `2`, il y a 2 salles :
- le `pont supérieur` ;
- la `salle de vidéo-surveillance` ;

### Les personnages et les objets

Il y a 4 personnages disposés dans les différentes salles avec lesquels on peut interagir, dont votre cible : Luca Lisai. Ils ont chacun 2 ou 3 phrases qui se répétent de manière cycliques. Les personnages se déplacent de manière aléatoire à chaque fois que la commande 'go' ou 'back' est exécutée correctement par le joueur.

Il y a également 7 objets disponibles. 6 sont disposées dans les différentes salles, mais un objet, la carte de chambre de votre cible, se trouve dans son inventaire, et on ne peut la récupérer qu'en utilisant un autre objet. A vous de trouver comment.

### Les quêtes

Le jeu dispose de 9 quêtes qui sont réparties en 2 types : les quêtes principales et le quêtes secondaires. Seules les quêtes principales doivent être complétées pour finir le jeu. N'oubliez pas de les activer en utilisant la commande `activate all_principales` ou `activate all`.

### Conditions de victoire et de défaite

Pour sortir victorieux du jeu, il faut finir les 5 quêtes principales, qui ne pourront se finir que dans un ordre précis en suivant l'histoire du jeu (si besoin d'aide, voir la vidéo). Les 4 quêtes secondaires n'ont pas besoin d'être complétées pour sortir victorieux. le jeu se finira automatiquement dés que la dernière quête principale aura été complétée, donc pensez à faire les quêtes secondaires avant si vous voulez toutes les compléter.
<ins>**Surtout, veillez bien à activer les quêtes principales avant de commencer, ou bien vous ne pourrez pas valider les quêtes au fur et à mesure et finir le jeu.**</ins>

Il y a une condition de défaite : se rendre dans la salle des serveurs, se trouvant au niveau -1 (le niveau le plus en bas) sans avoir la clé de session de votre cibre sur vous. Si cela se produit, le jeu se termine directement également, donc faites attention.

## Guide développeur

Voici un diagramme de classes permettant de comprendre l'organisation des différentes classes :

## Perspectives de développement

Les perspectives de développement sont variées. Déjà, la première est l'implémentation d'une interface graphique, qui est la seule chose manquante au jeu actuellement. Cette interface pourra contenir des images de fond pour toutes les salles, ainsi que des boutons pour naviguer à travers les salles et exécuter les différentes commandes.

On pourrait augmenter davantage le nombre de salles, d'objets et de personnages, ce qui permettrait de complexifier l'histoire avec de nouvelles quêtes.

On pourrait créer des salles spéciales fonctinnant différement. Actuellement, nous avons une salle qui n'est pas accessible sans un objet précis, mais on pourrait par exemple avoir une pièce assombrie qui ne laisse apparaître qu'une partie des objets, mais avec un objet comme une lampe torche, laisser apparaître des objets qui seraient dorénavant accessible, et pourquoi pas une porte cachée, qui changerait les sorties possible en ajoutant la nouvelle sortie à la liste des sorties disponibles.

Un ajout très intéressant serait celui des dialogues personnalisées en fonction des situations. On a déjà un cas exceptionnel qui permet d'obtenir l'objet présent dans l'inventaire de notre cible en lui parlant en ayant en notre possession un objet précis. Mais on peut imaginer d'autres scénarios, comme par exemple un dialogue caché après un nombre x d'interactions avec le personnage, ou après avoir parlé à un autre personnage, ou après avoir validé une quête précise etc.

On pourrait également imaginer des quêtes qui seraient activées par une action précise dans le jeu. Par exemple, après avoir parlé a un personnage qui nous demande un service, une quête s'active, et se validera après avoir rempli les conditions et être retourné parlé au même personnage.

Enfin, un système de sauvegarde serait intéressant à implémenter, laissant au joueur la possibilité de quitter sa partie en plein milieu et de reprendre là où il s'était arrêté.

Tous ces ajouts permettrait de créer une expérience de jeu plus immersive et complexe, et rendrait une partie plus intéressante et plaisante pour le joueur.