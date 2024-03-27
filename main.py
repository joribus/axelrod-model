import os
import random

import matplotlib.pyplot as plt
import numpy as np

from utility import *

f = 5
t = 15
medie = []
dimensioni = []

for i in range(20):
    L = i + 2
    dimensioni.append(L)

    plot = False

    numero_regioni = []

    for i in range(5):
        matrix = create_matrix(L, f, t)

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

plt.plot(dimensioni, medie)
plt.xlabel('Width of territory')
plt.ylabel('Average Number of Stable Regions')
plt.title('Plot of X and Y')
plt.show()