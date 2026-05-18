import graphviz as gv
import numpy as np

import bellman_ford as bel
import dijkstra as dij
import graphe as g

#Création d'une variable i pour simplifier l'écriture de l'inifinie dans la matrice
i = float('inf')

#Création d'un chemin arbitraire pour test

#Création d'une matrice abritraire pour test

#M = np.array([[i, 1, 1, 1, 1],
#     [i, i, i, 1, 1],
#     [1, i, 1, i, i],
#     [i, i, i, i, i],
#     [1, 1, 1, i, 1]])

M = g.graphe2(10, 0.8, -5, 5)

def matrix_to_graph(M,d,s) :
    #On initialise la création d'un dot qui permettra de stocker les informations de notre graphe
    dot = gv.Digraph(strict = True)
    #On initialise un dot2 qui resterra vide afin de ne rien renvoyer en cas de problème
    dot2 = gv.Digraph(strict = True)
    
    #On créer une variable qui nous permettra de choisir l'algorithme à utiliser
    algo = True
    
    #On parcours l'ensemble de la matrice
    for i in range (len(M[0])) :
        for j in range (len(M[0])) :
            #On cherche à savoir si certaines arêtes ont un poids négatif
            if M[i][j] < 0 :
                #Si c'est le cas algo passe en False
                algo = False
    
    #Si algo est encore True on va utiliser dijkstra car il n'y a pas d'arête à poid négatif
    if algo == True : 
        c = dij.dijkstra(M,d)[s]
    #Sinon on utilise Bellman-Ford
    else :
        c = bel.bellmanford(M,d)[s]
    
    #On initialise une liste d'arête parcourue pour ne pas ajouter deux fois dans dot
    c_parcourus = set()
    
    #On définit que les sommets mit dans le dot devront être en rouge
    dot.attr('node', color = 'red', fontcolor = 'red')
    
    #On parcours les indices de notre liste de sommets 
    for i in range (len(c) - 1) :
        #On ajoute le noeud qui correspond à l'indice i du chemin dans le dot
        dot.node(str(c[i]))
        #On vérifie que l'arête allant de c[i] à c[i+1] n'est pas infinie afin de s'assurer quel le chemin existe
        if M[c[i]][c[i+1]] != float('inf') :
            #Si l'arête existe, on ajoute la flêche correspondant dans le dot en rouge
            dot.edge(str(c[i]), str(c[i+1]), label = str(M[c[i]][c[i+1]]), color = 'red', fontcolor = 'red')
            c_parcourus.add((c[i],c[i+1]))
        else :
            #Si l'arête n'existe pas, on renvoie un fichier vide et on indique que le chemin n'existe pas
            print("Chemin impossible")
            return dot2
    
    #On ajoute le dernier sommet à la liste des sommets visités par le chemin
    dot.node(str(c[-1]))
    
    #On remet les paramêtres des noeuds afin qu'ils soient en noirs
    dot.attr('node', color = 'black', fontcolor = 'black')
    
    #On parcours l'ensemble des indices de la matrices
    for i in range (len(M)) : 
        for j in range (len(M)) :
            #On vérifie si une valeur correspondant à un indice est différente de l'infini
            if M[i][j] != float('inf') :
                #On vérifier que l'arête ne soit pas déjà dans le dot
                if (i,j) not in c_parcourus :
                    #Si c'est le cas, on ajoute la fleche correspondant en avec le poids
                    dot.edge(str(i),str(j), label = str(M[i][j]))

    #On renvoie le fichier dot
    return dot
    

#Création d'une variable dot qui transforme ma matrice en graphe en prenant en compte le chemin donné
dot = matrix_to_graph(M,0,3)

#Affichage du graphe
dot.render('output/graphviz_output.gv')