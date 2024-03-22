import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from utility import *
from PIL import Image, ImageDraw
import imageio

from utility import *

L = 2
f = 5
t = 3

matrix = create_matrix(L, f, t)
print_matrix(matrix)
plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
plt.show()


print("-----------------------------------------------------------")
print("-----------------------------------------------------------")


# Set up the figure and axis
fig, ax = plt.subplots()


frames = []

while True:

    k: Individuo = get_k(matrix)
    r: Individuo = get_r(k, matrix)

    if interaction(k, r):
        copiedFeature_index = k.copy_trait(r)
        frame = transform_matrix_to_color(transform_matrix(matrix))
        frames.append([plt.imshow(frame)])

        if check_cells_interaction(matrix):
            print("The state is ABSORBING")
            break

#print("STABLE REGIONS")
print_matrix(matrix)
#print(transform_matrix_to_color(transform_matrix(matrix)))
plt.imshow(transform_matrix_to_color(transform_matrix(matrix)))
plt.show()

# Create the animation
ani = animation.ArtistAnimation(fig, frames, interval=100, blit=True)

# Save the animation as a GIF
ani.save('animation.gif', writer='imagemagick')

# Display the animation (optional)
plt.show()


# Open the GIF file
gif_path = "animation.gif"
gif_image = Image.open(gif_path)

# Display the GIF
gif_image.show()