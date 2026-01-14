import numpy as np

def newtonian_test():
    x, y = -10.0, 1.0
    dx, dy = 0.1, 0.0
    dt = 0.01
    r_min = 10

    for _ in range(2000):
        r = np.sqrt(x**2 + y**2)
        if r < r_min:
            r_min = r
        ax = -2 * x / r**3
        ay = -2 * y / r**3
        dx += ax * dt
        dy += ay * dt
        x += dx * dt
        y += dy * dt
        if r < 1.5:
            break
    print("Phase 1 - Newtonian min approach distance:", r_min)


def schwarzschild_test():
    x, y = -10.0, 1.0
    dx, dy = 0.1, 0.0
    dt = 0.01
    r_min = 10

    # Schwarzschild bending (simplified for demo)
    for _ in range(2000):
        r = np.sqrt(x**2 + y**2)
        if r < r_min:
            r_min = r
        # stronger GR-like bending
        ax = -2.5 * x / r**3
        ay = -2.5 * y / r**3
        dx += ax * dt
        dy += ay * dt
        x += dx * dt
        y += dy * dt
        if r < 1.8:
            break
    print("Phase 2 - Schwarzschild min approach distance:", r_min)


def kerr_test():
    x, y = -10.0, 1.0
    dx, dy = 0.1, 0.0
    a = 0.7  # Kerr spin parameter
    dt = 0.01
    r_min = 10

    for _ in range(2000):
        r = np.sqrt(x**2 + y**2)
        if r < r_min:
            r_min = r
        # Kerr bending, slightly asymmetric
        ax = -2.5 * x / r**3 + 0.3 * a * y / r**3
        ay = -2.5 * y / r**3 - 0.3 * a * x / r**3
        dx += ax * dt
        dy += ay * dt
        x += dx * dt
        y += dy * dt
        if r < 1.9:
            break
    print("Phase 3 - Kerr min approach distance:", r_min)


# Run all tests
newtonian_test()
schwarzschild_test()
kerr_test()
