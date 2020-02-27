import numpy as np
import matplotlib.pyplot as plt
import itertools
import math

# 1.0
'''Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро)'''
for i in range(0, 37):
    a = input()
    x = np.random.uniform(0, 37)
    if x < 18:
        print('черное')
    elif x == 37:
        print('зероэ')
    else:
        print('красное')

# 2.1
'''Напишите код, проверяющий любую из теорем сложения или умножения вероятности 
на примере рулетки или подбрасывания монетки.'''

p1, p2 = 0, 0
k, m = 0, 0
n = 100
for i in range(0, n):
    x = np.random.uniform(0, 10)
    if x < 5:
#        print("орел")
        k += 1
        p1 += 1/n
    else:
#        print("решка")
        m += 1
        p2 += 1/n
print(f'Орел: {k}, решка: {m}, P(орел): {p1}, P(решка): {p2}, P: {p1 + p2}')

# 2.2
'''Сгенерируйте десять выборок случайных чисел х0, …, х9.
и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.'''

z = [sum(np.random.rand(100)) for i in range(10)]
n, bins, patches = plt.hist(z, 5)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()

# 3.1
'''Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей 
(через биномиальное распределение) и сравните результаты.'''

k, m = 0, 0
n = 5
el_events = [i for i in range(n + 1)]
p_success = 0.5

for i in range(0, n):
    x = np.random.uniform(0, 10)
    if x < 5:
        k += 1
    else:
        m +=1

def result_p(i):
    comb = math.factorial(n)/(math.factorial(i) * (math.factorial(n - i)))
    current_p = p_success**i
    current_q = (1 - p_success)**(n - i)
    return round(comb * current_p * current_q, 4)

print(f'Орел: {k}, Решка: {m}\nP({k}) орла из {n}: {result_p(k) * 100}%')

# 3.2
'''Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности 
из n независимых испытаний, взяв другие значения n и k.'''

# Расчет сочетаний сделан через факториал, потому что так быстрее производительность на больших числах
n = 10
el_events = [i for i in range(n + 1)]
p_success = 0.3

for i in el_events:
    comb = math.factorial(n)/(math.factorial(i) * (math.factorial(n - i)))
    current_p = p_success**i
    current_q = (1 - p_success)**(n - i)
    result = comb * current_p * current_q
    print(f'P({i}) из {n}: {round(result, 5)}')

# 4
'''Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты 
перестановок для других значений n и k'''

n = 6
k = 4
list_n = [i for i in range(n)]
i = 0
for p in itertools.permutations(list_n, k):
    print(''.join(str(x) for x in p))
    i += 1
print(f'A({n},{k}): {i}')

# 5
'''Дополните код расчетом коэффициента корреляции x и y по формуле'''
x = [1, 34, 12, 11, 16, 17, 20, 25, 1]
y = [0, 0, 11, 9, 8, 7, 6, 55, 20]

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

print(pearson_def(x, y))