import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.animation as animation
import math
import numpy as np

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = np.sin(X + Y)


fig = plt.figure()
ax = plt.axes(projection="3d")

mesh_args = dict(rstride=1, cstride=1, cmap='winter', edgecolor='none')
mesh = ax.plot_surface(X, Y, Z, **mesh_args)


def update(i):
    ax.collections = []
    scalar = (math.sin(.1 * i) + 1) / 2
    Z = scalar * np.sin(X) + np.sin(X + Y)
    ax.plot_surface(X, Y, Z, **mesh_args)
    return ax,


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_zlim(-2, 2)

anim = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

plt.show()
