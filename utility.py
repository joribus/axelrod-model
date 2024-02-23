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
