# Трехмерный график двух параллельных плоскостей
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = figure()
ax = Axes3D(fig)

# Параллельные плоскости
# X = np.arange(-5, 5, 0.5)
# Y = np.arange(-5, 5, 0.5)
# X, Y = np.meshgrid(X, Y)
# Z = 2*X + 5*Y + 10
# ax.plot_wireframe(X, Y, Z)
#
# X1 = np.arange(-5, 5, 0.5)
# Y1 = np.arange(-5, 5, 0.5)
# X1, Y1 = np.meshgrid(X1, Y1)
# Z1 = 4*X + 10*Y - 18
# ax.plot_wireframe(X1, Y1, Z1, color='green')
#
# show()

# Поверхности второго порядка
# Первая
X = np.arange(-15, 15, 1)
Y = np.arange(-15, 15, 1)
X, Y = np.meshgrid(X, Y)
# Z = 1 - 3*(X**2) + 2*X*Y - Y**2
Z = (X**2)/3 - (Y**2)/2
ax.plot_wireframe(X, Y, Z)

# Вторая
# X1 = np.arange(-15, 15, 0.5)
# Y1 = np.arange(-15, 15, 0.5)
# X1, Y1 = np.meshgrid(X1, Y1)
# Z1 = ((2*((X1 + 4)**2) + 3*((Y1 - 3)**2))/12) - 1
# ax.plot_wireframe(X1, Y1, Z1, color='green')

show()
