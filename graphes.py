import numpy as np

def graphe(n, a, b):
    T = np.random.randint(0, 2, (n, n))
    T = T.astype('float64')
    
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0:
                T[i][j] = np.random.randint(a, b)
            else:
                T[i][j] = float('inf')

    return T

def graphe2(n, p, a, b):
    T = np.random.binomial(1, p, (n, n))
    T = T.astype('float64')
    
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0:
                T[i][j] = np.random.randint(a, b)
            else:
                T[i][j] = float('inf')
    
    return T
