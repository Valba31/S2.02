import time
import numpy as np
import matplotlib.pyplot as plt
import utile as u

INF = float('inf')

def TempsDij(n) :
    start_time = time.time()
    
    M = u.graphe2(n, 0.5, 0, 10)
    
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
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return (elapsed_time)

def TempsBF(n) :
    
    start_time = time.time()
    
    M = u.graphe2(n, 0.5, -10, 10)
    
    # INITIALISATION
    # n correspond au nombre de sommets du graphe (car la matrice est carrée n * n)
    n = len(M)
    
    # Dictionnaire des distances minimales :
    # au départ, toutes les distances valent +inf
    poids = {i: INF for i in range(n)}
    
    # La distance du sommet de départ à lui-même vaut 0
    poids[0] = 0
    
    # Dictionnaire des prédécesseurs, qui permettra de reconstruire le plus court chemin
    precedents = {i: None for i in range(n)}
    
    # Liste des arêtes du graphe :
    F = u.obtenir_liste_aretes(M, u.pp(M, 0))
    
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
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    return (elapsed_time)


def comp_dij_bf() :
    tailles = list(range(2,200))
    temps_dij = []
    temps_bf = []
    
    for n in tailles :
        temps_dij.append(TempsDij(n))
        temps_bf.append(TempsBF(n))
        print(n)
        
    plt.figure(figsize = (10, 6))
    plt.plot(tailles, temps_dij, label = "Dijkstra", color = "red")
    plt.plot(tailles, temps_bf, label = "Bellman-Ford", color = "blue")
    
    plt.title("Evolution des temps d'éxécution de l'algorithme de Dijkstra et de Bellman-Ford")
    plt.xlabel("Nombre de sommet du graphe (N)")
    plt.ylabel("Temps d'exécution (s)")
    
    plt.legend()
    plt.grid(True, linestyle = '--', alpha = 0.5)
    plt.show()

def comp_dij_bf_log() :
    tailles = list(range(2,200))
    temps_dij = []
    temps_bf = []
    
    for n in tailles :
        temps_dij.append(TempsDij(n))
        temps_bf.append(TempsBF(n))
        print(n)
        
    plt.figure(figsize = (10, 6))
    plt.loglog(tailles, temps_dij, label = "Dijkstra", color = "red")
    plt.loglog(tailles, temps_bf, label = "Bellman-Ford", color = "blue")
    
    plt.title("Evolution des temps d'éxécution de l'algorithme de Dijkstra et de Bellman-Ford")
    plt.xlabel("Nombre de sommet du graphe (N)")
    plt.ylabel("Temps d'exécution (s)")
    
    plt.legend()
    plt.grid(True, linestyle = '--', alpha = 0.5, which = "both")
    plt.show()
   
comp_dij_bf_log()