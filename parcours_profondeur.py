def pp(M,s) :
    n = len(M)
    couleur = {}
    for i in range(n) :
        couleur[i] = 'blanc'
    couleur[s] = 'vert'
    pile = [s]
    Resultat = [s]
    
    while pile != [] :
        i = pile[-1]
        succ_blanc = []
        for j in range (n) :
            if (M[i,j] == 1 and couleur[j] == 'blanc') :
                succ_blanc.append(j)
        if succ_blanc != [] :
            v = succ_blanc[0]
            couleur[v] = 'vert'
            pile.append(v)
            Resultat.append
        else :
            pile.pop
    
    return(Resultat)