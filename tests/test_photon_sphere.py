import numpy as np

def photon_effective_potential(r, M=1.0):
    """
    Effective potential for null geodesics in Schwarzschild spacetime
    V_eff = (1 - 2M/r) / r^2
    """
    return (1 - 2*M/r) / r**2


def test_photon_sphere_radius():
    """
    The photon sphere occurs at the maximum of V_eff
    Expected at r = 1.5 Rs (with Rs = 2M)
    """

    M = 1.0
    r_vals = np.linspace(2.1, 10, 5000)
    V_vals = photon_effective_potential(r_vals, M)

    r_peak = r_vals[np.argmax(V_vals)]

    assert np.isclose(r_peak, 1.5 * M, atol=0.05)

