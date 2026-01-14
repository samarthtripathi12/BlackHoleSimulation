Black Hole Light Bending Simulation

Abstract
This project simulates the trajectory of light near a Schwarzschild black hole using Python. It demonstrates the progression from classical Newtonian physics to General Relativity, highlighting both numerical methods and physical insights. The simulations show how light bends under gravity, the limitations of naive numerical methods, and the importance of stable integration.

Phase 1 — Classical Baseline (Newtonian)

Scientific question:
What happens to light if gravity is treated classically?

Implementation:

Newtonian deflection model of a single light ray

RK4 integrator for numerical stability

Static plot and animated trajectory

Limitations:

Does not include General Relativity

No photon sphere or strong-field effects

Code & Outputs:

src/phase1_newton_light.py

data/phase1_newton_single_ray.png (static plot)

data/phase1_newton_animation.gif (animation)

Insights:

Establishes a baseline for light bending

Demonstrates that Newtonian gravity underestimates deflection

Phase 2 — Relativistic Single-Ray (Schwarzschild)

Scientific question:
How does spacetime curvature affect light trajectories?

Implementation:

Schwarzschild photon equations (non-rotating black hole)

Single light ray with RK4 integration

Static plot and animation visualizing light bending near the black hole

Not yet implemented:

Euler comparison

Photon sphere scan

Code & Outputs:

src/phase2_schwarzschild_single_ray.py

data/phase2_schwarzschild_single_ray.png

data/phase2_schwarzschild_animation.gif

Insights:

Correct implementation of General Relativity equations

Demonstrates stronger light bending than the Newtonian baseline

Shows photon trajectory curving sharply near the black hole

Phase 3 — Numerical Failure & Fix (Euler vs RK4)

Scientific question:
Do correct equations guarantee correct numerical results?

Implementation:

Euler integrator (unstable, naive method)

RK4 integrator (accurate and stable method)

Same initial conditions for side-by-side comparison

Visualizations include divergence points, photon sphere, and event horizon

Code & Outputs:

src/phase3_euler_vs_rk4.py

data/phase3_euler_vs_rk4_static1.png (Euler divergence)

data/phase3_euler_vs_rk4_static2.png (RK4 correct trajectory)

data/phase3_euler_vs_rk4_side_by_side.png

data/phase3_euler_vs_rk4.gif (animated RK4 trajectory)

Insights:

Euler method diverges near the black hole, highlighting numerical instability

RK4 remains accurate, emphasizing importance of stable numerical integration

Demonstrates how failure analysis informs correct computational physics

Summary of Project Progression:

Phase 1: Newtonian baseline — minimal bending, establishes expectations

Phase 2: Schwarzschild GR — strong curvature, photon sphere observed

Phase 3: Numerical methods comparison — shows why RK4 is necessary for correct physics

Technologies Used:

Python 3.x

NumPy for numerical computation

Matplotlib for plotting and animation

Key Takeaways:

Light follows null geodesics in curved spacetime

Strong gravitational fields require both correct physics and stable numerical methods

Animations help visualize relativistic effects dynamically

PHASE 4 — PHYSICAL VERIFICATION (PHOTON SPHERE @ 1.5 Rₛ)

Scientific question:
“Can I discover a General Relativity prediction numerically?”

What you implement:

Multiple light rays with varying impact parameters

Detection of which rays are captured vs. which escape

Identification of the critical radius where light forms unstable circular orbits

What you demonstrate:

Photon sphere exists at 1.5 Rₛ around a Schwarzschild black hole

Captured rays (red) vs. escaped rays (blue) are clearly visible

Animation shows real-time bending and capture near the black hole

Fate distribution chart shows counts of captured vs. escaped rays

End-state:
Code:

src/phase2_schwarzschild_photon_sphere.py


Outputs:

data/phase2_photon_sphere_scan.png
data/phase2_photon_sphere_fate_distribution.png
data/phase2_photon_sphere_animation.gif


What this proves:

You did not assume the photon sphere; it is numerically verified

Strong-field behavior of light around a black hole is captured accurately

