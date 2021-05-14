import random
from exercices.exercice_1 import sum
from exercices.exercice_2 import sub
from exercices.exercice_3 import count
from exercices.exercice_4 import count_even
from exercices.exercice_5 import count_odd

print('Démarrage des exercices')

print('Exercice 1')
a, b = random.randint(1, 100), random.randint(1, 100)
print(sum(a, b))

print('Exercice 2')
a, b = random.randint(1, 100), random.randint(1, 100)
print(sub(a, b))

print('Exercice 3')
a = random.randint(1, 100)
print(count(a))

print('Exercice 4')
a = random.randint(1, 100)
print(count_even(a))

print('Exercice 5')
a = random.randint(1, 100)
print(count_odd(a))