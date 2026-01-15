import numpy as np

def euler_step(x, v, a, dt):
    v_new = v + a * dt
    x_new = x + v * dt
    return x_new, v_new

def rk4_step(x, v, a_func, dt):
    k1_v = a_func(x) * dt
    k1_x = v * dt

    k2_v = a_func(x + 0.5 * k1_x) * dt
    k2_x = (v + 0.5 * k1_v) * dt

    k3_v = a_func(x + 0.5 * k2_x) * dt
    k3_x = (v + 0.5 * k2_v) * dt

    k4_v = a_func(x + k3_x) * dt
    k4_x = (v + k3_v) * dt

    v_new = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
    x_new = x + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6

    return x_new, v_new


def test_rk4_more_stable_than_euler():
    """
    Simple harmonic oscillator: x'' = -x
    Known stable system — Euler should diverge, RK4 should not.
    """

    dt = 0.1
    steps = 200

    # Initial conditions
    x_e, v_e = 1.0, 0.0
    x_r, v_r = 1.0, 0.0

    def accel(x):
        return -x

    for _ in range(steps):
        x_e, v_e = euler_step(x_e, v_e, accel(x_e), dt)
        x_r, v_r = rk4_step(x_r, v_r, accel, dt)

    # Euler energy blows up
    energy_euler = x_e**2 + v_e**2
    energy_rk4 = x_r**2 + v_r**2

    assert energy_rk4 < energy_euler

