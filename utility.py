import random
import numpy as np
from Individuo import Individuo


def create_matrix(L, f, t):
    matrix = []
    for x in range(L):
        row = []
        for y in range(L):
            row.append(Individuo(x, y, f, t))
        matrix.append(row)

    return np.array(matrix)


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
    #print_individuals(neighbors)
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


def are_all_cells_equal(matrix):
    L = len(matrix)
    if matrix[L-1][L-1].feature != matrix[0][0].feature:
        return False
    for i in range(L - 1):
        for j in range(L - 1):
            if matrix[i][j].feature != matrix[i + 1][j].feature or matrix[i][j].feature != matrix[i][j + 1].feature:
                return False
    return True

