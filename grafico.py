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

    for i in range(10):
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


# per LATEX

import os
import random

import matplotlib.pyplot as plt
import numpy as np

from utility import *

plot = True
numero_regioni = []
medie = []
f = 5
t = 10
L = 10
matrix = create_matrix(L, f, t)
print_matrix(matrix)
iteration_count = 0  # Initialize iteration count

if plot:
    plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
    plt.show()

latexMatrix = transform_matrix(matrix)
latex_code = "\\begin{bmatrix}\n"
for row in latexMatrix:
    latex_code += " & ".join(map(str, row)) + " \\\\\n"
latex_code += "\\end{bmatrix}"

print(latex_code)

if plot:
    plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
    plt.show()

while True:
    iteration_count += 1  # Increment iteration count
    k: Individuo = get_k(matrix)
    r: Individuo = get_r(k, matrix)
    if interaction(k, r):
        k.copy_trait(r)
    if check_cells_interaction(matrix):
        break
    if plot and (iteration_count == 120000 or iteration_count == 200000):
        plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
        print("200000")  # colore acceso
        plt.show()

numero_regioni.append(number_of_regions(matrix))
print("num iterazione ", len(numero_regioni))

medie.append(np.mean(numero_regioni))
print("L ", L)

print(medie)


if plot:
    plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
    plt.show()

latexMatrix = transform_matrix(matrix)
latex_code = "\\begin{bmatrix}\n"
for row in latexMatrix:
    latex_code += " & ".join(map(str, row)) + " \\\\\n"
latex_code += "\\end{bmatrix}"

print(latex_code)



# per fare la FIGURA 3

f = 5
t = 15
dimensioni = []

iterations_mean = []
interactions_mean = []

for i in range(10):
    L = i + 2
    dimensioni.append(L)

    plot = False

    for j in range(10):
        matrix = create_matrix(L, f, t)
        iterations = []
        interactions = []

        if plot:
            plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
            plt.show()

        iteration_count = 0  # Initialize iteration count
        interaction_count = 0
        while True:
            iteration_count += 1  # Increment iteration count
            k: Individuo = get_k(matrix)
            r: Individuo = get_r(k, matrix)
            if interaction(k, r):
                interaction_count += 1
                k.copy_trait(r)
            if check_cells_interaction(matrix):
                break
        if plot and (iteration_count == 50000 or iteration_count == 100000):
            plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
            print("200000")  # colore acceso
            plt.show()

        iterations.append(iteration_count)
        interactions.append(interaction_count)

    print("L ", L)
    iterations_mean.append(np.mean(iterations))
    interactions_mean.append(np.mean(interactions))


plt.plot(dimensioni, interactions_mean, marker="o")
plt.grid()
plt.xlabel('Width of Territory')
plt.ylabel('Average Number of interactions')
plt.title('Interactions')
plt.show()

plt.plot(dimensioni, iterations_mean, marker="o")
plt.grid()
plt.xlabel('Width of territory')
plt.ylabel('Average Number of iterations')
plt.title('Iterations')
plt.show()

plt.plot(dimensioni, iterations_mean, marker="o", label="Iterations")
plt.plot(dimensioni, interactions_mean, marker="o", label="Interactions")
plt.grid()
plt.xlabel('Width of territory')
plt.ylabel('Simulated Time')
plt.title('Avarage number of iterations and interactions')
plt.legend(labels=['Iterations', 'Interactions'])
plt.show()


import os
import random

import matplotlib.pyplot as plt
import numpy as np

from utility import *

for w in range(5):

    f = 5
    t = 15
    dimensioni = []

    iterations_mean = []
    interactions_mean = []

    for i in range(9):
        L = i + 2
        dimensioni.append(L)

        plot = False

        for j in range(15):
            matrix = create_matrix(L, f, t)
            iterations = []
            interactions = []

            if plot:
                plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
                plt.show()

            iteration_count = 0  # Initialize iteration count
            interaction_count = 0
            while True:
                iteration_count += 1  # Increment iteration count
                k: Individuo = get_k(matrix)
                r: Individuo = get_r(k, matrix)
                if interaction(k, r):
                    interaction_count += 1
                    k.copy_trait(r)
                if check_cells_interaction(matrix):
                    break
            if plot and (iteration_count == 50000 or iteration_count == 100000):
                plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
                print("200000")  # colore acceso
                plt.show()

            iterations.append(iteration_count)
            interactions.append(interaction_count)

        print("L ", L)
        iterations_mean.append(np.mean(iterations))
        interactions_mean.append(np.mean(interactions))

    plt.plot(dimensioni, iterations_mean, marker="o", label="Iterations")
    plt.plot(dimensioni, interactions_mean, marker="o", label="Interactions")
    plt.grid()
    plt.xlabel('Width of territory')
    plt.ylabel('Simulated Time')
    plt.title('Avarage number of iterations and interactions')
    plt.legend(labels=['Iterations', 'Interactions'])
    plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.1)

    plt.show()

    print("Plot numero: ", w)


