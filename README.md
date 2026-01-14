Black Hole Light Bending Simulation
Phase 1: Newtonian Light Bending

Description:

Simulates light bending using Newtonian gravity.

Light path is nearly straight, curving slightly near the black hole.

Serves as a baseline for comparison with full General Relativity.

Methods:

Euler integration to compute trajectory (sufficient here due to weak bending).

Generated both a static plot and an animation showing the light path.

Outputs:

Static Plot: phase1_newtonian_deflection.png

Animation: phase1_newtonian_animation.gif

Key Observations:

Closest approach: ~(-1, 1)

Light bends slightly, confirming weak gravitational deflection.

Sets up intuition for stronger effects in Phase 2 (Schwarzschild).

Real-World Relevance:

Illustrates weak gravitational lensing used in astrophysics.

Helps understand how light interacts with mass before considering relativistic effects.

Phase 2: Schwarzschild Light Bending (General Relativity)

Description:

Simulates light bending using the Schwarzschild metric (non-rotating black hole).

Light curves sharply as it approaches the black hole.

Includes Euler method (failure demonstration) and RK4 integration (accurate solution).

Methods:

Euler Method: Demonstrates instability near strong gravity (trajectory diverges).

RK4 Integration: Solves the null geodesic equation accurately, showing correct General Relativity bending.

Verified the photon sphere at 1.5 Schwarzschild radii, an unstable circular orbit for light.

Outputs:

Euler (failed) Static Plot: phase2_schwarzschild_euler.png

Euler Animation: phase2_schwarzschild_euler.gif

RK4 (correct) Static Plot: phase2_schwarzschild_rk4.png

RK4 Animation: phase2_schwarzschild_rk4.gif

Key Observations:

Closest approach: ~(-2, 1.8)

Light bends dramatically due to strong curvature.

Euler fails near black hole → shows importance of stable numerical methods.

RK4 successfully captures photon sphere behavior and correct GR trajectory.

Failures & Learning:

Euler method demonstrates numerical instability, a common challenge in computational physics.

RK4 solution shows the importance of robust numerical methods for high-curvature regimes.

Real-World Relevance:

Directly relates to gravitational lensing, used in astronomy to detect dark matter and distant galaxies.

Helps visualize light paths near black holes, important for understanding LIGO detections and Event Horizon Telescope imaging.
