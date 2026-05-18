import numpy as np

def pp(M,s) :
    n = len(M)
    couleur = {i: 'blanc' for i in range(n)}
    couleur[s] = 'vert'
    pile = [s]
    resultat = [s]
    
    while pile != []:
        i = pile[-1]
        succ_blanc = []
        
        for j in range(n):
            if (M[i,j] == 1 and couleur[j] == 'blanc'):
                succ_blanc.append(j)
                
        if succ_blanc != [] :
            v = succ_blanc[0]
            couleur[v] = 'vert'
            pile.append(v)
            resultat.append(v)
        else:
            pile.pop()
    
    return(resultat)

M = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
])

print(pp(M, 0))