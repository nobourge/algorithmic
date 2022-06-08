"""Exercice 1.2. Un tableau a[] est dit bitonique s’il existe
un indice i tel que les éléments d’indices
entre 0 et i sont triés en ordre strictement croissant,
et ceux d’indices supérieurs à i sont triés en ordre
strictement décroissant.
Écrire un programme qui détermine
si une valeur donnée appartient au tableau.
Ce programme ne devra effectuer que ∼ 3 log n comparaisons au pire cas"""

def find_in_bitonic_table(value, bitonic_list):
    m = max(bitonic_list)
    if value<m:
        find_in_bitonic_table(value, bitonic_list[m/2])
    else:
        find_in_bitonic_table(value, bitonic_list[/2])
