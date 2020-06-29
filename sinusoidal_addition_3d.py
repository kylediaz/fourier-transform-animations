import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.animation as animation
import math
import numpy as np


plt.style.use('dark_background')


x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = np.sin(X + Y)


fig = plt.figure()
mesh_args = dict(rstride=1, cstride=1, cmap='gray', edgecolor='none')

addend1_ax = fig.add_subplot(1, 3, 1, projection='3d')
addend1_Z = np.sin(X)
addend1_ax.plot_surface(X, Y, addend1_Z, **mesh_args)

addend2_ax = fig.add_subplot(1, 3, 2, projection='3d')
addend2_Z = np.sin(X)


ax = fig.add_subplot(1, 3, 3, projection='3d')

mesh = ax.plot_surface(X, Y, Z, **mesh_args)


def update(i):
    ax.collections = []
    addend2_ax.collections = []

    addend2_Z = np.sin(np.sin(.1 * i) * X + np.cos(.1 * i) * Y)
    addend2_ax.plot_surface(X, Y, addend2_Z, **mesh_args)
    Z = addend1_Z + addend2_Z
    ax.plot_surface(X, Y, Z, **mesh_args)

    return ax, addend2_ax


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_zlim(-2, 2)

anim = animation.FuncAnimation(fig, update, interval=20, blit=True)

plt.show()
