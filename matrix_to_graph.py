import graphviz as gv
import numpy as np

i = float('inf')

c = [0,1,4,2]
M = np.array([[i, 1, 1, 1, 1],
     [i, i, i, 1, 1],
     [1, i, 1, i, i],
     [i, i, i, i, i],
     [1, 1, 1, i, 1]])

def matrix_to_graph(M,c) :
    #On initialise la création d'un fichier dot qui permettra d'utilser graphviz
    dot = gv.Digraph(strict = True)
    dot2 = gv.Digraph(strict = True)
    #On parcours l'ensemble de la matrice à la recherche du chemin parcourus
    for i in range (len(c) - 1) :
        dot.attr('node', color = 'red', fontcolor = 'red')
        dot.node(str(c[i]))
        if M[c[i]][c[i+1]] != float('inf') :
            dot.edge(str(c[i]), str(c[i+1]), color = 'red', fontcolor = 'red')
        else :
            print("Chemin impossible")
            return dot2
    
    dot.attr('node', color = 'black', fontcolor = 'black')
    #On parcours l'ensemble de la matrice
    for i in range (len(M)) : 
        for j in range (len(M)) :
            if M[i][j] != float('inf') :
                dot.edge(str(i),str(j), label = str(M[i][j]))
    return dot
    

dot = matrix_to_graph(M,c)
dot.render('output/graphviz_output.gv')