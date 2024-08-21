import matplotlib.pyplot as plt
import numpy as np

a = 8
b = 3
c = 8
d = 3

theta = np.linspace(0, 2*np.pi, 100)
thetaUpper = np.linspace(0, np.pi, 100)
thetaLower = np.linspace(np.pi, 2*np.pi, 100)

x = a * np.cos(theta)
y = b * np.sin(theta)
eLower = c * np.cos(thetaLower)
fLower = d * np.sin(thetaLower) - 2
eUpper = c * np.cos(thetaUpper)
fUpper = d * np.sin(thetaUpper) - 2


plt.plot(eUpper, fUpper, linestyle='dashed', color='black', label='Upper Half', linewidth=1)
plt.plot(eLower, fLower, color='black', label='Lower Half')

plt.plot(x, y, color='black')
plt.plot([-8.01, -8.01], [-2, 0], color='black')
plt.plot([8, 8.01], [-2, 0], color='black')

labelText = r'r'
plt.plot([-8, 0], [0, 0], color='black', linewidth=1)


plt.text(-4, 0.1, labelText, color="black")
plt.plot(0, 0, marker="o", color="black")
plt.text(8.1, -1, '∆x', color='black')

plt.axis('equal')
plt.axis('off')
plt.show()