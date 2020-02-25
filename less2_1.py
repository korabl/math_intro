import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# парабола
x = np.linspace(-10, 10, 31)
y = x**2
plt.plot(x, y, color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title(r'График гиперболы $y = x^2$', fontsize = 16, y = 1.05)
plt.show()

# окружность
r = 3
x = np.linspace(-r, r, 1000)
y = []
y1 = []
for el in x:
    y.append(sqrt(r**2 - el**2))

for i in y[:]:
    i -= 2*i
    y1.append(i)

plt.plot(x,y)
plt.plot(x,y1)
plt.grid()
plt.show()

# эллипс
a = 5
b = 3
x1 = np.linspace(-a, a, 1000)
x = []
y = []
for el in x1:
    y.append(sqrt(((a**2)*(b**2) - (b**2)*(el**2))/a**2))

for el in x1[:]:
    z = (sqrt(((a**2)*(b**2) - (b**2)*(el**2))/a**2))
    z -= 2*z
    x.append(z)
plt.plot(x1, y)
plt.plot(x1, x)
plt.grid()
plt.show()

