# Phase 3: Kerr Black Hole Light Bending Simulation
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Black hole parameters
# -------------------------------
M = 1       # Mass of black hole
a = 0.7     # Spin parameter (0 = Schwarzschild, 1 = maximally spinning)

# -------------------------------
# 2. Simulation parameters
# -------------------------------
dt = 0.01
steps = 4000

# -------------------------------
# 3. Initial position and velocity of light
# -------------------------------
x, y = -10.0, 1.0
vx, vy = 1.0, 0.0
x_vals = [x]
y_vals = [y]

# -------------------------------
# 4. Simplified Kerr-inspired acceleration
# -------------------------------
def kerr_accel(x, y, M, a, vx, vy):
    r = np.sqrt(x**2 + y**2)
    
    # Basic Schwarzschild-like radial acceleration
    factor = 1 - 2*M/r
    ax = -2*M*x / (r**3 * factor)
    ay = -2*M*y / (r**3 * factor)
    
    # Add frame-dragging effect (simplified)
    ax += 0.1 * a * vy
    ay -= 0.1 * a * vx
    
    return ax, ay

# -------------------------------
# 5. Run simulation
# -------------------------------
for _ in range(steps):
    r = np.sqrt(x**2 + y**2)
    
    if r <= 2*M:  # Event horizon
        break
    
    ax, ay = kerr_accel(x, y, M, a, vx, vy)
    
    vx += ax * dt
    vy += ay * dt
    
    x += vx * dt
    y += vy * dt
    
    x_vals.append(x)
    y_vals.append(y)

# -------------------------------
# 6. Plot trajectory
# -------------------------------
plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, color="blue", linewidth=2, label=f"Light Ray (Kerr, a={a})")
plt.scatter(0, 0, color="black", s=100, label="Kerr Black Hole", zorder=5)
plt.xlabel("x (spatial coordinate)", fontsize=12)
plt.ylabel("y (impact parameter)", fontsize=12)
plt.title("Phase 3: Light Deflection near Kerr Black Hole", fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.tight_layout()

# -------------------------------
# 7. Save the figure
# -------------------------------
plt.savefig("phase3_kerr_deflection.png", dpi=300, bbox_inches='tight')
print("Plot saved successfully as 'phase3_kerr_deflection.png'")
plt.show()
