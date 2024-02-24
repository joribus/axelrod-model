import numpy as np
# dal file individuo importa la classe individuo
from individuo import individuo
from utility import *

# Creiamo una lista vuota per contenere la matrice di individui
matrix = []

L = 2
feature = 4
traits = 3

# Creiamo la matrice di individui
# il trattino non è un numero, fa L volte la cosa sotto
for _ in range(L):
    row = []  # Creiamo una nuova riga della matrice
    for _ in range(L):
        row.append(individuo(feature, traits))  # Aggiungiamo un nuovo individuo alla riga
    matrix.append(row)  # Aggiungiamo la riga alla matrice

matrix = np.array(matrix)

# seleziono individuo k
pos_k = get_k_pos(L)
#matrix[pos_k].showindividuo()  # individuo k in vettore

#print(pos_k)
#print(get_neighbors(pos_k, L))
#print(get_r_pos(pos_k, L))

pos_r = get_r_pos(pos_k, L)

# ho istanziato
k = matrix[pos_k]
r = matrix[pos_r]

k.showindividuo()
r.showindividuo()
print(get_diff(k,r))
print(get_pos(k,r))

print(get_prob(k,r))

if interaction(k,r):
    selection = random.choice(get_pos(k,r))
    k.feature[selection] = r.feature[selection]
    print("Ho fatto lo scambio")

print(k.feature)







