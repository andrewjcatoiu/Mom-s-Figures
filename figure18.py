import matplotlib.pyplot as plt
import numpy as np

n=256
x = np.linspace(1, 6.1, n, endpoint=True)
y = 0.8 * np.sin(x) + 2

fig, ax = plt.subplots()
ax.plot(x, y, color='black', alpha=1.0)
ax.fill_between(x, 1.85, y, color='grey', alpha=.2)
ax.plot([-1, 6], [1.85, 1.85], linewidth=1, linestyle='dashed', color='black')


ax.plot([-1, -1], [0, 4], linewidth=1, color='black')
ax.text(-1.5, 1.94, '$f(c)$', color='black')
ax.plot([-1, 2 * np.pi + 1], [0, 0], linewidth=1, color='black')
ax.plot([-1.15, -1], [3.85, 4], linewidth=1, color='black')
ax.plot([-0.85, -1], [3.85, 4], linewidth=1, color='black')
ax.text(-1.4, 3.5, '$y$', color='black')
ax.plot([2 * np.pi + 1, 2 * np.pi + 0.85], [0, -0.15], linewidth=1, color='black')
ax.plot([2 * np.pi + 1, 2 * np.pi + 0.85], [0, 0.15], linewidth=1, color='black')
ax.text(2 * np.pi + 0.6, -0.4, '$x$', color='black')


ax.plot([1, 1], [0, 2.67], linestyle='dashed', linewidth=1, color='black')
ax.text(0.94, -0.25, '$a$', color='black')
ax.plot([3.35, 3.35], [0, 1.85], linestyle='dashed', linewidth=1, color='black')
ax.text(3.29, -0.25, '$c$', color='black')
plt.plot(3.35, 1.85, marker="o", color="black")

ax.plot([6.1, 6.1], [0, 1.85], linestyle='dashed', linewidth=1, color='black')
ax.text(6.04, -0.25, '$b$', color='black')
ax.text(2 * np.pi + 0.25, 1.94, '$y = f(x)$', color='black')
ax.text(-1.2, -0.3, '$0$', color='black')
ax.plot([np.pi / 2, np.pi - 0.3], [2.4, 3.4], color='black', linewidth=1)
ax.text(np.pi - 0.2, 3.4, 'area A$_1$', color='black')
ax.plot([3 * (np.pi / 2), (2 * np.pi) - 0.3], [1.6, 2.6], color='black', linewidth=1)
ax.text((2 * np.pi) - 0.2, 2.6, 'area A$_2$', color='black')



plt.axis('equal')
plt.axis('off')
plt.show()