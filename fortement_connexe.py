import numpy as np
import matplotlib.pyplot as plt


# On génère une matrice de taille n x n où chaque élément est 1 avec une probabilité p et 0 sinon.
def g(n, p, a, b):
    T = np.random.binomial(1, p, (n, n))
    T = T.astype('float64')
    
    for i in range(n):
        for j in range(n):
            if T[i][j] != 0:
                T[i][j] = np.random.randint(a, b)
            else:
                T[i][j] = float('inf')
    
    return T


def parcours_largeur(M,s) :
    # INITIALISATION
    n = len(M)
    file = [s]
    resultat = [s]
    
    # PARCOURS
    while file != [] :
        for i in M[file[0]]:
            for j in range(n) :
                if (M[file[0]][j] == 1 ) and j not in resultat :
                    file.append(j)
                    resultat.append(j)
        file.pop(0)
        
    # AFFICHAGE
    return resultat



def fc(m):
    #on parcourt tous les sommets du graphe
    for sommet in range(len(m)):
        parcours = parcours_largeur(m, sommet) #on vérifie le parcours du graphe à partir de ce sommet
        parcoursTranspose = parcours_largeur(np.transpose(m), sommet) #on vérifie le parcours du graphe transposé à partir de ce sommet
        #on vérifie que le parcours contient tous les sommets de la matrice, sinon le graphe n'est pas fortement connexe
        for s in parcours:
            if s not in parcoursTranspose:
                return False    
    return True



def test_stat_fc(n):
    r=1000
    compteurT = 0
    for i in range(r):
        print(i,'/ ',r)
        m = g(n, 0.5, 0, 2)
        if fc(m):
            compteurT += 1
    return compteurT / r



def trouver_probabilité():
    res = 0
    i=28
    while res < 0.99:
        res = test_stat_fc(i)
        print("Pour n = " + str(i) + ", la probabilité d'être fortement connexe est de " + str(res))
        i+=1
    return res


#Pour n = 30, la probabilité d'être fortement connexe est de 0.989
#Pour n = 31, la probabilité d'être fortement connexe est de 0.991




def test_stat_fc2(n,p):
    r=50 #on teste sur 50 graphes pour avoir une estimation de la probabilité d'être fortement connexe pour n et p
    compteurT = 0 #on initialise le compteur à 0 pour compter le nombre de graphes fortement connexes parmi les r graphes générés
    for i in range(r): #on génère r graphes aléatoires avec n sommets et une probabilité p d'avoir une arête entre deux sommets
        m = g(n, p, 1, 2)
        if fc(m):
            compteurT += 1 #on incrémente le compteur si le graphe généré est fortement connexe
    return compteurT / r #on retourne la probabilité d'être fortement connexe pour n et p en divisant le nombre de graphes
                         #fortement connexes par le nombre total de graphes générés (r)



def seuil(n):
    p = 1.01 #on commence à 1.01 pour que la première itération soit à 1
    res = 1 #on initialise res à 1 pour entrer dans la boucle
    while res > 0.99: #on continue tant que la probabilité d'être fortement connexe est supérieure à 0.99
        p -= 0.01 #on diminue p de 0.01 à chaque itération
        res = test_stat_fc2(n, p)  #on teste la probabilité d'être fortement connexe pour n et p
    print("Pour n = " + str(n) + ", le seuil de p pour que la probabilité d'être fortement connexe soit supérieure à 0.99 est de " 
          , p)
    return p



def visualiser():
    tailles = list(range(10,41))
    pourcentages = []
    for n in tailles:
        res = seuil(n)
        pourcentages.append(res)
    
    plt.figure(figsize=(10, 6))
    plt.plot(tailles, pourcentages)
    plt.xlabel('Taille du graphe')
    plt.ylabel("Porcentage d'arrêtes")
    plt.title('Évolution du seuil de connexité en fonction de la taille du graphe')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def visualiser_loglog():
    tailles = list(range(10,41))
    pourcentages = [0.58,0.55,0.63,0.49,0.51,0.45,0.52,0.38,0.37,0.43,
                    0.39,0.35,0.34,0.34,0.30,0.31,0.30,0.26,0.28,0.27,
                    0.24,0.28,0.28,0.26,0.26,0.20,0.27,0.21,0.22,0.17,0.26]
    for n in tailles:
        res = seuil(n)
        pourcentages.append(res)
    
    
    plt.figure(figsize=(10, 6))
    plt.loglog(tailles, pourcentages)
    plt.xlabel('Taille du graphe')
    plt.ylabel("Porcentage d'arrêtes")
    plt.title('Évolution du seuil de connexité en fonction de la taille du graphe')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

visualiser_loglog()