import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# -------------------------------
# Constants (geometrized units)
# -------------------------------
M = 1  # mass of black hole
dt = 0.01
steps = 4000

# -------------------------------
# Initial position and velocity of light ray
# -------------------------------
x, y = -10.0, 1.0  # starting position
vx, vy = 1.0, 0.0  # initial velocity

# -------------------------------
# Store trajectory points
# -------------------------------
x_vals = [x]
y_vals = [y]

# -------------------------------
# Schwarzschild acceleration function
# -------------------------------
def schwarzschild_accel(x, y, M):
    r = np.sqrt(x**2 + y**2)
    factor = (1 - 2*M/r)
    ax = -2*M*x / (r**3 * factor)
    ay = -2*M*y / (r**3 * factor)
    return ax, ay

# -------------------------------
# Simulation loop
# -------------------------------
for _ in range(steps):
    r = np.sqrt(x**2 + y**2)
    
    if r <= 2*M:  # Schwarzschild radius → stop if too close
        break
    
    ax, ay = schwarzschild_accel(x, y, M)
    
    vx += ax * dt
    vy += ay * dt
    
    x += vx * dt
    y += vy * dt
    
    x_vals.append(x)
    y_vals.append(y)

# -------------------------------
# Plot trajectory
# -------------------------------
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, color="blue", label="Light Ray (GR)")
plt.scatter(0, 0, color="black", s=50, label="Black Hole")
plt.xlabel("x (spatial coordinate)")
plt.ylabel("y (impact parameter)")
plt.title("Phase 2: Light Deflection near Schwarzschild Black Hole")
plt.legend()
plt.grid(True)
plt.axis('equal')  # equal scale for X and Y
plt.tight_layout()

# -------------------------------
# Save the figure
# -------------------------------
plt.savefig("phase2_schwarzschild_deflection.png", dpi=300)

# Show the plot
plt.show()

