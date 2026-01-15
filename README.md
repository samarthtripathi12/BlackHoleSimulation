Black Hole Light Bending Simulation
Project Description

This project simulates the trajectory of light near black holes using Python, progressively exploring classical Newtonian gravity, Schwarzschild General Relativity, and optionally Kerr (rotating black holes). The simulations use numerical integration to visualize light bending, photon capture, and frame-dragging effects.

The goal is to demonstrate how gravitational physics affects light, show the importance of numerical methods, and verify key predictions of General Relativity. The project combines computational physics, visualization, and theoretical understanding into a coherent workflow.

Why This Project

Provides hands-on experience with General Relativity concepts in a computational setting.

Demonstrates the difference between Newtonian and relativistic predictions of light bending.

Highlights the importance of numerical stability and method selection, such as Euler vs RK4.

Shows how to verify theoretical predictions numerically, like the photon sphere at 1.5 Schwarzschild radii.

Optional Kerr simulations allow exploration of rotating spacetime and frame-dragging, going beyond classical coursework.

Phase 1 — Classical Baseline (Newtonian)

Scientific question:
“What does light do if gravity is treated classically?”

What is implemented:

Newtonian deflection model

One light ray

RK4 integrator

Static plot of trajectory

Animation showing the light bending

What is not claimed:

No General Relativity (GR) effects

No photon sphere

No strong-field behavior

End-state / Files:

Code: src/(phase1_newton_light.py)

Outputs:

![Phase 1: Newtonian](data/phase1_newtonian_deflection.png)  

data/hase1_newtonian_animation.gi

What this phase proves:

Establishes a baseline for light bending under classical gravity.

Shows that Newtonian gravity is insufficient for strong-field effects near a black hole.

Inputs for running:

Initial photon position and velocity (can be modified in code)

Time step and number of steps for RK4 integration

Expected outputs / end result:

A blue light ray bending slightly near a black hole

Black dot representing the black hole at the origin

Animation showing photon moving along a near-straight path with minor deflection

Placement of files:

Code saved in src/

Generated plots and animations saved in data/
