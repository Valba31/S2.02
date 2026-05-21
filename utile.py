import numpy as np

INF = float('inf')

def graphe(n, a, b):
    T = np.random.randint(0, 2, (n, n))
    T = T.astype('float64')
    
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0:
                T[i][j] = np.random.randint(a, b)
            else:
                T[i][j] = float('inf')

    return T

def graphe2(n, p, a, b):
    T = np.random.binomial(1, p, (n, n))
    T = T.astype('float64')
    
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0:
                T[i][j] = np.random.randint(a, b)
            else:
                T[i][j] = float('inf')
    
    return T

def pp(M, d):
    n = len(M)       # taille du tableau = nombre de sommets
    couleur = {i: "blanc" for i in range(n)}     # On colorie tous les sommets en blanc et s en vert
    couleur[d] = 'vert'
    pile=[d]       # on initialise la pile à s
    Resultat=[d] # on initialise la liste des résultats à s
    
    while pile !=[]: # tant que la pile n'est pas vide,
        i=pile[-1]          # on prend le dernier sommet i de la pile
        Succ_blanc=[]       # on crée la liste de ses successeurs non déjà visités (blancs)
        for j in range(n):
            if (M[i,j]!=INF and couleur[j]=='blanc'):
                Succ_blanc.append(j)
        if Succ_blanc!=[]:  # s'il y en a,
            v= Succ_blanc[0]    # on prend le premier (si on veut l'ordre alphabétique)
            couleur[v]='vert'   # on le colorie en vert, 
            pile.append(v)      # on l'empile
            Resultat.append(v)  # on le met en liste rsultat
        else:               # sinon:
            pile.pop()          # on sort i de la pile
    
    return(Resultat)

def pl(M, d):
    n=len(M)
    couleur={i: "blanc" for i in range(n)}     # On colorie tous les sommets en blanc et s (départ) en vert
    couleur[d] = 'vert'
    file=[d]
    Parcours=[d]
    while file !=[]:
        i=file[0]           # on prend le premier terme de la file
        for j in range(n):  # On enfile les successeurs de i encore blancs:
            if (M[file[0]][j]!=INF and couleur[j]=='blanc'):
                file.append(j)
                couleur[j]='vert' # On les colorie en vert (sommets visités)
                Parcours.append(j) # On les place dans la liste Resultat
        file.pop(0) # on défile i (on retire le premier élément)
    return(Parcours)

def obtenir_liste_aretes(M, resultat_du_parcours):
    # Liste finale des flèches : elle contiendra des tuples (x, y) pour chaque flèche qui part de x et qui va vers y
    liste = []
    
    # Pour chaque sommet du parcours en largeur/profondeur :
    for x in resultat_du_parcours:
        
        # Pour chaque flèche qui part de ce sommet :
        for k, v in enumerate(M[x]):
            # Si la flèche existe, on l'ajoute à la liste finale
            if v != float('inf'):
                liste.append((x, k))
    
    # On renvoit la liste finale
    return liste