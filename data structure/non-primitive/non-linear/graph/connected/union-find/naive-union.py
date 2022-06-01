"""Exercice 2.2. Trouver l’erreur dans cette écriture de la méthode union pour l’algorithme naïf :
1 public void union(int p, int q) {
2 if (connected(p, q))
3 return;
4 for (int i = 0; i < id.length; i++)
5 if (id[i] == id[p])
6 id[i] = id[q];
7 count--;
8 }"""

def union(p, q)
    if connected(p, q)
        return
    for
        if (id[i] != id[p])
            id[i] = id[q];
    count--
