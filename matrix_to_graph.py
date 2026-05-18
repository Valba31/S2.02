import graphviz as gv
import numpy as np

import algo as al
import graphes as g

# Création d'une variable pour représenter l'infini
INF = float('inf')

# Création de la matrice
M = g.graphe2(10, 0.6, -1, 10)

def matrix_to_graph(M, d, s):
    n = len(M)

    # Graphe principal
    dot = gv.Digraph(strict=True)

    # Graphe vide renvoyé en cas d'erreur
    dot_vide = gv.Digraph(strict=True)

    # Vérifie la présence de poids négatifs
    poids_negatif = False

    for i in range(n):
        for j in range(n):
            if M[i][j] < 0 and M[i][j] != INF:
                poids_negatif = True

    # Choix de l'algorithme
    try:
        if not poids_negatif:
            c = al.dijkstra(M, d)[s]
        else:
            c = al.bellman_ford(M, d)[s]

    except Exception as e:
        print("Erreur lors du calcul du chemin :", e)
        return dot_vide
    
    # Vérification du chemin
    if c is None or len(c) == 0:
        print("Chemin impossible")
        return dot_vide

    print("Chemin trouvé :", c)

    # Ensemble des arêtes déjà parcourues
    aretes_parcourues = set()

    # Configuration des noeuds du chemin en rouge
    dot.attr('node', color='red', fontcolor='red')

    # Ajout du chemin
    for i in range(len(c) - 1):

        sommet1 = c[i]
        sommet2 = c[i + 1]

        dot.node(str(sommet1))

        # Vérifie que l'arête existe
        if M[sommet1][sommet2] != INF:

            dot.edge(
                str(sommet1),
                str(sommet2),
                label=str(M[sommet1][sommet2]),
                color='red',
                fontcolor='red'
            )

            aretes_parcourues.add((sommet1, sommet2))

        else:
            print("Chemin impossible")
            return dot_vide

    # Ajout du dernier sommet
    dot.node(str(c[-1]))

    # Remise en noir des autres noeuds
    dot.attr('node', color='black', fontcolor='black')

    # Ajout des autres arêtes
    for i in range(n):
        for j in range(n):

            if M[i][j] != INF:

                if (i, j) not in aretes_parcourues:

                    dot.edge(
                        str(i),
                        str(j),
                        label=str(M[i][j])
                    )

    return dot

# Création du graphe
dot = matrix_to_graph(M, 0, 3)

# Affichage / export
dot.render('output/graphviz_output', format='png', view=True)