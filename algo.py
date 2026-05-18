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

    # Distances minimales
    poids = {i: float('inf') for i in range(n)}
    poids[d] = 0

    # Prédécesseurs
    precedents = {i: None for i in range(n)}

    # Liste des arêtes
    F = obtenir_liste(M, ps.pp(M, d))

    # ALGO
    # On répète au maximum n-1 fois : c'est le nombre de sommets du graphe moins 1, car un chemin simple ne peut pas faire plus de n-1 arêtes
    for _ in range(n - 1):

        # Indicateur de changement : s'il n'y a pas de changement dans un tour de boucle, on peut arrêter l'algorithme
        modification = False

        # Pour chaque arête du graphe :
        for p1, p2 in F:

            # Si le sommet de départ de l'arête est atteignable
            if poids[p1] != float('inf'):

                # On calcule une nouvelle valeur théorique pour le sommet d'arrivée de l'arête :
                nouvelle_valeur = poids[p1] + M[p1, p2]

                # Si cette nouvelle valeur est meilleure que celle connue actuellement, on met à jour
                if nouvelle_valeur < poids[p2]:

                    # On met à jour
                    poids[p2] = nouvelle_valeur
                    
                    # On change le prédécesseur
                    precedents[p2] = p1

                    # On indique qu'il y a eu une modification dans ce tour de boucle
                    modification = True

        # Arrêt si plus aucun changement
        if not modification:
            break

    # # -------------------------
    # # CYCLE NÉGATIF
    # # -------------------------

    # for p1, p2 in F:

    #     if poids[p1] != float('inf'):

    #         if poids[p1] + M[p1, p2] < poids[p2]:
    #             print("Cycle de poids négatif détecté")
    #             return None

    # AFFICHAGE
    # On crée un dictionnaire qui associe à chaque sommet son chemin depuis le sommet de départ, pour pouvoir tracer les graphes avec Graphviz
    dictionnaire_des_chemins = {i: None for i in range(n)}

    # Pour chaque sommet du graphe :
    for sommet in range(n):

        # Si le sommet est inaccessible
        if poids[sommet] == float('inf'):

            print(f"Sommet {sommet} non joignable depuis {d}")
            continue

        # Reconstruction du chemin
        chemin = []

        # On est sur le sommet d'arrivée
        actuel = sommet

        # On remonte par concatenation des prédécesseurs jusqu'à arriver au sommet de départ :
        while actuel is not None:
            # On ajoute le sommet actuel au chemin
            chemin.append(actuel)
            
            # On remonte d'un cran dans le chemin en allant au prédécesseur du sommet actuel
            actuel = precedents[actuel]

        # On inverse le chemin pour avoir le sommet de départ en premier
        chemin.reverse()

        # On affiche le résultat : poids du chemin et chemin lui-même
        print(f"Poids vers {sommet} : {poids[sommet]} | chemin : {chemin}")

        # On ajoute le chemin au dictionnaire des chemins
        dictionnaire_des_chemins[sommet] = chemin

    # On renvoit le dictionnaire des chemins
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
