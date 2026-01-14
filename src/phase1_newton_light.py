# -------------------------------
# Phase 1: Newtonian Light Bending
# -------------------------------

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



# -------------------------------
# Part B: Animation
# -------------------------------
# Reset initial conditions

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# -------------------------------
# Phase 1: Newtonian Animation
# -------------------------------

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
x_vals = []
y_vals = []

# Simulation to collect data
x_temp, y_temp = x, y
vx_temp, vy_temp = vx, vy

for _ in range(steps):
    r = np.sqrt(x_temp**2 + y_temp**2)
    if r < 1.5:
        break
    ax = -2 * G * M * x_temp / r**3
    ay = -2 * G * M * y_temp / r**3
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
    ax.set_title("Phase 1: Light Deflection near Black Hole (Newtonian Model)", 
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
        line, = ax.plot(x_vals[:idx], y_vals[:idx], color="blue", linewidth=2, label="Light Ray")
        # Current position marker
        point = ax.scatter(x_vals[idx-1], y_vals[idx-1], color="red", s=100, zorder=10)
        return [line, point]
    
    return []

# Create animation
frames = len(x_vals) // 5
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, 
                              interval=20, blit=False, repeat=True)

# Save animation
print("Saving Phase 1 animation...")
writer = PillowWriter(fps=30)
anim.save("phase1_newtonian_animation.gif", writer=writer)
print("Phase 1 animation saved as 'phase1_newtonian_animation.gif'")
plt.close()

