from sys import argv
from os import path
import matplotlib.image as mpimg
import numpy as np


def image_input():
    if len(argv) > 1:
        file_path = argv[1]
    else:
        file_path = ''
    while not path.exists(file_path):
        file_path = input('Input image path > ')
    return mpimg.imread(file_path)


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])
