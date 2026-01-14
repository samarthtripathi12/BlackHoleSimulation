# BlackHoleSimulation
Simulates light near a Schwarzschild black hole using Python
# Black Hole Simulation

## Abstract
This project simulates the trajectory of light near a Schwarzschild black hole using Python. 
It demonstrates computational General Relativity concepts, including null geodesics and photon spheres.

## Development Iterations
- v1.0 : Euler integration (unstable near event horizon)
- v2.0 : RK4 integration (stable, verified against photon sphere)

## Verification
- Photon sphere radius: 1.5 Rs
- Trajectory matches theoretical predictions within <1% error

## Requirements
- Python 3.11+
- NumPy
- Matplotlib
- (Optional) Numba for faster computation

- # Black Hole Simulation — Phase 1

## Phase 1: Newtonian Light Bending

This is the first step in simulating light deflection near a black hole using a **simplified Newtonian model**.

![Light Deflection](data/phase1_newtonian_deflection.png)

- Black dot = black hole  
- Blue line = light ray bending due to gravity  
- Stops near photon sphere (r ≈ 1.5)  

