from common import image_input, rgb_to_gray
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


plt.style.use('dark_background')


img = rgb_to_gray(image_input())

ny, nx = img.shape
x = np.linspace(0, nx, nx)
y = np.linspace(0, ny, ny)
xv, yv = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.gca(projection='3d')

mesh_args = dict(rstride=1, cstride=1, cmap='gray', edgecolor='none')
surf = ax.plot_surface(xv, yv, img, **mesh_args)


plt.axis('off')
ax.set_zlim(-2, 2)


def animate(i):
    ax.view_init(elev=90 - i, azim=90)
    return ax,


ani = animation.FuncAnimation(fig, animate, frames=90, interval=50, blit=True)

plt.show()
