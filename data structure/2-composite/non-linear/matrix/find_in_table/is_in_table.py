"""Exercice 1.6.
Décrire un algorithme de complexité O(n) pour le problème suivant :
étant donné une matrice a n × n dont les éléments apparaissent en
ordre croissant dans chaque ligne et chaque colonne,
déterminer si un élément x donné en entrée appartient à la matrice.
On suppose que tous les éléments
sont distincts."""

import time


matrix= [[1,2,3],
         [4,5,6],
         [7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

time.sleep(1)
