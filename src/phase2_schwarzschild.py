# ======================================================= 
# Phase 2: Schwarzschild Light Bending - Complete
# Demonstrates General Relativity light bending near a black hole
# =======================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# -------------------------------
# PART 1: EULER METHOD (Shows Failure)
# -------------------------------
print("=" * 60)
print("PART 1: EULER APPROXIMATION (Demonstrates Instability)")
print("=" * 60)

# Constants
M = 1.0         # Black hole mass (in geometric units)
dt = 0.01       # Time step
steps = 4000    # Number of integration steps

# Initial conditions (photon starting position and velocity)
x, y = -10.0, 1.0
vx, vy = 1.0, 0.0
x_vals_euler = [x]
y_vals_euler = [y]

def schwarzschild_accel(x, y, M):
    r = np.sqrt(x**2 + y**2)
    factor = (1 - 2*M/r)
    ax = -2*M*x/(r**3 * factor)
    ay = -2*M*y/(r**3 * factor)
    return ax, ay

# Euler integration loop
for _ in range(steps):
    r = np.sqrt(x**2 + y**2)
    if r <= 2*M:
        break
    ax, ay = schwarzschild_accel(x, y, M)
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    x_vals_euler.append(x)
    y_vals_euler.append(y)

print(f"✓ Euler integration complete: {len(x_vals_euler)} points")
print(f"  Note: Euler method is UNSTABLE and INACCURATE for this problem")

# Plot Euler result
plt.figure(figsize=(6,6))
plt.plot(x_vals_euler, y_vals_euler, color="blue", label="Euler Trajectory (WRONG)")
plt.scatter(0, 0, color="black", s=80, label="Black Hole")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Phase 2: Schwarzschild Light Bending (Euler - FAILS)")
plt.legend()
plt.axis("equal")
plt.grid(True)
plt.savefig("data/phase2_schwarzschild_deflection.png", dpi=300)  # matches README
plt.close()

# Euler Animation
fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim(-11,11)
ax.set_ylim(-5,5)
ax.set_aspect("equal")
ax.set_title("Phase 2: Euler Approximation (Demonstrates Failure)")
ax.scatter(0,0,color="black", s=80)
line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], "ro")

def update_euler(frame):
    if frame > 0:
        line.set_data(x_vals_euler[:frame], y_vals_euler[:frame])
        point.set_data([x_vals_euler[frame-1]], [y_vals_euler[frame-1]])
    return line, point

ani_euler = FuncAnimation(fig, update_euler, frames=len(x_vals_euler), interval=20)
ani_euler.save("data/phase2_schwarzschild_animation.gif", writer=PillowWriter(fps=30))  # matches README
plt.close()
print("✓ Euler plots saved\n")

# -------------------------------
# PART 2: RK4 METHOD (Correct GR Solution)
# -------------------------------
print("=" * 60)
print("PART 2: RK4 INTEGRATION (Correct General Relativity)")
print("=" * 60)

def schwarzschild_geodesic(u, du, M=1.0):
    return -u + 3*M*u**2

def rk4_step(u, du, dphi, M=1.0):
    k1 = dphi * schwarzschild_geodesic(u, du, M)
    l1 = dphi * du
    k2 = dphi * schwarzschild_geodesic(u + 0.5*l1, du + 0.5*k1, M)
    l2 = dphi * (du + 0.5*k1)
    k3 = dphi * schwarzschild_geodesic(u + 0.5*l2, du + 0.5*k2, M)
    l3 = dphi * (du + 0.5*k2)
    k4 = dphi * schwarzschild_geodesic(u + l3, du + k3, M)
    l4 = dphi * (du + k3)
    du_new = du + (k1 + 2*k2 + 2*k3 + k4)/6
    u_new = u + (l1 + 2*l2 + 2*l3 + l4)/6
    return u_new, du_new

def integrate_rk4(r0=10.0, b=3.0, M=1.0, dphi=0.001, max_steps=20000):
    u0 = 1.0/r0
    du0 = np.sqrt(1.0/b**2 - u0**2*(1 - 2*M/r0))
    phi_vals, r_vals = [], []
    u, du = u0, du0
    phi = np.pi
    for _ in range(max_steps):
        r = 1/u
        if r <= 1.51*M or r > 50:
            break
        phi_vals.append(phi)
        r_vals.append(r)
        u, du = rk4_step(u, du, dphi, M)
        phi += dphi
    return np.array(phi_vals), np.array(r_vals)

def polar_to_cartesian(phi_vals, r_vals):
    x = r_vals * np.cos(phi_vals)
    y = r_vals * np.sin(phi_vals)
    return x, y

# Run RK4 integration
print("Integrating geodesic equation...")
phi_vals, r_vals = integrate_rk4(r0=10.0, b=3.0)
x_rk4, y_rk4 = polar_to_cartesian(phi_vals, r_vals)
print(f"✓ RK4 integration complete: {len(x_rk4)} points")
print(f"  Closest approach: {np.min(r_vals):.3f} Rs")
print(f"  Photon sphere at: 1.500 Rs")

# Plot RK4 result (no filename change needed)
plt.figure(figsize=(8,8))
plt.plot(x_rk4, y_rk4, color='blue', linewidth=2, label='Light Ray (RK4 - CORRECT)')
plt.scatter(0, 0, color='black', s=100, label='Black Hole', zorder=5)
circle = plt.Circle((0,0), 1.5*M, color='red', fill=False, linestyle='--', linewidth=2, label='Photon Sphere (1.5 Rs)')
plt.gca().add_patch(circle)
plt.xlabel('x (Schwarzschild radii)')
plt.ylabel('y (Schwarzschild radii)')
plt.title('Phase 2: Schwarzschild Light Bending (RK4 - General Relativity)')
plt.legend()
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.xlim(-12,12)
plt.ylim(-8,8)
plt.savefig('data/phase2_schwarzschild_single_ray.png', dpi=300)  # matches README
plt.close()

# RK4 Animation (no filename change needed)
fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim(-12,12)
ax.set_ylim(-8,8)
ax.set_aspect('equal')
ax.scatter(0,0,color='black', s=100, zorder=5)
circle = plt.Circle((0,0), 1.5*M, color='red', fill=False, linestyle='--', linewidth=2)
ax.add_patch(circle)
horizon = plt.Circle((0,0), 2.0*M, color='gray', fill=False, linestyle=':', linewidth=1, alpha=0.5)
ax.add_patch(horizon)
line, = ax.plot([], [], lw=2, color='blue')
point, = ax.plot([], [], 'ro', markersize=8)
def update(frame):
    if frame > 0:
        line.set_data(x_rk4[:frame], y_rk4[:frame])
        point.set_data([x_rk4[frame-1]], [y_rk4[frame-1]])
    return line, point
frames_to_use = list(range(0,len(x_rk4),10))
ani = FuncAnimation(fig, update, frames=frames_to_use, interval=20)
ani.save('data/phase2_schwarzschild_animation.gif', writer=PillowWriter(fps=30))  # matches README
plt.close()

print("✓ RK4 plots saved\n")
