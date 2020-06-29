from common import image_input, rgb_to_gray
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


plt.style.use('dark_background')


img = rgb_to_gray(image_input())

f_transform = np.fft.fft2(img)
f_transform_shift = np.fft.fftshift(f_transform)
magnitude_spectrum = 20 * np.log(np.abs(f_transform_shift))


# using 0 will eventually result in a divide by zero error, so instead of elements being 0, they will be None
epsilon = .001


def high_pass_filter(matrix, threshold):
    rows, cols = matrix.shape
    row_threshold = min(threshold, rows) // 2
    col_threshold = min(threshold, cols) // 2
    crow, ccol = rows // 2, cols // 2
    matrix[crow - row_threshold:crow + row_threshold, ccol - col_threshold:ccol + col_threshold] = epsilon


def low_pass_filter(matrix, threshold):
    rows, cols = matrix.shape
    row_threshold = min(threshold, rows) // 2
    col_threshold = min(threshold, cols) // 2
    crow, ccol = rows // 2, cols // 2
    matrix[:crow - row_threshold, :] = epsilon
    matrix[crow + row_threshold:, :] = epsilon
    matrix[:, :ccol - col_threshold] = epsilon
    matrix[:, ccol + col_threshold:] = epsilon


def transformation_to_spectrum(transformation):
    return 20 * np.log(np.abs(transformation))


def transformation_to_image(transformation):
    return np.abs(np.fft.ifft2(np.fft.ifftshift(transformation)))


filter_size = 0

f_transform_high_pass = f_transform_shift.copy()
high_pass_filter(f_transform_high_pass, filter_size)
high_pass_magnitude_spectrum = transformation_to_spectrum(f_transform_high_pass)
high_pass_image = transformation_to_image(f_transform_high_pass)

f_transform_low_pass = f_transform_shift.copy()
low_pass_filter(f_transform_low_pass, filter_size)
low_pass_magnitude_spectrum = transformation_to_spectrum(f_transform_low_pass)
low_pass_image = transformation_to_image(f_transform_low_pass)


fig, (image_axes, spectrum_axes) = plt.subplots(2, 3)
original_image_ax, low_pass_image_ax, high_pass_image_ax = image_axes
original_spectrum_ax, low_pass_spectrum_ax, high_pass_spectrum_ax = spectrum_axes
for ax in image_axes:
    ax.set_xticks([])
    ax.set_yticks([])
for ax in spectrum_axes:
    ax.set_xticks([])
    ax.set_yticks([])


def update_axes():
    image_axes_args = dict(cmap='gray')
    original_image_ax.imshow(img, **image_axes_args)
    low_pass_image_ax.imshow(low_pass_image, **image_axes_args)
    high_pass_image_ax.imshow(high_pass_image, **image_axes_args)

    spectrum_axes_args = dict(cmap='gray')
    original_spectrum_ax.imshow(magnitude_spectrum.astype(float), **spectrum_axes_args)
    low_pass_spectrum_ax.imshow(low_pass_magnitude_spectrum.astype(float), **spectrum_axes_args)
    high_pass_spectrum_ax.imshow(high_pass_magnitude_spectrum.astype(float), **spectrum_axes_args)


update_axes()
growth_per_frame = 5


def init():
    global f_transform_high_pass
    f_transform_high_pass = f_transform_shift.copy()
    return ()


def animate(i):
    print(i)
    i = int(i ** 2)

    global high_pass_magnitude_spectrum, high_pass_image
    global low_pass_magnitude_spectrum, low_pass_image

    high_pass_filter(f_transform_high_pass, i)
    high_pass_magnitude_spectrum = transformation_to_spectrum(f_transform_high_pass)
    high_pass_image = transformation_to_image(f_transform_high_pass)

    f_transform_low_pass = f_transform_shift.copy()
    low_pass_filter(f_transform_low_pass, i)
    low_pass_magnitude_spectrum = transformation_to_spectrum(f_transform_low_pass)
    low_pass_image = transformation_to_image(f_transform_low_pass)

    update_axes()
    return low_pass_image_ax, high_pass_image_ax, low_pass_spectrum_ax, high_pass_spectrum_ax


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=int(max(*img.shape) ** .5 + 1), interval=100, blit=True)

plt.show()
