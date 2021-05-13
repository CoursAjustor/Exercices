import random
from exercices.exercice_1 import Exercice1
from exercices.exercice_2 import Exercice2
from exercices.exercice_3 import Exercice3
from exercices.exercice_4 import Exercice4
from exercices.exercice_4b import Exercice4b
from exercices.exercice_5 import Exercice5
from exercices.exercice_5b import Exercice5b

exercices = []

exercices.append(Exercice1())
exercices.append(Exercice2())
exercices.append(Exercice3())
exercices.append(Exercice4())
exercices.append(Exercice4b())
exercices.append(Exercice5())
exercices.append(Exercice5b())

print('Démarrage des exercices')

for exercice in exercices:
    param = random.randint(1, 100)
    exercice.main(param)
