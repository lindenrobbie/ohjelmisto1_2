import numpy as np
import matplotlib.pyplot as plt


angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]


angles_rad = np.radians(angles_deg)


x = np.cos(angles_rad)
y = np.sin(angles_rad)


theta = np.linspace(0, 2*np.pi, 100)
x_unit_circle = np.cos(theta)
y_unit_circle = np.sin(theta)


plt.figure(figsize=(6,6))
plt.plot(x_unit_circle, y_unit_circle, label='Yksikköympyrä')
plt.scatter(x, y, color='red')  # Merkitään kulmat
plt.xlabel('x-akseli')
plt.ylabel('y-akseli')
plt.title('Kulmat yksikköympyrällä')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')


for i, angle in enumerate(angles_deg):
    plt.text(x[i] + 0.05, y[i] + 0.05, f'{angle}°', fontsize=12, ha='center')

plt.legend()
plt.grid(True)
plt.show()