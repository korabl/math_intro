import numpy as np
import matplotlib.pyplot as plt

# from scipy.optimize import fsolve
#
# def f(x):
#     return (np.sin(x + 1))
#
# x0 =  fsolve(f, 1)
# print (x0)

x = np.linspace(-10, 10, 201)
plt.plot(x)
# plt.plot([-10, 10],[0,0], color ='red', linewidth=0.75, linestyle ="--")
# plt.xlabel('x')
# plt.ylabel('y')
plt.grid(True)
plt.show()



