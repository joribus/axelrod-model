import os
import random

import matplotlib.pyplot as plt
import numpy as np

from utility import *

f = 5
t = 15
iterazioni = []
media_iterazioni = []
dimensioni = []

for i in range(10):
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

        print(iteration_count)
        iterazioni.append(iteration_count)

    media_iterazioni.append(np.mean(iterazioni))
    print("L ", L)

print(media_iterazioni)


plt.plot(dimensioni, media_iterazioni)
plt.xlabel('Width of territory')
plt.ylabel('Average number of iterations to reach stability')
plt.title('Plot of iterations for increasing territory width')
plt.show()