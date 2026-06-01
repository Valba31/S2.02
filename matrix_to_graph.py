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

    # Création du graphe sans chemin
    for i in range(n):
        for j in range(n):
            if M[i][j] != INF:
                dot_vide.edge(str(i), str(j), label=str(M[i][j]))

    # Vérification de la présence d'une arête de poids négatif
    poids_negatif = False
    for i in range(n):
        for j in range(n):
            if M[i][j] < 0 and M[i][j] != INF:
                poids_negatif = True
                break

    # Utilisation de l'algorithme adapté à notre situation
    if not poids_negatif:
        resultat = dijkstra(M, d)
    else:
        resultat = bellman_ford(M, d)

    # Si cycle négatif alors on renvoie le graphe sans chemin
    if resultat is None:
        print("Cycle négatif détecté, chemin impossible")
        return dot_vide

    # Récupération de la liste des sommet pour aller de d à s
    c = resultat[s]

    #Si il n'y a pas de chemin alors on renvoie le graphe sans chemin
    if c is None or len(c) == 0:
        print("Chemin impossible")
        return dot_vide

    print("Chemin trouvé :", c)

    # Si il y a un chemin on fait une liste d'arêtes parcourues
    aretes_parcourues = set()

    # On définit les noeuds que l'on va parcourir en rouge
    dot.attr('node', color='red', fontcolor='red')

    # On parcours la liste des sommet du chemin
    for i in range(len(c) - 1):
        sommet1 = c[i]
        sommet2 = c[i + 1]

        # On ajoute le noeuds en rouge
        dot.node(str(sommet1))


        # Si il y a un chemin qui n'est pas infini entre les deux noeuds, on ajoute l'arêtes en rouge 
        if M[sommet1][sommet2] != INF:
            dot.edge(
                str(sommet1), str(sommet2),
                label=str(M[sommet1][sommet2]),
                color='red', fontcolor='red'
            )
            aretes_parcourues.add((sommet1, sommet2))

    # On ajoute le dernier sommet du chemin c
    dot.node(str(c[-1]))

    # Modification des prochaines arêtes en noir
    dot.attr('node', color='black', fontcolor='black')

    # Ajout des arêtes qui ne sont pas dans le chemin en noir
    for i in range(n):
        for j in range(n):
            if M[i][j] != INF and (i, j) not in aretes_parcourues:
                dot.edge(str(i), str(j), label=str(M[i][j]))

    return dot

# Création de la matrice
<<<<<<< Updated upstream
M = utile.graphe2(4, 0.6, -1, 20)
=======
M = utile.graphe2(10, 0.2, -1, 20)
>>>>>>> Stashed changes

# Création du graphe
dot = matrix_to_graph(M, 0, 3)

# Affichage / export
dot.render('output/graphviz_output', format='png', view=True)