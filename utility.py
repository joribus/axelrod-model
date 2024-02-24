import random
def get_k_pos(L):
    riga = random.randint(0, L - 1)
    col = random.randint(0, L - 1)
    return riga, col

# dc = delta colonna
# dr = delta riga

def get_neighbors(position, L):
    neighbors = []

    # Calcola i vicini della cella attuale
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = position[0] + dr, position[1] + dc
        if 0 <= r < L and 0 <= c < L:
            neighbors.append((r, c))

    return neighbors

def get_r_pos(position, L):
    return random.choice(get_neighbors(position, L))



def get_diff(k, r):
    k_r = []
    for i in range(len(k.feature)):
        if k.feature[i] != r.feature[i]:
            k_r.append(k.feature[i])

    return k_r

def get_pos(k ,r):
    position = []
    for i in range(len(k.feature)):
        if k.feature[i] != r.feature[i]:
            position.append(i)

    return position

def get_prob(k, r):
    n_kr = len(k.feature) - len(get_diff(k,r))
    prob = n_kr / len(k.feature)

    return prob

def print_matrix(matrix):
    # Stampiamo la matrice di individui
    for row in matrix:
        for individuo in row:
            individuo.showindividuo()

def interaction(k,r):
    return random.uniform(0,1) < get_prob(k,r)



