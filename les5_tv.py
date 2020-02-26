import numpy as np
import matplotlib.pyplot as plt
import itertools

# 1.0
'''Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро)'''
# for i in range(0, 37):
#     a = input()
#     x = np.random.uniform(0, 37)
#     if x < 18:
#         print('черное')
#     elif x == 37:
#         print('зероэ')
#     else:
#         print('красное')

# 2.1
'''Напишите код, проверяющий любую из теорем сложения или умножения вероятности 
на примере рулетки или подбрасывания монетки.'''

# p1, p2 = 0, 0
# k, m = 0, 0
# n = 100
# for i in range(0, n):
#     x = np.random.uniform(0, 10)
#     if x < 5:
# #        print("орел")
#         k += 1
#         p1 += 1/n
#     else:
# #        print("решка")
#         m += 1
#         p2 += 1/n
# print(f'Орел: {k}, решка: {m}, P(орел): {p1}, P(решка): {p2}, P: {p1 + p2}')

# 2.2
'''Сгенерируйте десять выборок случайных чисел х0, …, х9.
и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.'''

# z = [sum(np.random.rand(100)) for i in range(10)]
# n, bins, patches = plt.hist(z, 5)
# plt.xlabel('x')
# plt.ylabel('Probability')
# plt.title('Histogram')
# plt.show()

# 3.1
'''Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей 
(через биномиальное распределение) и сравните результаты.'''
# C(1, 2) => q^2 + 2pq + p^2 = 1 => (p + q)^2 = 1 => p + q = 1
#
# k, m = 0, 0
# n = 100
#
# for i in range(0, n):
#     x = np.random.uniform(0, 10)
#     if x < 5:
#         k += 1
#     else:
#         m +=1
#
# p_k = (n - m)/n
# p_m = (n - k)/n
#
# print(f'Орел: {k}, Решка: {m} \nP(орел): {p_k}, P(решка): {p_m}, P: {p_k + p_m}')

# 3.2
'''Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности 
из n независимых испытаний, взяв другие значения n и k.'''

k = 2
n = [i for i in range(3)]
c = 0
for p in itertools.combinations(n, k):
    c += 1

print(f'C({len(n)},{k}): {c}')
# какая то лажа


# 4
'''Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты 
перестановок для других значений n и k'''
# n = 6
# k = 4
# list_n = [i for i in range(n)]
# i = 0
# for p in itertools.permutations(list_n, k):
#     print(''.join(str(x) for x in p))
#     i += 1
# print(f'A({n},{k}): {i}')

