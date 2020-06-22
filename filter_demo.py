from common import image_input, rgb_to_gray
import numpy as np
from matplotlib import pyplot as plt

img = rgb_to_gray(image_input())

f_transform = np.fft.fft2(img)
f_transform_shift = np.fft.fftshift(f_transform)
magnitude_spectrum = 20 * np.log(np.abs(f_transform_shift))

rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
filter_size = 40
s = filter_size // 2

f_transform_high_pass = f_transform_shift.copy()
f_transform_high_pass[crow - s:crow + s, ccol - s:ccol + s] = 0.01
high_pass_magnitude_spectrum = 20 * np.log(np.abs(f_transform_high_pass))
high_pass_image = np.abs(np.fft.ifft2(np.fft.ifftshift(f_transform_high_pass)))

f_transform_low_pass = f_transform_shift.copy()
f_transform_low_pass[:crow - s, :] = 0.01
f_transform_low_pass[crow + s:, :] = 0.01
f_transform_low_pass[:, :ccol - s] = 0.01
f_transform_low_pass[:, ccol + s:] = 0.01
low_pass_magnitude_spectrum = 20 * np.log(np.abs(f_transform_low_pass))
low_pass_image = np.abs(np.fft.ifft2(np.fft.ifftshift(f_transform_low_pass)))


fig, (image_axes, spectrum_axes) = plt.subplots(2, 3)
original_image_ax, low_pass_image_ax, high_pass_image_ax = image_axes
original_spectrum_ax, low_pass_spectrum_ax, high_pass_spectrum_ax = spectrum_axes
for ax in image_axes:
    ax.set_xticks([])
    ax.set_yticks([])
for ax in spectrum_axes:
    ax.set_xticks([])
    ax.set_yticks([])


fig.patch.set_facecolor('xkcd:black')

image_axes_args = dict(cmap='gray')
original_image_ax.imshow(img, **image_axes_args)
low_pass_image_ax.imshow(low_pass_image, **image_axes_args)
high_pass_image_ax.imshow(high_pass_image, **image_axes_args)

spectrum_axes_args = dict(cmap='gray')
original_spectrum_ax.imshow(magnitude_spectrum.astype(float), **spectrum_axes_args)
low_pass_spectrum_ax.imshow(low_pass_magnitude_spectrum.astype(float), **spectrum_axes_args)
high_pass_spectrum_ax.imshow(high_pass_magnitude_spectrum.astype(float), **spectrum_axes_args)

plt.show()
