import graphviz as gv
import numpy as np

#Création d'une variable i pour simplifier l'écriture de l'inifinie dans la matrice
i = float('inf')

#Création d'un chemin arbitraire pour test
c = [0,1,4,2]

#Création d'une matrice abritraire pour test
M = np.array([[i, 1, 1, 1, 1],
     [i, i, i, 1, 1],
     [1, i, 1, i, i],
     [i, i, i, i, i],
     [1, 1, 1, i, 1]])

def matrix_to_graph(M,c) :
    #On initialise la création d'un dot qui permettra de stocker les informations de notre graphe
    dot = gv.Digraph(strict = True)
    #On initialise un dot2 qui resterra vide afin de ne rien renvoyer en cas de problème
    dot2 = gv.Digraph(strict = True)
    
    #On définit que les sommets mit dans le dot devront être en rouge
    dot.attr('node', color = 'red', fontcolor = 'red')
    
    #On parcours les indices de notre liste de sommets 
    for i in range (len(c) - 1) :
        #On ajoute le noeud qui correspond à l'indice i du chemin dans le dot
        dot.node(str(c[i]))
        #On vérifie que l'arête allant de c[i] à c[i+1] n'est pas infinie afin de s'assurer quel le chemin existe
        if M[c[i]][c[i+1]] != float('inf') :
            #Si l'arête existe, on ajoute la flêche correspondant dans le dot en rouge
            dot.edge(str(c[i]), str(c[i+1]), color = 'red', fontcolor = 'red')
        else :
            #Si l'arête n'existe pas, on renvoie un fichier vide et on indique que le chemin n'existe pas
            print("Chemin impossible")
            return dot2
    
    #On remet les paramêtres des noeuds afin qu'ils soient en noirs
    dot.attr('node', color = 'black', fontcolor = 'black')
    
    #On parcours l'ensemble des indices de la matrices
    for i in range (len(M)) : 
        for j in range (len(M)) :
            #On vérifie si une valeur correspondant à un indice est différente de l'infini
            if M[i][j] != float('inf') :
                #Si c'est le cas, on ajoute la fleche correspondant en avec le poids
                dot.edge(str(i),str(j), label = str(M[i][j]))

    #On renvoie le fichier dot
    return dot
    

#Création d'une variable dot qui transforme ma matrice en graphe en prenant en compte le chemin donné
dot = matrix_to_graph(M,c)

#Affichage du graphe
dot.render('output/graphviz_output.gv')