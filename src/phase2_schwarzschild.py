# -------------------------------
# Phase 2: Schwarzschild Light Bending
# -------------------------------

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


# =======================================================
# Phase 2: Schwarzschild Light Bending - Animation
# =======================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# -------------------------------
# Phase 2: Schwarzschild Animation
# -------------------------------

# Constants (geometrized units, G=c=1)
M = 1  # mass of black hole

# Initial position and velocity
x, y = -10.0, 1.0
vx, vy = 1.0, 0.0
dt = 0.01
steps = 4000

# Store trajectory
x_vals = []
y_vals = []

def schwarzschild_accel(x, y, M):
    r = np.sqrt(x**2 + y**2)
    # Approximate GR correction: stronger near black hole
    factor = (1 - 2*M/r)
    ax = -2*M*x/(r**3 * factor)
    ay = -2*M*y/(r**3 * factor)
    return ax, ay

# Simulation to collect data
x_temp, y_temp = x, y
vx_temp, vy_temp = vx, vy

for _ in range(steps):
    r = np.sqrt(x_temp**2 + y_temp**2)
    if r < 2*M:   # Schwarzschild radius
        break
    ax, ay = schwarzschild_accel(x_temp, y_temp, M)
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
    ax.set_title("Phase 2: Light Deflection near Schwarzschild Black Hole", 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')
    # Draw black hole
    ax.scatter(0, 0, color="black", s=200, label="Black Hole", zorder=5)
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
        line, = ax.plot(x_vals[:idx], y_vals[:idx], color="blue", linewidth=2, label="Light Ray (GR)")
        # Current position marker
        point = ax.scatter(x_vals[idx-1], y_vals[idx-1], color="red", s=100, zorder=10)
        return [line, point]
    
    return []

# Create animation
frames = len(x_vals) // 5
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, 
                              interval=20, blit=False, repeat=True)

# Save animation
print("Saving Phase 2 animation...")
writer = PillowWriter(fps=30)
anim.save("phase2_schwarzschild_animation.gif", writer=writer)
print("Phase 2 animation saved as 'phase2_schwarzschild_animation.gif'")
plt.close()


