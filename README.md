## Waveframe Hypothesis

A cosmological framework proposing that the universe evolves within a large-scale oscillatory structure—“the Waveframe”—driven by a scalar field. Includes code, datasets, comparisons with ΛCDM, and tools for numerical analysis.

---

## About the Model

The Waveframe Hypothesis describes the expansion history of the universe using a dynamical scalar field φ(t) evolving under a periodic potential. This framework posits that the shape of spacetime emerges from a deeper oscillatory structure, replacing the cosmological constant with scalar field dynamics. 

---

## How It Works

The scalar field potential is defined as:

V(ϕ) = Λ⁴ [1 − cos(ϕ / f)]

This scalar field evolves according to a damped Klein-Gordon equation in an expanding background:

ϕ̈ + 3Hϕ̇ + (Λ⁴ / f) sin(ϕ / f) = 0

The Hubble parameter is determined self-consistently via the Friedmann equation:

H² = (1 / 3Mₚ²) [½ ϕ̇² + V(ϕ)]

These coupled equations drive the expansion history and determine the effective equation of state of the universe.

---

## Datasets Used

This analysis uses two main observational datasets:

**Pantheon+ Supernovae Sample**

- Source: Pantheon+ Compilation  
- Number of supernovae: 1701  
- Redshift range: z ∈ [0.01, 2.3]  
- Observable: Distance modulus  
- Use: Fit to theoretical luminosity distance using  
  μ(z) = 5 log₁₀ [ d_L(z) / 1 Mpc ] + 25

**Cosmic Chronometers**

- Source: Moresco et al. (2016), others  
- Number of data points: 9  
- Redshift range: z ∈ [0.1, 2.0]  
- Observable: H(z) from galaxy age differentials  
- Use: Direct comparison via  
  H(z) = ȧ / a

---

## Numerical Methods

- Scalar field potential:  
  V(ϕ) = Λ⁴ [1 − cos(ϕ / f)]

- Friedmann equation:  
  H² = (1 / 3Mₚ²) [½ ϕ̇² + V(ϕ)]

- Field evolution:  
  ϕ̈ + 3Hϕ̇ + (Λ⁴ / f) sin(ϕ / f) = 0

- Redshift mapping:  
  dz/dt = −(1 + z) H(z)

- Likelihood:  
  χ² = Σ [ (Data − Model) / σ ]²

---

## Results

| Parameter | Best-fit Value |
|----------|----------------|
| f        | 0.25 Mₚ        |
| Λ        | 2.0 × 10⁻³ Mₚ  |
| χ²       | 31.6           |
| AIC      | 35.6           |
| BIC      | 36.9           |

---

## Get the Code

All code and data are available in the GitHub repository.

### Repository

**GitHub URL:**  
[https://github.com/Wright_Shawn/waveframe](https://github.com/Wright_Shawn/waveframe)

### Included Files

- `waveframe_model.py` – Scalar field simulation  
- `pantheon_plus.csv` – Supernova dataset  
- `moresco_chronometers.csv` – H(z) dataset  
- `README.md` – Documentation  
- `LICENSE` – MIT License  
- `figures/` – All output plots  
- `manuscript/` – LaTeX draft of paper

### License

MIT License — Free for use, distribution, and modification.

---

## Citations

- Scolnic et al. (2022), Pantheon+ Compilation  
- Moresco et al. (2016), H(z) Chronometers  
- Planck Collaboration (2020), ΛCDM Reference

---

## Figures

Figures are available in the `/figures` directory. Each plot compares Waveframe vs ΛCDM for H(z), μ(z), and residuals.

---

## Limitations and Assumptions

- Assumes a spatially flat universe (Ω_k = 0)  
- Radiation density neglected in late-time fits  
- Scalar field has no interaction with matter or radiation  
- Priors fixed for some parameters (e.g., H₀ = 70 km/s/Mpc)  
- Numerical methods used are grid-based, not MCMC

---

## Planned Future Work

- Incorporate radiation density (Ω_r) for high-redshift fits  
- Perform MCMC analysis for uncertainty quantification  
- Add Planck CMB data for stronger constraints  
- Include BAO, weak lensing, and large-scale structure  
- Connect potential V(ϕ) to quantum field derivation  
- Create modular software packaging (pip-ready)

---

## Appendix

- All derivations and intermediate steps available in manuscript  
- Full solution logs and error analysis in `logs/`  
- Conversion of units: c = 1, ℏ = 1, Mₚ² = 1/(8πG)

---

## Collaboration Invitation

We welcome contributions! Whether you’re a physicist, programmer, or curious explorer, you’re invited to participate.

Ways to help:
- Fork the repo and try new extensions  
- Submit bug reports or open issues  
- Contribute code, docs, or test datasets  
- Reach out via GitHub Discussions or pull requests

---

## Final Summary

The Waveframe Hypothesis presents an alternative cosmological model rooted in scalar field dynamics rather than a cosmological constant. It reproduces key observations with competitive χ² scores and provides a natural mechanism for dynamical dark energy. While simplified, it opens new paths for investigating the shape of spacetime and the forces that govern it.
