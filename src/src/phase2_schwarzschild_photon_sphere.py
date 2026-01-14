import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Constants (units: G = c = 1)
G = 1.0
M = 1.0

# Initial conditions
x0, y0 = -10.0, 1.0
vx0, vy0 = 1.0, 0.0
dt = 0.01
steps = 3000

# Compute trajectory (Euler)
def compute_trajectory():
    x, y = x0, y0
    vx, vy = vx0, vy0
    xs, ys = [], []
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
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)

# Static Plot
def make_static_plot(x, y):
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Light Ray (Euler)")
    plt.scatter(0, 0, color="black", s=80, label="Central Mass")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Phase 1: Newtonian Light Deflection (Euler)")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.savefig("phase1_newton_static.png", dpi=300)
    plt.close()

# Animation
def make_animation(x, y):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-11, 11)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.set_title("Phase 1: Newtonian Light Deflection")
    ax.scatter(0, 0, color="black", s=80)
    line, = ax.plot([], [], lw=2)
    point, = ax.plot([], [], "ro")
    
    def update(frame):
        if frame > 0:
            line.set_data(x[:frame], y[:frame])
            point.set_data([x[frame-1]], [y[frame-1]])
        return line, point
    
    ani = FuncAnimation(fig, update, frames=len(x), interval=20)
    ani.save("phase1_newton_animation.gif", writer=PillowWriter(fps=30))
    plt.close()

# Main Execution
if __name__ == "__main__":
    x, y = compute_trajectory()
    make_static_plot(x, y)
    make_animation(x, y)
    print("Phase 1 complete!")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

M = 1.0
dt = 0.01
steps = 4000

print("="*70)
print("EULER vs RK4 COMPARISON")
print("="*70)

# ===== PART 1: EULER METHOD =====
x, y = -10.0, 1.0
vx, vy = 1.0, 0.0
x_euler = [x]
y_euler = [y]

def schwarzschild_accel(x, y, M):
    r = np.sqrt(x**2 + y**2)
    if r < 2.1*M:
        return 0, 0
    factor = (1 - 2*M/r)
    if factor < 0.01:
        factor = 0.01
    ax = -2*M*x/(r**3 * factor)
    ay = -2*M*y/(r**3 * factor)
    return ax, ay

for _ in range(steps):
    r = np.sqrt(x**2 + y**2)
    if r <= 2*M or r > 50:
        break
    ax, ay = schwarzschild_accel(x, y, M)
    vx += ax * dt
    vy += ay * dt
    x += vx * dt
    y += vy * dt
    x_euler.append(x)
    y_euler.append(y)

x_euler = np.array(x_euler)
y_euler = np.array(y_euler)
print(f"Euler: {len(x_euler)} points, closest: {np.min(np.sqrt(x_euler**2 + y_euler**2)):.3f} Rs")

# ===== PART 2: RK4 METHOD =====
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
    du0 = np.sqrt(1.0/b**2 - u0**2*(1 - 2*M*r0))
    phi_vals, r_vals = [], []
    u, du, phi = u0, du0, np.pi
    
    for _ in range(max_steps):
        r = 1/u
        if r <= 1.51*M or r > 50:
            break
        phi_vals.append(phi)
        r_vals.append(r)
        u, du = rk4_step(u, du, dphi, M)
        phi += dphi
    
    return np.array(phi_vals), np.array(r_vals)

phi_vals, r_vals = integrate_rk4(r0=10.0, b=3.0)
x_rk4 = r_vals * np.cos(phi_vals)
y_rk4 = r_vals * np.sin(phi_vals)
print(f"RK4: {len(x_rk4)} points, closest: {np.min(r_vals):.3f} Rs")

# ===== PART 3: SIDE-BY-SIDE PLOT =====
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Euler
ax1.plot(x_euler, y_euler, 'r-', linewidth=2, label='Euler (WRONG)')
ax1.scatter(0, 0, color='black', s=150, label='Black Hole', zorder=5)
circle1 = plt.Circle((0,0), 1.5*M, color='orange', fill=False, 
                     linestyle='--', linewidth=2, label='Photon Sphere')
ax1.add_patch(circle1)
ax1.set_xlim(-12, 12)
ax1.set_ylim(-8, 8)
ax1.set_aspect('equal')
ax1.set_title('EULER METHOD (Unstable)', fontsize=14, fontweight='bold', color='red')
ax1.legend()
ax1.grid(True, alpha=0.3)

# RK4
ax2.plot(x_rk4, y_rk4, 'b-', linewidth=2, label='RK4 (CORRECT)')
ax2.scatter(0, 0, color='black', s=150, label='Black Hole', zorder=5)
circle2 = plt.Circle((0,0), 1.5*M, color='orange', fill=False, 
                     linestyle='--', linewidth=2, label='Photon Sphere')
ax2.add_patch(circle2)
ax2.set_xlim(-12, 12)
ax2.set_ylim(-8, 8)
ax2.set_aspect('equal')
ax2.set_title('RK4 METHOD (Stable)', fontsize=14, fontweight='bold', color='blue')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('comparison_side_by_side.png', dpi=300)
plt.close()

# ===== PART 4: OVERLAY PLOT =====
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x_euler, y_euler, 'r-', linewidth=2.5, label='Euler (WRONG)', alpha=0.7)
ax.plot(x_rk4, y_rk4, 'b-', linewidth=2.5, label='RK4 (CORRECT)', alpha=0.7)
ax.scatter(0, 0, color='black', s=200, label='Black Hole', zorder=5)
circle = plt.Circle((0,0), 1.5*M, color='orange', fill=False, 
                    linestyle='--', linewidth=2.5, label='Photon Sphere')
ax.add_patch(circle)
ax.set_xlim(-12, 12)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')
ax.set_title('EULER vs RK4: Direct Comparison', fontsize=15, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.savefig('comparison_overlay.png', dpi=300)
plt.close()

# ===== PART 5: DISTANCE PLOT =====
fig, ax = plt.subplots(figsize=(12, 6))
r_euler = np.sqrt(x_euler**2 + y_euler**2)
ax.plot(r_euler, 'r-', linewidth=2, label='Euler', alpha=0.8)
ax.plot(r_vals, 'b-', linewidth=2, label='RK4', alpha=0.8)
ax.axhline(y=1.5, color='orange', linestyle='--', linewidth=2, label='Photon Sphere')
ax.axhline(y=2.0, color='gray', linestyle=':', linewidth=2, label='Event Horizon')
ax.set_xlabel('Integration Step', fontsize=12)
ax.set_ylabel('Distance from Black Hole (Rs)', fontsize=12)
ax.set_title('Radial Distance vs Steps', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 12)
plt.savefig('comparison_distance.png', dpi=300)
plt.close()

# ===== PART 6: ANIMATION =====
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

for ax in [ax1, ax2]:
    ax.set_xlim(-12, 12)
    ax.set_ylim(-8, 8)
    ax.set_aspect('equal')
    ax.scatter(0, 0, color='black', s=120, zorder=5)
    ax.grid(True, alpha=0.3)
    circle = plt.Circle((0,0), 1.5*M, color='orange', fill=False, linestyle='--', linewidth=2)
    ax.add_patch(circle)

ax1.set_title('EULER', fontsize=13, fontweight='bold', color='red')
ax2.set_title('RK4', fontsize=13, fontweight='bold', color='blue')

line1, = ax1.plot([], [], 'r-', lw=2)
point1, = ax1.plot([], [], 'ro', markersize=10)
line2, = ax2.plot([], [], 'b-', lw=2)
point2, = ax2.plot([], [], 'bo', markersize=10)

def update(frame):
    idx1 = min(frame * 5, len(x_euler) - 1)
    idx2 = min(frame * 20, len(x_rk4) - 1)
    
    if idx1 > 0:
        line1.set_data(x_euler[:idx1], y_euler[:idx1])
        point1.set_data([x_euler[idx1-1]], [y_euler[idx1-1]])
    if idx2 > 0:
        line2.set_data(x_rk4[:idx2], y_rk4[:idx2])
        point2.set_data([x_rk4[idx2-1]], [y_rk4[idx2-1]])
    
    return line1, point1, line2, point2

max_frames = max(len(x_euler) // 5, len(x_rk4) // 20)
ani = FuncAnimation(fig, update, frames=max_frames, interval=30, blit=True)
ani.save('comparison_animation.gif', writer=PillowWriter(fps=30))
plt.close()

print("\n" + "="*70)
print("COMPARISON COMPLETE!")
print("="*70)
print(f"\nEuler: {len(x_euler)} steps, closest {np.min(r_euler):.3f} Rs - FAILS")
print(f"RK4:   {len(x_rk4)} steps, closest {np.min(r_vals):.3f} Rs - WORKS")
print("\nOutputs:")
print("  1. comparison_side_by_side.png")
print("  2. comparison_overlay.png")
print("  3. comparison_distance.png")
print("  4. comparison_animation.gif")

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle

M = 1.0
PHOTON_SPHERE_R = 1.5 * M
EVENT_HORIZON_R = 2.0 * M

print("="*70)
print("PHASE 4: PHOTON SPHERE VERIFICATION")
print("="*70)

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

def integrate_photon_orbit(b, M=1.0, r_start=20.0):
    """Integrate using effective potential method"""
    r_vals, phi_vals = [], []
    r, phi, dphi = r_start, -np.pi, 0.005
    dr_sign, fate = -1, 'unknown'
    
    for step in range(100000):
        V_eff = r**2 * (1 - 2*M/r)
        term = r**4 / b**2 - V_eff
        
        if term < 0:
            if len(r_vals) > 100:
                fate = 'escaped' if r > r_start * 0.5 else 'captured'
                break
            dr_sign *= -1
            term = 0
        
        dr_dphi = dr_sign * np.sqrt(term)
        
        if r <= EVENT_HORIZON_R * 1.01:
            fate = 'captured'
            break
        if r > r_start * 0.8 and len(r_vals) > 300 and dr_sign > 0:
            fate = 'escaped'
            break
        if abs(phi) > 20*np.pi:
            fate = 'orbiting'
            break
        
        r_vals.append(r)
        phi_vals.append(phi)
        r += dr_dphi * dphi
        phi += dphi
        
        if abs(dr_dphi) < 0.01 and len(r_vals) > 100:
            dr_sign *= -1
    
    if fate == 'unknown':
        fate = 'captured' if r <= EVENT_HORIZON_R * 1.5 else 'escaped'
    
    r_vals = np.array(r_vals)
    phi_vals = np.array(phi_vals)
    x = r_vals * np.cos(phi_vals)
    y = r_vals * np.sin(phi_vals)
    closest = np.min(r_vals) if len(r_vals) > 0 else r_start
    
    return x, y, fate, closest

# Test multiple impact parameters
impact_params = np.array([3.0, 3.5, 4.0, 4.5, 5.0, 5.1, 5.15, 5.19, 
                          5.21, 5.25, 5.3, 5.5, 6.0, 7.0, 8.0, 10.0])

print(f"\nTesting {len(impact_params)} impact parameters")
print(f"Theory: b_critical = √27 M = {np.sqrt(27)*M:.3f} Rs\n")

trajectories = []
for i, b in enumerate(impact_params):
    print(f"[{i+1:2d}/{len(impact_params)}] b = {b:.2f} Rs ... ", end='', flush=True)
    x, y, fate, closest = integrate_photon_orbit(b, M=M, r_start=20.0)
    trajectories.append({'b': b, 'x': x, 'y': y, 'fate': fate, 'closest': closest})
    print(f"{fate:10s} (closest: {closest:.3f} Rs, points: {len(x)})")

captured = [t for t in trajectories if t['fate'] == 'captured']
escaped = [t for t in trajectories if t['fate'] == 'escaped']
print(f"\nResults: {len(captured)} captured, {len(escaped)} escaped")

# ===== MAIN TRAJECTORY PLOT =====
fig, ax = plt.subplots(figsize=(14, 14))
colors_map = {'captured': '#e74c3c', 'escaped': '#3498db', 'orbiting': '#f39c12'}

for traj in trajectories:
    color = colors_map[traj['fate']]
    ax.plot(traj['x'], traj['y'], color=color, linewidth=2.5, alpha=0.75)
    ax.scatter(traj['x'][0], traj['y'][0], color=color, s=60, 
               edgecolors='black', linewidth=1, zorder=5)

ax.scatter(0, 0, color='black', s=400, zorder=10, edgecolors='white', linewidth=3)
horizon = Circle((0, 0), EVENT_HORIZON_R, color='black', fill=True, alpha=0.2, zorder=1)
ax.add_patch(horizon)
photon_sphere = Circle((0, 0), PHOTON_SPHERE_R, color='orange', fill=False, 
                       linestyle='--', linewidth=4, zorder=2)
ax.add_patch(photon_sphere)

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_aspect('equal')
ax.set_xlabel('x (Schwarzschild radii)', fontsize=15, fontweight='bold')
ax.set_ylabel('y (Schwarzschild radii)', fontsize=15, fontweight='bold')
ax.set_title('Phase 4: Photon Sphere Verification\n' + 
             'Multiple Light Rays - Numerical GR Confirmation',
             fontsize=17, fontweight='bold', pad=20)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#e74c3c', label='Captured'),
    Patch(facecolor='#3498db', label='Escaped'),
    Patch(facecolor='black', label='Black Hole'),
    Patch(facecolor='orange', edgecolor='orange', fill=False, 
          label=f'Photon Sphere ({PHOTON_SPHERE_R} Rs)')
]
ax.legend(handles=legend_elements, fontsize=13, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('phase4_photon_sphere_scan.png', dpi=300, bbox_inches='tight')
plt.close()

# ===== ANALYSIS PLOT =====
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

bs = [t['b'] for t in trajectories]
closest = [t['closest'] for t in trajectories]
fcolors = [colors_map[t['fate']] for t in trajectories]

ax1.scatter(bs, closest, c=fcolors, s=150, edgecolors='black', linewidth=2, alpha=0.8)
ax1.axhline(y=PHOTON_SPHERE_R, color='orange', linestyle='--', linewidth=3, 
            label='Photon Sphere')
ax1.axhline(y=EVENT_HORIZON_R, color='black', linestyle=':', linewidth=2, 
            label='Event Horizon')
ax1.set_xlabel('Impact Parameter b (Rs)', fontsize=13, fontweight='bold')
ax1.set_ylabel('Closest Approach (Rs)', fontsize=13, fontweight='bold')
ax1.set_title('Closest Approach vs Impact Parameter', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

ax2.bar(['Captured', 'Escaped'], [len(captured), len(escaped)], 
        color=['#e74c3c', '#3498db'], edgecolor='black', linewidth=2.5, width=0.5)
ax2.set_ylabel('Number of Rays', fontsize=13, fontweight='bold')
ax2.set_title('Fate Distribution', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3, axis='y')
for i, count in enumerate([len(captured), len(escaped)]):
    if count > 0:
        ax2.text(i, count + 0.2, str(count), ha='center', 
                 fontsize=16, fontweight='bold')

plt.tight_layout()
plt.savefig('phase4_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# ===== ANIMATION =====
print("\nCreating animation...")
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
ax.set_aspect('equal')
ax.set_title('Phase 4: Multiple Photon Trajectories', fontsize=16, fontweight='bold')
ax.set_xlabel('x (Rs)', fontsize=14, fontweight='bold')
ax.set_ylabel('y (Rs)', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

ax.scatter(0, 0, color='black', s=400, zorder=10, edgecolors='white', linewidth=3)
ax.add_patch(Circle((0, 0), EVENT_HORIZON_R, color='black', fill=True, 
                    alpha=0.2, zorder=1))
ax.add_patch(Circle((0, 0), PHOTON_SPHERE_R, color='orange', fill=False, 
                    linestyle='--', linewidth=4, zorder=2))

lines, points = [], []
for traj in trajectories[::2]:
    color = colors_map[traj['fate']]
    line, = ax.plot([], [], color=color, linewidth=2.5, alpha=0.75)
    point, = ax.plot([], [], 'o', color=color, markersize=9, 
                     markeredgecolor='black', markeredgewidth=1.5)
    lines.append(line)
    points.append(point)

max_len = max(len(t['x']) for t in trajectories[::2])

def update(frame):
    for i, traj in enumerate(trajectories[::2]):
        idx = min(frame * 50, len(traj['x']) - 1)
        if idx > 0:
            lines[i].set_data(traj['x'][:idx], traj['y'][:idx])
            points[i].set_data([traj['x'][idx]], [traj['y'][idx]])
    return lines + points

ani = FuncAnimation(fig, update, frames=range(0, max_len // 50 + 1), 
                   interval=40, blit=True)
ani.save('phase4_photon_sphere_animation.gif', writer=PillowWriter(fps=30))
plt.close()

print("\n" + "="*70)
print("PHASE 4 COMPLETE!")
print("="*70)
print(f"\nTheory: b_critical = {np.sqrt(27)*M:.3f} Rs")
print(f"Tested: b = {impact_params.min():.1f} to {impact_params.max():.1f} Rs")
print(f"Captured: {len(captured)}, Escaped: {len(escaped)}")
print("\nOutputs:")
print("  1. phase4_photon_sphere_scan.png")
print("  2. phase4_analysis.png")
print("  3. phase4_photon_sphere_animation.gif")
