import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Constants
G = 1
M = 1
c = 1

# Initial position and velocity
x, y = -10.0, 1.0
vx, vy = 1.0, 0.0
dt = 0.01
steps = 2000

# Store trajectory
x_vals = [x]
y_vals = [y]

# Simulation loop
for _ in range(steps):
    r = np.sqrt(x**2 + y**2)
    if r < 1.5:
        break
    ax = -2 * G * M * x / r**3
    ay = -2 * G * M * y / r**3
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    x_vals.append(x)
    y_vals.append(y)

# Plot trajectory
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, color="blue", label="Light Ray")
plt.scatter(0, 0, color="black", s=50, label="Black Hole")
plt.xlabel("x (spatial coordinate)")
plt.ylabel("y (impact parameter)")
plt.title("Phase 1: Light Deflection near Black Hole (Newtonian Model)")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.tight_layout()

# Save plot
plt.savefig("phase1_newtonian_deflection.png", dpi=300)
plt.show()

