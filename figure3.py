import matplotlib.pyplot as plt
import numpy as np

a = 9
b = 3
c = 9
d = 3
hInner = 3
vInner = 1
lower_hInner = 3
lower_vInner = 1

theta = np.linspace(0, 2*np.pi, 100)
thetaUpper = np.linspace(0, np.pi, 100)
thetaLower = np.linspace(np.pi, 2*np.pi, 100)

x = a * np.cos(theta)
y = b * np.sin(theta)
eLower = c * np.cos(thetaLower)
fLower = d * np.sin(thetaLower) - 3
eUpper = c * np.cos(thetaUpper)
fUpper = d * np.sin(thetaUpper) - 3
innerX = hInner * np.cos(theta)
innerY = vInner * np.sin(theta)
otherInnerX = lower_hInner * np.cos(theta)
otherInnerY = lower_vInner * np.sin(theta) - 3


plt.plot(innerX, innerY, color='black')
plt.plot(otherInnerX, otherInnerY, color='black', linestyle='dashed', linewidth = 1)
plt.plot(eUpper, fUpper, linestyle='dashed', color='black', label='Upper Half', linewidth=1)
plt.plot(eLower, fLower, color='black', label='Lower Half')

plt.plot(x, y, color='black')
plt.plot([-9.02, -9.02], [-3, 0], color='black')
plt.plot([9.02, 9.02], [-3, 0], color='black')
plt.plot([-3, -3], [-3, 0], color='black', linewidth=1, linestyle='dashed')
plt.plot([3, 3], [-3, 0], color='black', linewidth=1, linestyle='dashed')


plt.plot([0, 3], [3.5, 3.5], color='black')
plt.text(1.5, 3.7, 'r', color='black')
plt.scatter(0, 3.5, 5, marker="o", color="black")
plt.scatter(3, 3.5, 5, marker="o", color="black")

plt.plot([0, 9], [4.5, 4.5], color='black')
plt.text(4.5, 4.7, 'R', color='black')
plt.scatter(0, 4.5, 5, marker="o", color="black")
plt.scatter(9, 4.5, 5, marker="o", color="black")
plt.text(9.1, -1.5, '∆x', color='black')

plt.plot([0, 0], [4.5, -7.5], color='black', linewidth=1, linestyle='dashed')
plt.plot([3, 3], [3.5, 0], color='black', linewidth=1, linestyle='dashed')

plt.plot([9, 9], [0, 4.5], color='black', linewidth=1, linestyle='dashed')

plt.axis('equal')
plt.axis('off')
plt.show()
plt.savefig('figure3.jpg', format='jpeg')