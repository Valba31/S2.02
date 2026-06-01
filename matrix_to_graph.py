import graphviz as gv

import utile
from dijkstra import dijkstra
from bellman_ford import bellman_ford

# Création d'une variable pour représenter l'infini
INF = float('inf')

def matrix_to_graph(M, d, s):
    n = len(M)
    
    dot = gv.Digraph(strict=True)
    dot_vide = gv.Digraph(strict=True)

    # Création d'un graphe dans le cas ou il n'y a pas de chemin
    for i in range(n):
        for j in range(n):
            if M[i][j] != INF:
                dot_vide.edge(str(i), str(j), label=str(M[i][j]))

    # On vérifie la présence d'arête à poid négatif
    poids_negatif = False
    for i in range(n):
        for j in range(n):
            if M[i][j] < 0 and M[i][j] != INF:
                poids_negatif = True
                break

    # On fait le calcul du chemin avec l'algorithme adaptée
    if not poids_negatif:
        resultat = dijkstra(M, d)
    else:
        resultat = bellman_ford(M, d)

    # On renvoie le graphe sans chemin si il y a un cycle négatif
    if resultat is None:
        print("Cycle négatif détecté, chemin impossible")
        return dot_vide

    #Si il n'y a pas ce cycle négatif on récupère le chemin
    c = resultat[s]

    #Si le chemin est nul, on renvoie le graphe sans chemin
    if c is None or len(c) == 0:
        print("Chemin impossible")
        return dot_vide

    print("Chemin trouvé :", c)

    # Si on a un chemin, on va stocker l'ensemble des arêtes parcourues
    aretes_parcourues = set()

    # On définit les noeuds en rouge
    dot.attr('node', color='red', fontcolor='red')

    # On parcours le chemin
    for i in range(len(c) - 1):
        sommet1 = c[i]
        sommet2 = c[i + 1]

        # On ajoute les noeuds que l'on rencontre
        dot.node(str(sommet1))

        # On ajoute l'arête en rouge si elle se se trouve bien dans la matrice
        if M[sommet1][sommet2] != INF:
            dot.edge(
                str(sommet1), str(sommet2),
                label=str(M[sommet1][sommet2]),
                color='red', fontcolor='red'
            )
            # On l'ajoute à la liste des arêtes parcourues
            aretes_parcourues.add((sommet1, sommet2))

    # On ajoute le denier noeuds du chemin
    dot.node(str(c[-1]))

    # On redéfinit la suite pour avoir des noeuds en noirs
    dot.attr('node', color='black', fontcolor='black')

    # On ajoute le reste des noeuds et arêtes
    for i in range(n):
        for j in range(n):
            if M[i][j] != INF and (i, j) not in aretes_parcourues:
                dot.edge(str(i), str(j), label=str(M[i][j]))

    return dot

# Création de la matrice
M = utile.graphe2(8, 0.2, -1, 20)

# Création du graphe
dot = matrix_to_graph(M, 0, 3)

# Affichage / export
dot.render('output/graphviz_output', format='png', view=True)