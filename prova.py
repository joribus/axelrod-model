import random

import numpy as np
# dal file individuo importa la classe individuo
from individuo import individuo
from utility import *

# Creiamo una lista vuota per contenere la matrice di individui

random.seed(20)
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

pos_vicini = get_neighbors(pos_k, L)
#for i in range(len(pos_vicini)):
#    H.append(matrix[pos_vicini[i]])
#    H[i].showindividuo()   # mostra i vicini
#    print("I vicini di k: ", H[i].feature)



#print("Differenze tra k e r: ", get_diff(k, r))
#print("Posizioni delle differenze: ", get_pos(k, r))

#print("Probabilità di interazione tra k e r: ", get_prob(k, r))

if interaction(k, r):
    selection = random.choice(get_pos(k, r))
    k.feature[selection] = r.feature[selection]
    print("Ho fatto lo scambio")
    print("Nuovo k dopo lo scambio: ", k.feature)
    for i in range(len(pos_vicini)):
        v = matrix[pos_vicini[i]]
        #v.showindividuo()
        if v.feature[selection] == r.feature[selection]:
            H.append(v)
    print("questo è l'insieme H: ", H)
    h = len(H)
    f = len(k.feature)
    sommatoria = []
    for i in range(h):
        r = H[i]
        n_kr = len(k.feature) - len(get_diff(k, r))
        print(n_kr)
        in_somma = (n_kr/f) * (1/(f-n_kr))
        sommatoria.append(in_somma)
        print(sommatoria)
    probabilita = (1/((L**2)*h))*sum(sommatoria)

    print("La prob: ", probabilita)


while True:
    pos_k = get_k_pos(L)
    pos_r = get_r_pos(pos_k, L)

    # Istruzioni per istanziare k e r

    pos_vicini = get_neighbors(pos_k, L)

    # Istruzioni per iterare sui vicini di k e calcolare H

    if interaction(k, r):
        # Istruzioni per effettuare lo scambio e aggiornare H

        h = len(H)
        f = len(k.feature)
        sommatoria = []
        for i in range(h):
            r = H[i]
            n_kr = len(k.feature) - len(get_diff(k, r))
            in_somma = (n_kr / f) * (1 / (f - n_kr))
            sommatoria.append(in_somma)
        probabilita = (1 / ((L ** 2) * h)) * sum(sommatoria)

        print("La probabilità:", probabilita)

    # Aggiungi qui le condizioni per uscire dal ciclo
    if probabilita == 0 or probabilita == 1:
        break



#print_matrix(matrix) # è la nuova con la sostituzione