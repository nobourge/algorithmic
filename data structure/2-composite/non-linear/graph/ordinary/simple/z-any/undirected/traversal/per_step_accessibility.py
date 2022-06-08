"""
Exercice 6.4 (Un jeu de rôle).
Un monstre et un joueur se trouvent chacun sur un sommet distinct
d’un graphe (simple, non dirigé).
Le joueur et le monstre jouent à tour de rôle.
A chaque tour, ils
peuvent se déplacer sur un sommet adjacent, ou rester sur le même sommet.
Donner un algorithme
pour déterminer tous les sommets que le joueur peut atteindre avant le monstre. On suppose que le
joueur joue en premier.
"""
#1. si le monstre ne se deplace pas, le joueur peut atteindre tout les sommets sauf celui du monstre