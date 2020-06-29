import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


plt.style.use('dark_background')


x = np.linspace(-6, 6, 100)
y = np.linspace(-6, 6, 2)

X, Y = np.meshgrid(x, y)
Z = np.sin(X)


fig = plt.figure()
ax = plt.axes(projection='3d')

mesh_args = dict(rstride=1, cstride=1, cmap='gray', edgecolor='none')
mesh = ax.plot_surface(X, Y, Z, **mesh_args)


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Intensity')

ax.set_zticks([-1, 0, 1])
ax.set_zlim(-1.5, 1.5)


def animate(i):
    ax.view_init(elev=0, azim=(i - 45) / 2)
    return ax,


ani = animation.FuncAnimation(fig, animate, frames=720, interval=20, blit=True)

plt.show()
