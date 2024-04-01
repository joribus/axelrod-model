import os
import random

import matplotlib.pyplot as plt
import numpy as np

from utility import *

f = 4
t = 15

L = 4
matrix = create_matrix(L, f, t)
print_matrix(matrix)

# Create a plot
fig, ax = plt.subplots()

# Plot digits of each cell with distance
for i in range(L):
    for j in range(L):
        feature_vector = matrix[i, j].feature
        print(feature_vector)
        for idx, digit in enumerate(feature_vector):
            ax.text(i + 0.2 * idx - 0.3, j, str(digit), ha='center', va='center', fontsize=10)
            print(digit)
# Add grid lines
for i in range(L+1):
    ax.axvline(x=i-0.5, color='gray', linestyle='-')
    ax.axhline(y=i-0.5, color='gray', linestyle='-')

# Set x and y limits
ax.set_xlim([-0.5, L-0.5])
ax.set_ylim([-0.5, L-0.5])
ax.set_aspect('equal', 'box')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Remove ticks
ax.set_xticks([])
ax.set_yticks([])

# Show the plot
plt.grid(False)
plt.show()
"""
if plot:
    plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
    plt.show()

iteration_count = 0  # Initialize iteration count

while True:
    iteration_count += 1  # Increment iteration count
    k: Individuo = get_k(matrix)
    r: Individuo = get_r(k, matrix)
    if interaction(k, r):
        k.copy_trait(r)
        if check_cells_interaction(matrix):
            break
if plot and (iteration_count == 50000 or iteration_count == 100000):
    plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
    print("200000")  # colore acceso
    plt.show()

numero_regioni.append(number_of_regions(matrix))
print("num iterazione ", len(numero_regioni))

medie.append(np.mean(numero_regioni))
print("L ", L)

print(medie)
print(dimensioni)

"""