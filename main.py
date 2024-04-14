import os
import random

import matplotlib.pyplot as plt
import numpy as np

from utility import *
random.seed(100)

L = 4
f = 5
t = 5

matrix = create_matrix(L, f, t)
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

    if iteration_count % 100 == 0:
        plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
        plt.show()

plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
plt.show()
print(iteration_count)