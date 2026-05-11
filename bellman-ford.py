import numpy as np

def bellmanford(M, d):
    # n correspond au nombre de sommets du graphe (car la matrice est carrée n * n)
    n = len(M)

    # Dictionnaire des distances minimales :
    # au départ, toutes les distances valent +inf
    poids = {i: float('inf') for i in range(n)}
    
    # La distance du sommet de départ à lui-même vaut 0
    poids[d] = 0
    
    # Dictionnaire des distances minimales : il sera utile pour comparer la liste des poids actuels avec le tour précédent de l'algo
    poidsPrecedents = {}

    # Dictionnaire des prédécesseurs, qui permettra de reconstruire le plus court chemin
    precedents = {i: None for i in range(n)}

    # Liste des flèches : (x, y) représente une flèche qui part de x et qui va vers y
    F = [(0, 1), (1, 0), (0, 4), (4, 3), (4, 5), (5, 3), (3, 5), (3, 2), (2, 1)]

    i = 0
    while (i < n) & (poids != poidsPrecedents):
        poidsPrecedents = poids.copy()

        for p1, p2 in F:
            nouvelle_valeur = poidsPrecedents[p1] + M[p1, p2]

            if poidsPrecedents[p2] > nouvelle_valeur:
                poids[p2] = nouvelle_valeur
                poidsPrecedents[p2] = nouvelle_valeur
                precedents[p2] = p1
            else:
                poids[p2] = poidsPrecedents[p2]
        
        i += 1
    
    if (i == n):
        print("Cycle de poids négatif : pas de plus court chemin")
    else:
        print("Poids : ", poids)
        print("Précédents : ", precedents)

i = float('inf')
M = np.array([
    [i, -1, i, i, 1, i],
    [2, i, i, i, i, i],
    [i, 3, i, i, i, i],
    [i, i, -4, i, i, 6],
    [i, i, i, 7, i, -2],
    [i, i, i, 5, i, i]
])

bellmanford(M, 0)