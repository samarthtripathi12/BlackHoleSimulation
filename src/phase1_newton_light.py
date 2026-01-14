import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# -------------------------------
# Phase 1: Newtonian Light Bending
# Euler Integration (Baseline)
# -------------------------------

# Constants (units: G = c = 1)
G = 1.0
M = 1.0

# Initial conditions
x0, y0 = -10.0, 1.0
vx0, vy0 = 1.0, 0.0

dt = 0.01
steps = 3000


# -------------------------------
# Compute trajectory (Euler)
# -------------------------------
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


# -------------------------------
# Static Plot
# -------------------------------
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

    plt.savefig("data/phase1_newton_static.png", dpi=300)
    plt.close()


# -------------------------------
# Animation
# -------------------------------
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
        line.set_data(x[:frame], y[:frame])
        point.set_data(x[frame-1], y[frame-1])
        return line, point

    ani = FuncAnimation(fig, update, frames=len(x), interval=20)
    ani.save("data/phase1_newton_animation.gif", writer=PillowWriter(fps=30))

    plt.close()


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    x, y = compute_trajectory()
    make_static_plot(x, y)
    make_animation(x, y)

