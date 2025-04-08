import numpy as np
import matplotlib.pyplot as plt


angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]


angles_rad = np.radians(angles_deg)


x = np.cos(angles_rad)
y = np.sin(angles_rad)


theta = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
x_unit_circle = np.cos(theta)
y_unit_circle = np.sin(theta)


plt.figure(figsize=(19.2, 14.4))
plt.plot(theta, x_unit_circle, color='green', linestyle='--', label='cos(x)')
plt.plot(theta, y_unit_circle, color='blue', linestyle=':', label='sin(x)')
plt.scatter(x, y, color='red', zorder=5)


for i, angle in enumerate(angles_deg):
    plt.text(x[i] + 0.05, y[i] + 0.05, f'{angle}°', fontsize=12, ha='center')


plt.legend(loc='upper right')


plt.xlabel('x-akseli')
plt.ylabel('y-akseli')
plt.title('Kulmat yksikköympyrällä')


plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')


plt.grid(True)


plt.show()