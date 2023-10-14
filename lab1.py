import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure('Цыкин Павел. 11 Вариант. Лабораторная работа №1', figsize=(7, 6))
plt.subplot(111, polar=True)
plt.title('ρ = a/ф')
A, B = map(int, input('A, B: ').split())
phi = np.arange(A, B, 0.05)
a = int(input('a: '))
rho = a * phi
plt.plot(phi, rho, lw=2)
plt.show()
