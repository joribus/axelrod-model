import math
import random
import numpy as np
from Individuo import Individuo
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap


def create_matrix(L, f, t):
    matrix = []
    for x in range(L):
        row = []
        for y in range(L):
            row.append(Individuo(x, y, f, t))
        matrix.append(row)

    return np.array(matrix)


def transform_matrix(matrix):
    L = len(matrix)
    new_matrix = []
    for x in range(L):
        row = []
        for y in range(L):
            row.append(matrix[x][y].feature)
        new_matrix.append(row)

    return np.array(new_matrix)


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(f"({i}, {j}): {matrix[i, j].feature}")


def get_k(matrix):
    r = random.randint(0, len(matrix) - 1)
    c = random.randint(0, len(matrix) - 1)

    return matrix[r, c]


def get_neighbors(k, matrix):
    neighbors = []

    # Calcola i vicini della cella attuale
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = k.x + dr, k.y + dc
        if 0 <= r < len(matrix) and 0 <= c < len(matrix):
            neighbors.append(matrix[r, c])

    return neighbors


def get_r(k, matrix):
    neighbors = get_neighbors(k, matrix)
    for n in neighbors:
        if n.feature == k.feature:
            neighbors.remove(n)
    # print_individuals(neighbors)
    return random.choice(neighbors)


def get_Nsimilarity(k, r):  # n_kr
    n = 0
    for i in range(len(k.feature)):
        if k.feature[i] == r.feature[i]:
            n += 1
    return n


def interaction(k, r):
    prob = get_Nsimilarity(k, r) / len(k.feature)
    if prob == 1:
        return False
    return random.uniform(0, 1) < prob


def get_H(k, matrix, copiedFeature_index):
    H = []
    for n in get_neighbors(k, matrix):
        if n.feature[copiedFeature_index] == k.feature[copiedFeature_index]:
            H.append(n)
    return H


def prob_state(matrix, k, copiedFeature_index):
    n_feature = len(k.feature)
    summation = 0
    H = get_H(k, matrix, copiedFeature_index)
    for n in H:
        n_similarity = get_Nsimilarity(k, n)
        if n_similarity == n_feature:
            return 1
        summation += (n_similarity / n_feature) * (1 / (n_feature - n_similarity))

    return (1 / ((len(matrix) ** 2) * len(H))) * summation


def print_individuals(individuals):
    print("-------------------------")
    print("vicini")
    for individual in individuals:
        individual.showindividuo()
    print("-------------------------")


# il controllo si fa su interaction pittosto che sull'uguaglianza
# se non c'è nessuna coppia chw puo interagire allora fermo


def check_cells_interaction(matrix):
    L = len(matrix)
    for i in range(L):
        for j in range(L):
            k = matrix[i, j]
            neighbors = get_neighbors(k, matrix)
            for neighbor in neighbors:
                if cells_interaction(k, neighbor):
                    return False

    return True


def cells_interaction(k, r):
    prob = get_Nsimilarity(k, r) / len(k.feature)
    if prob == 1 or prob == 0:
        return False
    return True


def integers_to_colors(array_of_integers, cmap_name='turbo'):
    cmap = plt.get_cmap(cmap_name)
    mean_color = cmap(array_to_n(array_of_integers))
    return mean_color


def transform_matrix_to_color(matrix):
    L = len(matrix)
    new_matrix = []
    for x in range(L):
        row = []
        for y in range(L):
            row.append(integers_to_colors(matrix[x][y]))
        new_matrix.append(row)

    return np.array(new_matrix)


def array_to_n(array):
    arr_tuple = tuple(array) #mette le tonde al posto delle quadre

    # Use Python's built-in hash function
    hash_value = hash(arr_tuple)

    # Ensure the hash value is positive
    hash_value = abs(hash_value)

    large_number = 10 ** 18  # You can adjust this depending on the desired precision
    normalized_value = hash_value % large_number
    result_decimal = normalized_value / large_number

    return result_decimal