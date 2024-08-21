import matplotlib.pyplot as plt
import numpy as np

n=256
x = np.linspace(np.pi, 4 * np.pi, n, endpoint=True)
y = 2 * np.sin(x - 2 * np.pi) + 5

plt.plot(y, x, color='black', alpha=1.0)
plt.plot([0, 0], [2, 14], color='black', linewidth=1)
plt.plot([0, 9], [2, 2], color='black', linewidth=1)

plt.plot(5, np.pi, marker="o", color="black")
plt.plot(5, 4 * np.pi, marker="o", color="black")

plt.plot([0, 5], [np.pi, np.pi], color='black', linewidth=1, linestyle='dashed')
plt.text(-0.5, 3.08, 'c', color='black')
plt.plot([0, 5], [4 * np.pi, 4 * np.pi], color='black', linewidth=1, linestyle='dashed')
plt.text(-0.5, 12.42, 'd', color='black')

plt.plot([-0.15, 0], [13.85, 14], linewidth=1, color='black')
plt.plot([0.15, 0], [13.85, 14], linewidth=1, color='black')

plt.plot([8.85, 9], [2.15, 2], linewidth=1, color='black')
plt.plot([8.85, 9], [1.85, 2], linewidth=1, color='black')

plt.text(7.5, 7.85, 'x = g(y)', color='black')
plt.text(9.6, 1.82, 'x', color='black')
plt.text(-0.18, 14.82, 'y', color='black')

plt.axis('equal')
plt.axis('off')
plt.show()