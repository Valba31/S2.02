import parcours as p
import numpy as np

def fc(m):
    parcours = p.pp(m, 0)
    parcoursTranspose = p.pp(np.transpose(m), 0)
    for s in parcours:
        if s not in parcoursTranspose:
            return False
    return True

print (fc(np.array([[1,1,1],
                    [1,1,1],
                    [0,0,0]])))