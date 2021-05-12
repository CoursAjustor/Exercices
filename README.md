# Ce que tu dois faire

Ecrire les codes dans le dossier "exercices" dans les fichiers correspondants,
créé une branche où tu faira une pull request afin de valider ton code
des tests passeront et vérifieront que le résultat est le bon, quand tous les tests seront passés je vérifierais
la qualitée du code.

Ne touche en aucun cas les tests et ne regarde pas dedans il n'y a pas de réponses


## Exercice 1

écrire une méthode ```checkAge``` qui pour un paramètre passé dis si oui ou non l'utilisateur peut accéder au site. Cette méthode devra être appelée dans la méthode ```main``` de la classe correspondant à l'exercice
exemple:
```
age < 21 => non
sinon => oui
```

## Exercice 2

écrire une méthode ```checkAge``` qui pour un paramètre passé dis si oui ou non l'utilisateur peut accéder au site suivant le pay. Cette méthode devra être appelée dans la méthode ```main``` de la classe correspondant à l'exercice

exemple:
```
age < 18 => non
age < 21 => oui sauf EU
sinon => oui
```

## Exercice 3

écrire une méthode ```counter``` qui compte de 1 au paramètre passé, le résultat doit être affiché et retourné par la fonction sous la forme d'un tableau de données. Cette méthode devra être appelée dans la méthode ```main``` de la classe correspondant à l'exercice
exemple:
de 1 à 15
sortie:
```
1
2
3
4
...
15
```

## Exercice 4

écrire une méthode ```counterEven``` qui compte de 1 au paramètre passé et avec seulement les nombre pairs. Cette méthode devra être appelée dans la méthode ```main``` de la classe correspondant à l'exercice
exemple:
de 1 à 15
sortie:
```
2
4
...
14
```

## Exercice 4.1

écrire une méthode ```counterOdd``` qui compte de 1 au paramètre passé et avec seulement les nombre impairs. Cette méthode devra être appelée dans la méthode ```main``` de la classe correspondant à l'exercice
exemple:
de 1 à 15
sortie:
```
1
3
...
15
```

## Exercice 5

écrire une méthode ```drawPyramid``` qui affiche une pyramide d'étoile de hauteur le paramètre passé. Cette méthode devra être appelée dans la méthode ```main``` de la classe correspondant à l'exercice
ex:
entrée:
3
sortie:
```
  *
 ***
*****
```
entrée:
4
sortie:
```
   *
  ***
 *****
*******
```

## Exercice final (bonus)

écrire une méthode ```draw``` qui affiche un losange d'étoile de hauteur le paramètre passé (attention il y a une subtilité). Cette méthode devra être appelée dans la méthode ```main``` de la classe correspondant à l'exercice
ex:
entrée:
3
sortie:

```
  *
 ***
  *
```
entrée:
4
sortie:
```
size need to be odd rerun using the default value
  *
 ***
  *
```
entrée:
5
sortie:
```
  *
 ***
*****
 ***
  *
```