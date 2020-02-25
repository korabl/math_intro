import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve

# 1.0
x = np.linspace(-2*np.pi, 3*np.pi, 201)
y = np.cos(x - 2) + 3
y1 = 2*np.cos(x - 6) + 1
y2 = 1/2*np.cos(x + 2) - 2
plt.plot(x, y)
plt.plot(x, y1, color='red')
plt.plot(x, y2, color='brown')
plt.grid(True)
plt.show()

# 3.1 Перевести полярные координаты в декартовы
P_x = int(input('p(x): '))
Fi_x_grad = int(input('fi(x): '))
Fi_x_rad = (Fi_x_grad*np.pi)/180
x = P_x*round(np.cos(Fi_x_rad), 3)
y = P_x*round(np.sin(Fi_x_rad), 3)

print(f'x: {x}, y: {y}')

# 3.2 График окружности в полярных координатах
p = 5
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.linspace(p, p, 100)
plt.polar(x, y)
plt.grid()
plt.show()

3.3 График отрезка прямой в полярных координатах
x = np.linspace(-20, 20, 50)
r = []
for el in x:
    r.append(np.pi/4)
plt.polar(r, x)
plt.show()

# 4.1
x = np.linspace(-4, 6)
plt.plot(x, ((np.exp(x) - 1) / x) + 1)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 5)
plt.grid(True)

def equations(p):
    x, y = p
    return (y - x ** 2 + 1, np.exp(x) + x*(1 - y) - 1)

x1, y1 = fsolve(equations, [-4, 6])
print(f'{x1}, {y1}')

plt.show()

