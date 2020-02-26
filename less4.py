import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0.01, 0.02, 500)
x = np.linspace(100, 500, 500)
k = np.linspace(0, 3, 100)

y = a * x
z = k * np.pi
plt.plot(y, color='red')
plt.plot(z)
plt.grid()

plt.show()

