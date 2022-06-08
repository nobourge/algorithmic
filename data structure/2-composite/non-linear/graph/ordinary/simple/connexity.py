"""
* Exercice 6.3 (Graphes 2-arête-connexes).
Un pont dans un graphe connexe est une arête telle que
si on l’enlève, le graphe est divisé en deux composantes connexes.
Un graphe sans pont est dit 2-arête-connexe.
Donner un algorithme qui détermine si un graphe donné est
2-arête-connexe
"""

def contains_a_bridge(graph):
    """

    :param graph:
    :return: if the graph contains a bridge
    """
    v = graph[0]
    if v[degree] == 1:
        return True
    else
        for neighbour in v.neighbours :
            delete v.neighbours[neighbour]


def is_minimum_n_edges_connex(graph, n):
    """

    :param n:
    :return: true if
    """
    for neighbour

graph =
print(is_minimum_n_edges_connex(graph,2))
