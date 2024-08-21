import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch


plt.plot([-3, 3], [0, 0], color='black')
plt.plot([-3, 0], [0, 5], color='black')
plt.plot([3, 0], [0, 5], color='black')

plt.plot([0, 0], [0, 5.8], color='black', linewidth=1)
plt.text(-0.3, 1.6, '$y_i$', color='black')
plt.plot([0, 2.04], [1.6, 1.6], color='black', linewidth=1)
plt.text(-0.3, 5.2, '$h$')
plt.text(1.02, 1.35, '$r_i$')
plt.text(1.5, -0.3, '$r$')
plt.text(-0.07, -0.3, '$0$')




plt.plot(0, 1.6, marker="o", color="black")
plt.plot(0, 0, marker="o", color="black")
plt.plot(3, 0, marker="o", color="black")
plt.plot(2.04, 1.6, marker="o", color="black")
plt.plot(0, 5, marker="o", color="black")

plt.plot([-0.15, 0], [5.65, 5.8], color='black', linewidth=1)
plt.plot([0.15, 0], [5.65, 5.8], color='black', linewidth=1)
plt.text(0.25, 5.65, '$y$', color='black')

plt.plot([3.75, 2.04], [1.6, 1.6], color='black', linewidth=1, linestyle='dashed')
plt.plot([3.75, 3.75], [0, 1.6], color='black', linewidth=1)
plt.plot([3.75, 3.6], [0, 0.15], color='black', linewidth=1)
plt.plot([3.75, 3.9], [0, 0.15], color='black', linewidth=1)
plt.plot([3.75, 3.6], [1.6, 1.45], color='black', linewidth=1)
plt.plot([3.75, 3.9], [1.6, 1.45], color='black', linewidth=1)
plt.text(3.9, 0.85, '$y_i$', color='black')

plt.plot([4.5, 0], [5, 5], color='black', linewidth=1, linestyle='dashed')
plt.plot([4.5, 4.5], [0, 5], color='black', linewidth=1)
plt.plot([4.5, 4.35], [5, 4.85], color='black', linewidth=1)
plt.plot([4.5, 4.65], [5, 4.85], color='black', linewidth=1)
plt.plot([4.5, 4.35], [0, 0.15], color='black', linewidth=1)
plt.plot([4.5, 4.65], [0, 0.15], color='black', linewidth=1)
plt.text(4.65, 2.55, '$h$', color='black')







x_start, y_start = 2, 3
x_end, y_end = 6, 8

plt.plot()

plt.axis('equal')
plt.axis('off')
plt.show()