# The Waveframe Hypothesis  
*A Scalar Field Model of Emergent Cosmic Structure*

---

The Waveframe Hypothesis proposes that cosmic structure, time, and gravity emerge from a dynamical scalar field oscillating in a periodic potential. This model offers an alternative to ΛCDM by treating spacetime evolution as a phase-bound system governed by wave-like dynamics in scalar field space.

This repository contains the full source code, observational datasets, figures, manuscript (LaTeX), and documentation supporting this hypothesis.

---

## 🌌 Project Overview

- A cosmological model based on scalar field dynamics in a cosine potential  
- Self-consistent evolution of the Hubble parameter $begin:math:text$ H(t) $end:math:text$ from the field equation  
- Physical redshift-time integration: $begin:math:text$ \\frac{dz}{dt} = -(1 + z) H(z) $end:math:text$  
- Fit to observational datasets: Pantheon+ supernovae and Moresco cosmic chronometers  
- Likelihood evaluation using chi-squared, AIC, and BIC criteria  
- Comparison with ΛCDM

---

## 📁 Repository Structure

```
waveframe-hypothesis/
├── code/
│   └── waveframe_model.py
├── data/
│   ├── moresco_chronometers.csv
│   └── pantheon_plus.csv
├── figures/
│   └── Hz_vs_z_comparison.png
├── main_final_submission_with_methods.tex
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 📈 Datasets Used

- **Pantheon+ Supernovae Sample**
  - N = 1701 supernovae
  - Redshift range: $begin:math:text$ z \\sim 0.01 $end:math:text$ to $begin:math:text$ z \\sim 2.3 $end:math:text$
  - Distance moduli (μ) and associated uncertainties
- **Moresco et al. (2016) Cosmic Chronometers**
  - N = 9 Hubble parameter measurements
  - Redshift range: $begin:math:text$ z \\sim 0.1 $end:math:text$ to $begin:math:text$ z \\sim 2.0 $end:math:text$
  - Provided as H(z) in km/s/Mpc with uncertainties

---

## 🧮 Numerical Methods

- Scalar field potential:  
  $begin:math:text$ V(\\phi) = \\Lambda^4 \\left[1 - \\cos\\left(\\frac{\\phi}{f}\\right)\\right] $end:math:text$

- Friedmann equation with field evolution:  
  $begin:math:text$ H^2 = \\frac{1}{3M_p^2} \\left[ \\frac{1}{2} \\dot{\\phi}^2 + V(\\phi) \\right] $end:math:text$

- Time evolution:  
  $begin:math:text$ \\ddot{\\phi} + 3H\\dot{\\phi} + \\frac{\\Lambda^4}{f} \\sin\\left(\\frac{\\phi}{f}\\right) = 0 $end:math:text$

- Physical redshift mapping via:  
  $begin:math:text$ \\frac{dz}{dt} = -(1 + z) H(z) $end:math:text$

- Likelihood evaluation using  
  $begin:math:text$ \\chi^2 = \\sum \\left( \\frac{\\text{Data} - \\text{Model}}{\\sigma} \\right)^2 $end:math:text$

---

## 📊 Results Summary

| Parameter   | Best-fit Value |
|-------------|----------------|
| $begin:math:text$ \\Lambda $end:math:text$ | $begin:math:text$ 4.2 \\times 10^{-11} $end:math:text$ |
| $begin:math:text$ f $end:math:text$       | $begin:math:text$ 1.4 $end:math:text$ |
| $begin:math:text$ \\phi_0 $end:math:text$  | $begin:math:text$ 2.1 $end:math:text$ |

| Model        | Chi²  | AIC   | BIC   |
|--------------|-------|-------|-------|
| Waveframe    | 94.7  | 100.7 | 101.9 |
| ΛCDM         | 92.3  | 96.3  | 97.1  |

---

## 📜 Citations

- M. Moresco et al., *JCAP* **05** (2016) 014  
- D. Brout et al., *Astrophys. J.* **938**, 110 (2022)  
- T. Padmanabhan, *Rept. Prog. Phys.* **73**, 046901 (2010)  
- E. Verlinde, *JHEP* **04**, 029 (2011)

---

## 📂 Get the Code

- All code is available in `/code/`
- CSV datasets are in `/data/`
- See `requirements.txt` for dependencies

---

## 📎 License

This project is licensed under the MIT License. You are free to use, modify, and distribute with attribution.

---

## 🤝 Collaboration Invitation

If you're a physicist, developer, data scientist, or just deeply curious, contributions are welcome.

- Submit issues or suggestions
- Fork and experiment with the model
- Reach out with questions or proposals

Contact: **shawnkardin@gmail.com**

---

## 🧠 Limitations and Assumptions

- Radiation component $begin:math:text$ \\Omega_r $end:math:text$ is neglected for simplicity  
- Initial field values are chosen heuristically  
- No MCMC sampling yet; optimization is via local minimization  
- Relies on reduced Planck mass $begin:math:text$ M_p = 1 $end:math:text$ (natural units)  
- Assumes spatial flatness and homogeneous scalar field

---

## 🔭 Planned Future Work

- Include radiation and early-universe constraints  
- Explore field potentials beyond cosine  
- Run full MCMC chains for posterior analysis  
- Extend to include structure growth and CMB comparison  
- Package into pip-installable module

---

## 🔬 Appendix

- Scalar field code runs via `scipy.odeint` or `solve_ivp`  
- All redshift-time transformations are computed numerically  
- Both H(z) and luminosity distance predictions are generated from simulation output  
- Contour plots and figures are available in `/figures`

---

Let me know if you'd like this exported as `README.md` directly or zipped in the GitHub-ready bundle.
```
