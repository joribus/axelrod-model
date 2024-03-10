import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from utility import *

L = 15
f = 10
t = 30

matrix = create_matrix(L, f, t)
print_matrix(matrix)

while True:

    k: Individuo = get_k(matrix)
    r: Individuo = get_r(k, matrix)
    #k.showindividuo()
    #r.showindividuo()
    if interaction(k, r):
        copiedFeature_index = k.copy_trait(r)
        #print(prob_state(matrix, k, copiedFeature_index))
        #if (prob_state(matrix, k, copiedFeature_index) == 1 and
        if check_cells_interaction(matrix):
            break

print("Tutte le celle sono uguali")
print_matrix(matrix)
#print(transform_matrix_to_color(transform_matrix(matrix)))
plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
plt.show()

