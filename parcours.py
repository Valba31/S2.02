def pl(M,s) :
    # INITIALISATION
    n = len(M)
    couleur = {i: 'blanc' for i in range(n)}
    couleur[s] = 'vert'
    file = [s]
    resultat = [s]
    
    # PARCOURS
    while file != [] :
        i = file[0]
        
        for j in range(n) :
            if(M[file[0]][j] != float('inf') and couleur[j] == 'blanc') :
                file.append(j)
                couleur[j] = 'vert'
                resultat.append(j)
                
        file.pop(0) 
        
    # AFFICHAGE
    return resultat

def pp(M,s) :
    # INITIALISATION
    n = len(M)
    couleur = {i: 'blanc' for i in range(n)}
    couleur[s] = 'vert'
    pile = [s]
    resultat = [s]
    
    # PARCOURS
    while pile != []:
        i = pile[-1]
        succ_blanc = []
        
        for j in range(n):
            if (M[i,j] != float('inf') and couleur[j] == 'blanc'):
                succ_blanc.append(j)
                
        if succ_blanc != [] :
            v = succ_blanc[0]
            couleur[v] = 'vert'
            pile.append(v)
            resultat.append(v)
        else:
            pile.pop()
    
    # AFFICHAGE
    return resultat
