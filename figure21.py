import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 0.05 * (x - 1) * (x - 3) * (x - 6) + 3

x = np.linspace(0, 7)
y = f(x)

plt.plot([-1, -1], [1, 4.75], linewidth=1, color='black')
plt.plot([-1, 7.5], [1, 1], linewidth=1, color='black')

plt.plot(x, y, label='$y = 0.05(x-1)(x-3)(x-6)+3$', color='black', linewidth=2)
plt.plot([-1, 7], [4.2, 4.2], color='black', linewidth=1, linestyle='dashed')
plt.text(-1.5, 4.1, '$f(b)$', color='black')
plt.plot([-1, 0], [2.1, 2.1], color='black', linewidth=1, linestyle='dashed')
plt.text(-1.5, 2, '$f(a)$', color='black')
plt.text(-0.06, 0.75, '$a$', color='black')
plt.text(6.94, 0.75, '$b$', color='black')

plt.plot([0, 0], [1, 2.1], color='black', linewidth=1, linestyle='dashed')
plt.plot([7, 7], [1, 4.2], color='black', linewidth=1, linestyle='dashed')

plt.plot([-1, -1.15], [4.75, 4.6], linewidth=1, color='black')
plt.plot([-1, -0.85], [4.75, 4.6], linewidth=1, color='black')

plt.plot([7.5, 7.35], [1, 0.85], linewidth=1, color='black')
plt.plot([7.5, 7.35], [1, 1.15], linewidth=1, color='black')


plt.text(2.5, 4.5, '$y = f(x)$', color='black')
plt.plot(0, 2.1, marker="o", color="black")
plt.text(0.25, 1.95, '$A$', color='black')
plt.plot(7, 4.2, marker="o", color="black")
plt.text(7.25, 4.1, '$B$', color='black')

plt.text(7.7, 0.9, '$x$', color='black')
plt.text(-1.1, 5.05, '$y$', color='black')
plt.text(-1.2, 0.7, '$0$', color='black')
plt.axis('equal')
plt.axis('off')
plt.show()
