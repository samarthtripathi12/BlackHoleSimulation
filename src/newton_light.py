import numpy as np
import matplotlib.pyplot as plt

# Constants (natural units)
G = 1
M = 1

x, y = -10.0, 1.0
vx, vy = 1.0, 0.0
dt = 0.01

x_vals = []
y_vals = []

for _ in range(1000):
    r = np.sqrt(x**2 + y**2)
    if r < 1.5:
        break

    ax = -x / r**3
    ay = -y / r**3

    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt

    x_vals.append(x)
    y_vals.append(y)

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals)
plt.scatter(0, 0, label="Black Hole")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Newtonian Light Deflection (Toy Model)")
plt.legend()
plt.grid()
plt.show()

