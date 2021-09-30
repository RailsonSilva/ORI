from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection = '3d')

x = np.arange(-20, 20.5, 0.5)
y = np.arange(-20, 20.5, 0.5)

X, Y = np.meshgrid(x, y) # gera a matrizes X e Y  que representam o produto cartesiano entre x e y

Z = -(X**2)/6 + (Y**2)/4

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride = 1, cmap = cm.jet)
fig.colorbar(surf)

plt.show()