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


Phase 5 — Strong-Field Rotation (Kerr Black Hole) (Optional Extension)
Scientific Question

What changes in light trajectories when spacetime itself rotates?

This phase extends the Schwarzschild (non-rotating) black hole to a rotating Kerr black hole, allowing investigation of frame dragging and rotational asymmetry in photon motion.

Physical Background

In Kerr spacetime:

The black hole has angular momentum.

Spacetime is dragged around the rotating mass (Lense–Thirring effect).

Photon paths depend on whether they move with (prograde) or against (retrograde) the rotation.

Unlike Schwarzschild geometry, light trajectories are no longer symmetric.

What Is Implemented

Simplified Kerr photon equations (equatorial plane)

Single-ray and multi-ray simulations

RK4 numerical integrator

Comparison between:

Prograde vs retrograde motion

Kerr vs Schwarzschild trajectories

Visual Outputs

Saved in data/:

Kerr single-ray trajectory

Shows light bending asymmetrically around a rotating black hole

Event horizon and ergosphere are marked

Prograde vs Retrograde comparison

Prograde rays curve more strongly

Retrograde rays resist bending due to opposite rotation

Kerr vs Schwarzschild comparison

Schwarzschild: symmetric bending

Kerr: skewed, rotation-dependent bending

Multiple photon trajectories

Different impact parameters

Clear separation of paths caused by frame dragging

Animation

Time evolution of photon motion

Frame dragging visible as rotational distortion of trajectories

End State

Code

src/phase5_kerr_light.py


Outputs

data/phase5_kerr_single_ray.png
data/phase5_kerr_comparison.png
data/phase5_kerr_multi_ray.png
data/phase5_kerr_animation.gif

What This Phase Demonstrates

Extension from static to rotating spacetime

Numerical handling of strong-field relativistic effects

Physical understanding of:

Frame dragging

Ergosphere

Rotation-induced asymmetry

Willingness to explore beyond the minimal model

This phase is not required for correctness of the project, but it shows depth, curiosity, and strong conceptual control of General Relativity in a computational setting.

Phase 6 — Testing & Scientific Rigor
Scientific Question

“Are the numerical and physical results produced by this simulation reliable?”

Computational physics is not only about producing visually convincing plots.
It requires verification that numerical methods behave correctly and that physical predictions match known theory.

This phase introduces automated tests to validate both.

What is Tested
1. Numerical Integrators

File:
tests/test_integrators.py

Compares Euler and RK4 integration methods

Uses a simple harmonic oscillator (a system with known behavior)

Demonstrates:

Euler integration accumulates numerical error and diverges

RK4 remains stable for the same timestep

This confirms that differences observed in earlier phases are numerical effects, not plotting artifacts.

2. Physical Prediction: Photon Sphere

File:
tests/test_photon_sphere.py

Computes the effective potential for null geodesics in Schwarzschild spacetime

Locates the radius where the potential is maximized

Verifies that the peak occurs at:

𝑟
=
1.5
 
𝑅
𝑠
r=1.5R
s
	​


within numerical tolerance.

This test independently confirms the photon sphere without hard-coding the theoretical value.

What This Phase Demonstrates

Numerical methods are validated, not assumed

General Relativity predictions are verified numerically

Results shown in Phases 2–4 are physically and computationally consistent

The project follows practices used in real scientific codebases

Outputs

No plots or animations are produced in this phase

Success is defined by:

Correct test logic

Physical consistency

Reproducible validation

Why This Matters

By adding tests, this project goes beyond simulation and visualization.
It demonstrates an understanding that:

Correct physics requires both correct equations and correct numerics.

This phase completes the project as a scientifically sound computational study, not just a visual demonstration.

 Project Status

Phase 1: Newtonian baseline — complete

Phase 2: Schwarzschild light bending — complete

Phase 3: Numerical failure & fix — complete

Phase 4: Photon sphere verification — complete

Phase 5: Kerr / rotation (optional) — complete

Phase 6: Testing & rigor — complete

