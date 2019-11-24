# -tc- ne jamais utiliser * dans un import
from squares import *

# -tc- hériter de object était nécessaire en python 2. On le trouve encore dans de vieux tutos
# -tc- tutos qui ne se sont pas adaptés, mais ce n'est plus nécessaire et plus recommandé
# -tc- en python 3
class Labyrinth(object):
    """docstring for Labyrinth."""

    maps = []

    def __init__(self, **kwargs):
        # -tc- Si on voulait utiliser super, juste super().__init__()
        super(Labyrinth, self).__init__()
        self.buildLabyrinth()

    # -tc- Pour nommer les méthodes, utiliser uniquement des miniscules et séparer les mots
    # -tc- avec des underscores
    def buildLabyrinth(self):
        # -tc- Le labyrinthe doit être défini dans un fichier. Il n'y a pas besoin d'avoir des murs
        # -tc- tout autour, cela te fait perdre de la place (déjà qu'il n'est pas grand :) )
        laby = [
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
            ['w', 'p', '_', 'w', '_', '_', '_', 'w', 'g', 'w'],
            ['w', 'w', '_', 'w', '_', 'w', '_', 'w', '_', 'w'],
            ['w', '_', '_', '_', '_', 'w', 'w', 'w', '_', 'w'],
            ['w', '_', 'w', 'w', 'w', '_', '_', '_', '_', 'w'],
            ['w', '_', 'w', '_', '_', 'w', '_', 'w', 'w', 'w'],
            ['w', '_', 'w', '_', 'w', '_', '_', '_', '_', 'w'],
            ['w', '_', 'w', '_', 'w', 'w', 'w', 'w', '_', 'w'],
            ['w', '_', '_', '_', '_', '_', '_', '_', '_', 'w'],
            ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ]

        # -tc- les noms de variables en minuscules uniquement. Seule les classes et les constantes
        # -tc- utilisent des minuscules.
        # -tc- Pour la boucle for, il serait plus pythonique ici d'utiliser for i_row, row in enumerate(laby)
        for iRow in range(len(laby)):
            row = laby[iRow]
            mapRow = []
            # -tc- for i_column, square in enumerate(row)
            for iColumn in range(len(row)):
                square = row[iColumn]
                coords = [iRow, iColumn]

                # -tc- Pas optimal de mettre tes instances de Wall,
                # -tc- Guard et Square dans la même liste, à moins de construire une liste de squares au sein de Square.
                if(square == 'w'):
                    mapRow.append(Wall(coords))
                elif(square == 'g'):
                    # -tc- Cette position est aussi un square où MacGyver peut se déplacer
                    mapRow.append(Guard(coords))
                else:
                    mapRow.append(Square(coords))

                # -tc- Eviter de mettre des prints dans les classes de modèle
                print('Square Loaded : ' + str(square))

            # -tc- La liste de listes est à mon avis une structure de données qui complexifie le développement du jeu
            self.maps.append(mapRow)
