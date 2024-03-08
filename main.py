from utility import *

L = 5
f = 5
t = 5

matrix = create_matrix(L, f, t)
print_matrix(matrix)


while True:

    k: Individuo = get_k(matrix)
    r: Individuo = get_r(k, matrix)
    #k.showindividuo()
    #r.showindividuo()
    if interaction(k, r):
        copiedFeature_index = k.copy_trait(r)
        # print(prob_state(matrix, k, copiedFeature_index))
        if prob_state(matrix, k, copiedFeature_index) == 1 and are_all_cells_equal(matrix):
            break

print("Tutte le celle sono uguali")
print_matrix(matrix)


