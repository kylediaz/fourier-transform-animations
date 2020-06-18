import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg
import numpy as np
import sys
from os import path

if len(sys.argv) > 1:
    image_path = sys.argv[1]
else:
    image_path = ''
while not path.exists(image_path):
    image_path = input('Input image path > ')
img = mpimg.imread(image_path)


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])


img = rgb2gray(img)

fig, (original_ax, filtered_ax) = plt.subplots(1, 2)
fig.patch.set_facecolor('xkcd:black')
image_ax_args = dict(cmap='gray')
original_ax.set_title('Original Image')
filtered_ax.set_title('Filtered Image')

original_ax.imshow(img, **image_ax_args)

threshold = 10
high_pass_filter = np.vectorize(lambda n: n if n.real ** 2 + n.imag ** 2 < threshold ** 2 else 0, otypes=[complex])
low_pass_filter = np.vectorize(lambda n: n if n.real ** 2 + n.imag ** 2 > threshold ** 2 else 0, otypes=[complex])


def update(i):
    f_transform = np.fft.fft2(img)
    f_transform = high_pass_filter(f_transform)
    global threshold
    threshold += 10 ** (.1 * (i + 10))

    inverse_f_transform = np.fft.ifft2(f_transform).astype(float)

    filtered_ax.imshow(inverse_f_transform, **image_ax_args)
    return filtered_ax,


animation.FuncAnimation(fig, update, interval=10, blit=True)

plt.show()
