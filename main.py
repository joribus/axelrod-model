import numpy as np
# dal file individuo importa la classe individuo
from individuo import individuo
from utility import *

# Creiamo una lista vuota per contenere la matrice di individui

#random.seed(8)
L = 2
feature = 4
traits = 3
H = []

matrix = crea_matrice(L, feature, traits)
print_matrix(matrix)
# seleziono individuo k

#while
pos_k = get_k_pos(L)
pos_r = get_r_pos(pos_k, L)

# ho istanziato
k = matrix[pos_k]
print("Individuo k: ")
k.showindividuo()
r = matrix[pos_r]
print("Individuo r: ")
r.showindividuo()

#print("Differenze tra k e r: ", get_diff(k, r))
#print("Posizioni delle differenze: ", get_pos(k, r))

#print("Probabilità di interazione tra k e r: ", get_prob(k, r))

if interaction(k, r):
    selection = random.choice(get_pos(k, r))
    k.feature[selection] = r.feature[selection]
    print("Ho fatto lo scambio")
    print("Nuovo k dopo lo scambio: ", k.feature)

print_matrix(matrix) # è la nuova con la sostituzione

