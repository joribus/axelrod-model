from utility import *

L = 2
f = 4
t = 3

matrix: np.ndarray = create_matrix(L, f, t)
print_matrix(matrix)

for i in range(100):
    k: Individuo = get_k(matrix)
    r: Individuo = get_r(k, matrix)
    if interaction(k, r):
        copiedFeature_index = k.copy_trait(r)
        print(prob_state(matrix, k, copiedFeature_index))

