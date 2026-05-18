import numpy as np
import parcours as ps

def dijkstra(M, d):
    # INITIALISATION
    # n correspond au nombre de sommets du graphe (car la matrice est carrée n * n)
    n = len(M) 
    
    # Dictionnaire des distances minimales :
    # au départ, toutes les distances valent +inf
    poids = {i: float('inf') for i in range(n)}
    
    # La distance du sommet de départ à lui-même vaut 0
    poids[d] = 0
    
    # Dictionnaire des prédécesseurs, qui permettra de reconstruire le plus court chemin
    precedents = {i: None for i in range(n)}
    
    # Liste des sommets déjà visités
    visites = []
    
    # ALGO
    # Il y a au maximum n sommets à traiter
    for _ in range(n):
        
        # On crée un dictionnaire contenant uniquement les sommets non encore visités
        non_visites = {k: v for k, v in poids.items() if k not in visites}
        
        # Si tous les sommets ont été visités, on peut arrêter l'algorithme
        if len(non_visites) == 0: break
        
        """
        On choisit le sommet non visité ayant la plus petite distance connue.
        Pour ça, on utilise la syntaxe : min(dict, key=dict.get)
        qui renvoie la clé associée à la plus petite valeur du dictionnaire 
        """ 
        cle = min(non_visites, key=non_visites.get)
        
        # Distance minimale actuelle vers ce sommet
        valeur = poids[cle]
        
        # On ajoute ce sommet à ceux déjà visités pour le prochain tour de la boucle
        visites.append(cle)
        
        # On regarde tous les sommets du graphe pour mettre à jour les distances
        for j in range(n): 
            
            # Si le sommet a déjà été visité, on ne le traite plus
            if j in visites: continue 
            
            # S'il n'existe pas d'arête entre le sommet actuel (cle) et le sommet j, on passe au suivant 
            if M[cle][j] == float('inf'): continue 
            
            # Nouvelle distance possible :
            # distance jusqu'à "cle" + poids de l'arête (cle -> j)
            nouvelle_distance = valeur + M[cle][j] 
            
            # Si cette nouvelle distance est meilleure que celle connue actuellement, on met à jour 
            if poids[j] > nouvelle_distance: 
                # Mise à jour de la meilleure distance 
                poids[j] = nouvelle_distance 
                
                # On mémorise le sommet précédent dans le plus court chemin 
                precedents[j] = cle 
                
    # AFFICHAGE
    # On utilise un dictionnaire pour lier les chemins à un sommet, ça nous sera utile pour le tracer des graphes avec Graphviz
    dictionnaire_des_chemins = {i: None for i in range(n)}
    
    # Pour chaque sommet du graphe :
    for k, v in poids.items():
            
        # Si le sommet est celui de départ, on passe au prochain sommet
        if k == d: continue 
            
        # Si le sommet n'a pas de prédécésseur : on affiche qu'il n'est pas joignable
        if precedents[k] == None: print(f"sommet {k} non joignable à {d} par un chemin dans le graphe G") 
            
        # Sinon
        else:            
            # On crée le chemin : au début seul le sommet d'arrivée est dedans : 
            chemin = "" + str(k)
                
            # On construit le chemin par concaténation :
            # chemin = prédécent(k) + précédent[précédent(k)] + ... tant que k est différent du sommet de départ
            actuel = k 
            while actuel != d:
                chemin += str(precedents[actuel])
                actuel = precedents[actuel]
                
            # On inverse le chemin pour avoir le sommet de départ en premier (d'où la syntaxe [::-1])
            chemin = chemin[::-1]
                    
            """
            On affiche le résultat :
            - le poids du chemin au sommet k correspond à la valeur dans le dictionnaire "poids" pour la clé k
            - le chemin est celui créé plus haut
            """
            print(f"Poids du chemin à {k} : {v} | chemin : {chemin}")
            
            # On réécrit le chemin sous la forme d'une liste d'entiers car c'est plus simple avec Graphviz
            dictionnaire_des_chemins[k] = [int(i) for i in list(chemin)]

    # On renvoit le dictionnaire
    return dictionnaire_des_chemins

def bellman_ford(M, d):
    # INITIALISATION
    # n correspond au nombre de sommets du graphe (car la matrice est carrée n * n)
    n = len(M)

    # Dictionnaire des distances minimales au tour T :
    # au départ, toutes les distances valent +inf
    poids = {i: float('inf') for i in range(n)}
    
    # La distance du sommet de départ à lui-même vaut 0
    poids[d] = 0
    
    # Dictionnaire des distances minimales au tour T - 1 : il sera utile pour comparer la liste des poids actuels avec le tour précédent de l'algo
    ancienPoids = {}

    # Dictionnaire des prédécesseurs, qui permettra de reconstruire le plus court chemin
    precedents = {i: None for i in range(n)}

    # Liste des flèches : (x, y) représente une flèche qui part de x et qui va vers y
    F = obtenir_liste(M, ps.pp(M, d))

    # On initialise un index : si celui si dépasse le nombre de sommet on saura qu'il y a un cycle négatif
    i = 0
    
    # ALGO
    # Tant que l'index est inférieur au nombre de sommets et que les poids actuels sont différents de ceux au tour précédent :
    while (i < n) and (poids != ancienPoids):
        
        # On recopie les poids dans les poids précédents :
        # Comme on est au début du tour, c'est le bon moment
        ancienPoids = poids.copy()

        # Pour chaque flèche :
        for p1, p2 in F:
            
            # Nouvelle distance possible :
            # distance jusqu'à p1 + poids de l'arête (p1 -> p2)
            nouvelle_valeur = ancienPoids[p1] + M[p1, p2]

            # Si cette nouvelle distance est meilleure :
            if nouvelle_valeur < poids[p2]:
                # on met à jour le poids du sommet p2
                poids[p2] = nouvelle_valeur
                
                # On met aussi à jour les poids du tour T - 1 pour éviter un problème d'écrasement plus tard dans le tour
                ancienPoids[p2] = nouvelle_valeur
                
                # On mémorise le sommet précédent dans le plus court chemin 
                precedents[p2] = p1
        
        # On incrémente l'indice par 1
        i += 1
    
    # Si l'indice égale le nombre de sommet, il y a un cycle négatif !
    if (i == n):
        print("Cycle de poids négatif : pas de plus court chemin")
    else:
        # AFFICHAGE
        # On utilise un dictionnaire pour lier les chemins à un sommet, ça nous sera utile pour le tracer des graphes avec Graphviz
        dictionnaire_des_chemins = {i: None for i in range(n)}
    
        # Pour chaque sommet du graphe :
        for k, v in poids.items():
                
            # Si le sommet est celui de départ, on passe au prochain sommet
            if k == d: continue 
                
            # Si le sommet n'a pas de prédécésseur : on affiche qu'il n'est pas joignable
            if precedents[k] == None: print(f"sommet {k} non joignable à {d} par un chemin dans le graphe G") 
                
            # Sinon
            else: 
                # On crée le chemin : au début seul le sommet d'arrivée est dedans : 
                chemin = "" + str(k)
                    
                # On construit le chemin par concaténation :
                # chemin = prédécent(k) + précédent[précédent(k)] + ... tant que k est différent du sommet de départ
                actuel = k 
                while actuel != d:
                    chemin += str(precedents[actuel])
                    actuel = precedents[actuel]
                      
                # On inverse le chemin pour avoir le sommet de départ en premier (d'où la syntaxe [::-1])
                chemin = chemin[::-1]
              
                """
                On affiche le résultat :
                - le poids du chemin au sommet k correspond à la valeur dans le dictionnaire "poids" pour la clé k
                - le chemin est celui créé plus haut
                """
                print(f"Poids du chemin à {k} : {v} | chemin : {chemin}")
                
                # On réécrit le chemin sous la forme d'une liste d'entiers car c'est plus simple avec Graphviz
                dictionnaire_des_chemins[k] = [int(i) for i in list(chemin)]
    
    # On renvoit le dictionnaire
    return dictionnaire_des_chemins

def obtenir_liste(M, L):        
    # Liste finale des flèches : elle contiendra des tuples (x, y) pour chaque flèche qui part de x et qui va vers y
    liste = []
    
    # Pour chaque sommet du parcours en largeur/profondeur :
    for x in L:
        
        # Pour chaque flèche qui part de ce sommet :
        for k, v in enumerate(M[x]):
            # Si la flèche existe, on l'ajoute à la liste finale
            if v != float('inf'):
                liste.append((x, k))
    
    # On renvoit la liste finale
    return liste
