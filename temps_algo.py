import time
import numpy as np
import graphes as g

def TempsDij(n) :
    start_time = time.time()
    
    M = g.graphe2(n, 0.5, 0, 10)
    
    # Dictionnaire des distances minimales :
    # au départ, toutes les distances valent +inf
    poids = {i: float('inf') for i in range(n)}
    
    # La distance du sommet de départ à lui-même vaut 0
    poids[0] = 0
    
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
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return (elapsed_time)

print(TempsDij(10))