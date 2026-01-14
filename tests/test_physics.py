import numpy as np

# Photon closest approach should be around r ~ 1.5
x, y = -10.0, 1.0
dx, dy = 0.1, 0.0
dt = 0.01
r_min = 10

for _ in range(2000):
    r = np.sqrt(x**2 + y**2)
    if r < r_min:
        r_min = r
    ax = -2 * x / r**3
    ay = -2 * y / r**3
    dx += ax * dt
    dy += ay * dt
    x += dx * dt
    y += dy * dt
    if r < 1.5:
        break

print("Minimum approach distance:", r_min)

