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

  
# Black Hole Simulation

This repository demonstrates the bending of light near a black hole, progressing from a **simplified Newtonian model** to a **General Relativity (Schwarzschild) simulation**.

---

## Phase 1: Newtonian Light Bending

This first step uses a simplified Newtonian approximation to show how gravity affects light. The light ray bends gradually around the black hole.

![Newtonian Light Deflection](data/phase1_newtonian_deflection.png)

**Key points:**

- Black dot = black hole  
- Blue line = light ray  
- Light travels farther before bending significantly  
- Stops around `r ≈ 1.5` (approximate photon sphere)  
- Curve is gradual and smooth  

---

## Phase 2: Schwarzschild Light Bending (General Relativity)

Now, the simulation uses the Schwarzschild metric from General Relativity. Light bending is stronger and occurs closer to the black hole.

![GR Light Deflection](data/phase2_schwarzschild_deflection.png)

**Key points:**

- Black dot = black hole  
- Blue line = light ray  
- Light bends earlier and more sharply than Newtonian model  
- Stops at Schwarzschild radius `r = 2M`  
- Curve is more pronounced, demonstrating GR effects  

---

## **Comparison Between Phase 1 and Phase 2**

| Feature | Phase 1 (Newtonian) | Phase 2 (GR/Schwarzschild) |
|---------|-------------------|---------------------------|
| Distance before bending | Farther | Closer to black hole |
| Curve shape | Gradual | Sharp, stronger curvature |
| Closest approach | ~(-1, 1) | ~(-2, 1.5-2) |

This shows a clear **progression from basic physics → advanced GR simulation**, demonstrating understanding of **light deflection and photon sphere effects**.

---

## **Next Steps / Phase 3 (Optional)**

- Simulate light bending around a **spinning black hole (Kerr metric)**  
- Demonstrate **frame-dragging effects**  
- Make multi-ray simulations with different impact parameters for comparison  

---

