# =======================================================
# Phase 3: Kerr Black Hole Light Bending - Static Plot
# =======================================================



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


# =======================================================
# Phase 3: Kerr Black Hole Light Bending - Animation
# =======================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# -------------------------------
# Phase 3: Kerr Animation
# -------------------------------

# Black hole parameters
M = 1       # Mass of black hole
a = 0.7     # Spin parameter

# Simulation parameters
dt = 0.01
steps = 4000

# Initial position and velocity of light
x, y = -10.0, 1.0
vx, vy = 1.0, 0.0

# Store trajectory
x_vals = []
y_vals = []

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

# Simulation to collect data
x_temp, y_temp = x, y
vx_temp, vy_temp = vx, vy

for _ in range(steps):
    r = np.sqrt(x_temp**2 + y_temp**2)
    if r <= 2*M:  # Event horizon
        break
    ax, ay = kerr_accel(x_temp, y_temp, M, a, vx_temp, vy_temp)
    vx_temp += ax * dt
    vy_temp += ay * dt
    x_temp += vx_temp * dt
    y_temp += vy_temp * dt
    x_vals.append(x_temp)
    y_vals.append(y_temp)

# Create animation
fig, ax = plt.subplots(figsize=(8, 8))

def init():
    ax.clear()
    ax.set_xlim(-11, 11)
    ax.set_ylim(-5, 5)
    ax.set_xlabel("x (spatial coordinate)", fontsize=12)
    ax.set_ylabel("y (impact parameter)", fontsize=12)
    ax.set_title("Phase 3: Light Deflection near Kerr Black Hole", 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    # Draw black hole
    ax.scatter(0, 0, color="black", s=200, label="Kerr Black Hole", zorder=5)
    ax.legend(fontsize=11)
    return []

def animate(frame):
    # Clear previous lines
    for line in ax.lines[:]:
        line.remove()
    for collection in ax.collections[1:]:  # Keep the black hole (first collection)
        collection.remove()
    
    # Plot trajectory up to current frame (show every 5th frame for speed)
    idx = min(frame * 5, len(x_vals))
    if idx > 0:
        line, = ax.plot(x_vals[:idx], y_vals[:idx], color="blue", linewidth=2, label=f"Light Ray (Kerr, a={a})")
        # Current position marker
        point = ax.scatter(x_vals[idx-1], y_vals[idx-1], color="red", s=100, zorder=10)
        return [line, point]
    
    return []

# Create animation
frames = len(x_vals) // 5
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, 
                              interval=20, blit=False, repeat=True)

# Save animation
print("Saving Phase 3 animation...")
writer = PillowWriter(fps=30)
anim.save("phase3_kerr_animation.gif", writer=writer)
print("Phase 3 animation saved as 'phase3_kerr_animation.gif'")
plt.close()
