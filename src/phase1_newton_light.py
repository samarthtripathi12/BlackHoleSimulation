import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# -------------------------------
# Phase 1: Newtonian Light Bending
# RK4 Integration (Improved Stability)
# -------------------------------

# Constants (Natural units: G = c = 1)
G = 1.0
M = 1.0

# Initial Conditions
x0, y0 = -10.0, 1.0
vx0, vy0 = 1.0, 0.0

dt = 0.01
steps = 3000


# -------------------------------
# Acceleration Function
# -------------------------------
def acceleration(x, y):
    r = np.sqrt(x**2 + y**2)
    ax = -2 * G * M * x / r**3
    ay = -2 * G * M * y / r**3
    return ax, ay


# -------------------------------
# RK4 Integrator
# -------------------------------
def compute_trajectory():
    x, y = x0, y0
    vx, vy = vx0, vy0

    xs, ys = [], []

    for _ in range(steps):
        r = np.sqrt(x**2 + y**2)
        if r < 1.5:
            break

        # k1
        ax1, ay1 = acceleration(x, y)
        k1_vx = ax1 * dt
        k1_vy = ay1 * dt
        k1_x = vx * dt
        k1_y = vy * dt

        # k2
        ax2, ay2 = acceleration(x + 0.5*k1_x, y + 0.5*k1_y)
        k2_vx = ax2 * dt
        k2_vy = ay2 * dt
        k2_x = (vx + 0.5*k1_vx) * dt
        k2_y = (vy + 0.5*k1_vy) * dt

        # k3
        ax3, ay3 = acceleration(x + 0.5*k2_x, y + 0.5*k2_y)
        k3_vx = ax3 * dt
        k3_vy = ay3 * dt
        k3_x = (vx + 0.5*k2_vx) * dt
        k3_y = (vy + 0.5*k2_vy) * dt

        # k4
        ax4, ay4 = acceleration(x + k3_x, y + k3_y)
        k4_vx = ax4 * dt
        k4_vy = ay4 * dt
        k4_x = (vx + k3_vx) * dt
        k4_y = (vy + k3_vy) * dt

        vx += (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx) / 6
        vy += (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy) / 6
        x += (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
        y += (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6

        xs.append(x)
        ys.append(y)

    return np.array(xs), np.array(ys)


# -------------------------------
# Static Plot
# -------------------------------
def make_static_plot(x, y):
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label="Light Ray (RK4)")
    plt.scatter(0, 0, color="black", s=80, label="Central Mass")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Phase 1: Newtonian Light Deflection (RK4)")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)

    plt.savefig("data/phase1_newton_single_ray.png", dpi=300)
    plt.close()


# -------------------------------
# Animation
# -------------------------------
def make_animation(x, y):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-11, 11)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal")
    ax.set_title("Phase 1: Newtonian Light Deflection (RK4)")

    ax.scatter(0, 0, color="black", s=80)

    line, = ax.plot([], [], lw=2)
    point, = ax.plot([], [], "ro")

    def update(frame):
        line.set_data(x[:frame], y[:frame])
        point.set_data(x[frame-1], y[frame-1])
        return line, point

    ani = FuncAnimation(fig, update, frames=len(x), interval=20)
    ani.save("data/phase1_newton_animation.gif", writer=PillowWriter(fps=30))

    plt.close()


# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    x, y = compute_trajectory()
    make_static_plot(x, y)
    make_animation(x, y)
