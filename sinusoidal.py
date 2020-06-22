import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = np.sin(X)


fig = plt.figure()
ax = plt.axes(projection='3d')

mesh_args = dict(rstride=1, cstride=1, cmap='gray', edgecolor='none')
mesh = ax.plot_surface(X, Y, Z, **mesh_args)


axis_label_args = dict(color='white')
ax.set_xlabel('x', **axis_label_args)
ax.set_ylabel('y', **axis_label_args)
ax.set_zlabel('z', **axis_label_args)
ax.set_facecolor('xkcd:black')
for axis in 'x', 'y', 'z':
    ax.tick_params(axis=axis, colors='white')

ax.set_zticks([-1, 0, 1])

ax.set_zlim(-1.5, 1.5)

fig.patch.set_facecolor('black')

plt.show()
