import numpy as np 

def dijkstra(M, d):
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
                
    # Affichage :
    liste_des_chemins = []
    
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
            
            liste_des_chemins.append(list(chemin))

    return liste_des_chemins
                


i = float('inf')
M = np.array([ [i, 3, i, i, i], [i, i, 2, 4, i], [i, i, i, 7, i], [i, 1, 5, i, i], [i, i, i, i, i] ])
dijkstra(M, 0)
