from utile import pp, obtenir_liste_aretes

INF = float('inf')

def bellman_ford(M, d):
    # INITIALISATION
    # n correspond au nombre de sommets du graphe (car la matrice est carrée n * n)
    n = len(M)
    
    # Dictionnaire des distances minimales :
    # au départ, toutes les distances valent +inf
    poids = {i: INF for i in range(n)}
    
    # La distance du sommet de départ à lui-même vaut 0
    poids[d] = 0
    
    # Dictionnaire des prédécesseurs, qui permettra de reconstruire le plus court chemin
    precedents = {i: None for i in range(n)}
    
    # Liste des arêtes du graphe :
    F = obtenir_liste_aretes(M, pp(M, d))
    
    # ALGO
    # Compteur qui nous permettra de savoir s'il y a un cycle négatif
    compteur = 0
    
    # On répète au maximum n fois :
    for _ in range(n):
        
        # Indicateur de changement : s'il n'y a pas de changement dans un tour de boucle, on peut arrêter l'algorithme
        modification = False
        
        # Pour chaque arête du graphe :
        for p1, p2 in F:
            
            # Si le poids de l'arête (p1, p2) est égal à +inf, il n'existe pas d'arête entre p1 et p2 : on passe à la suivante
            if M[p1, p2] == INF: continue
            
            # Nouvelle distance possible :
            # distance jusqu'à "p1" + poids de l'arête (p1 -> p2)
            nouvelle_distance = poids[p1] + M[p1, p2]
            
            # Si cette nouvelle distance est meilleure que celle connue actuellement, on met à jour 
            if poids[p2] > nouvelle_distance: 
                # Mise à jour de la meilleure distance 
                poids[p2] = nouvelle_distance
                
                # Mise à jour du prédécesseur
                precedents[p2] = p1
                
                # Indication de changement pour le prochain tour de boucle
                modification = True
        
        # On incrémente le compteur à chaque tour de boucle
        compteur += 1
        
        # Arrêt et on sort de la boucle en avance si plus aucun changement
        if modification == False:
            break
        
    # VERIFICATION
    if compteur == n:
        print("Il existe un cycle de poids négatif dans le graphe")
        return None
    
    # AFFICHAGE
    # On utilise un dictionnaire pour lier les chemins à un sommet, ça nous sera utile pour le tracer des graphes avec Graphviz
    dictionnaire_des_chemins = {i: None for i in range(n)}
    
    # Pour chaque sommet du graphe :
    for k, v in poids.items():
            
        # Si le sommet est celui de départ, on passe au prochain sommet
        if k == d:
            continue 
            
        # Si le sommet n'a pas de prédécésseur : on affiche qu'il n'est pas joignable
        if precedents[k] == None:
            print(f"Sommet {k} non joignable depuis {d}")
            continue
            
        # Sinon            
        else:            
            # On crée le chemin : au début seul le sommet d'arrivée est dedans : 
            chemin = []
                
            # On construit le chemin par concaténation :
            # chemin = k + prédécent(k) + précédent[précédent(k)] + ... tant que k est différent du sommet de départ
            actuel = k 
            while actuel != d:
                chemin.append(actuel)
                actuel = precedents[actuel]
                
            # On inverse le chemin pour avoir le sommet de départ en premier
            chemin.append(d)
            chemin.reverse()
                    
            """
            On affiche le résultat :
            - le poids du chemin au sommet k correspond à la valeur dans le dictionnaire "poids" pour la clé k
            - le chemin est celui créé plus haut
            """
            print(f"Poids vers {k} : {poids[k]} | chemin : {chemin}")
            
            # On réécrit le chemin sous la forme d'une liste d'entiers car c'est plus simple avec Graphviz
            dictionnaire_des_chemins[k] = chemin

    return dictionnaire_des_chemins
