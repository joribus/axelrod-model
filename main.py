import numpy as np
# dal file individuo importa la classe individuo
from individuo import individuo
from utility import *

# Creiamo una lista vuota per contenere la matrice di individui
matrix = []

L = 2

# Creiamo la matrice di individui
# il trattino non è un numero, fa L volte la cosa sotto
for _ in range(L):
    row = []  # Creiamo una nuova riga della matrice
    for _ in range(L):
        row.append(individuo())  # Aggiungiamo un nuovo individuo alla riga
    matrix.append(row)  # Aggiungiamo la riga alla matrice

matrix = np.array(matrix)

# Stampiamo la matrice di individui
for row in matrix:
    for individuo in row:
        individuo.showindividuo()

# seleziono individuo k
position = get_k_pos(L)
matrix[position].showindividuo()


print(position)
print(get_neighbors(position, L))
print(get_r_pos(position, L))


