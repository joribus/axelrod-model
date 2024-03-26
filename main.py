import os
import random

import numpy as np

from utility import *

# (f=10,t=10) = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# (f=10,t=15) = [2, 2, 1, 1, 2, 1, 1, 1, 2, 2]
# (f=15,t=5)  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# (f=15,t=10) = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# (f=15,t=15) = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


L = 10
f = 5
t = 10
save = True

matrix = create_matrix(L, f, t)

plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
plt.show()

"""
# Create 'img' directory if it doesn't exist
img_dir = 'img'
if not os.path.exists(img_dir):
    os.makedirs(img_dir)
"""


iteration_count = 0  # Initialize iteration count

while True:
    iteration_count += 1  # Increment iteration count
    k: Individuo = get_k(matrix)
    r: Individuo = get_r(k, matrix)
    if interaction(k, r):
        k.copy_trait(r)
        if check_cells_interaction(matrix):
            break
    if iteration_count == 50000 or iteration_count == 100000:
        plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
        print("200000")# colore acceso
        plt.show()

"""
    # Save figure for current iteration in 'img' folder
    if save and iteration_count % 5 == 0:
        plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
        plt.savefig(
            os.path.join(img_dir, f"iteration_{1000000000-iteration_count}.png"))  # Save figure in 'img' folder
        plt.close()  # Close the figure to release memory
        print(iteration_count)

if save:
    plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
    plt.savefig(
        os.path.join(img_dir, f"iteration_{1000000000-iteration_count}.png"))  # Save figure with unique filename in 'img' folder
    plt.close()
"""

plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))  # colore acceso
plt.show()

print(number_of_regions(matrix))


"""
regioni = np.unique(transform_matrix(matrix))
print(len(regioni))
print(regioni)
#print(iteration_count)
"""
# ffmpeg -framerate 5 -pattern_type glob -i 'iteration_*.png' -c:v libx264 -pix_fmt yuv420p output.mp4
# ffmpeg -i output.mp4 -vf reverse reversed_output.mp4