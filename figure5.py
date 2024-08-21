import matplotlib.pyplot as plt
import numpy as np

a = 3
b = 1


theta = np.linspace(0, 2*np.pi, 100)
thetaUpper = np.linspace(0, np.pi, 100)
thetaLower = np.linspace(np.pi, 2*np.pi, 100)

x = a * np.cos(theta)
y = b * np.sin(theta)
xLower = a * np.cos(thetaLower)
yLower = b * np.sin(thetaLower)
xUpper = a * np.cos(thetaUpper)
yUpper = b * np.sin(thetaUpper)


plt.plot(xUpper, yUpper, linestyle='dashed', color='black', label='Upper Half', linewidth=1)
plt.plot(xLower, yLower, color='black', label='Lower Half')

plt.plot([0, 3], [0, 0], color='black', linewidth=1, linestyle='dashed')
plt.text(1.5, -0.3, '$r$', color='black')

plt.plot([0, 0], [0, 6], color='black', linewidth=1, linestyle='dashed')
plt.text(0.1, 3, '$h$', color='black')

plt.plot([0, 0.3], [0.3, 0.3], color='black', linewidth=1)
plt.plot([0.3, 0.3], [0, 0.3], color='black', linewidth=1)

plt.plot([-3.02, 0], [0, 6], color='black')
plt.plot([3.02, 0], [0, 6], color='black')

plt.axis('equal')
plt.axis('off')
plt.show()