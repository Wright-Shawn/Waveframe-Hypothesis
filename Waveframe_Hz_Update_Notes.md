
# Waveframe Cosmology — Updated Expansion History

This update includes a full numerical integration of the Waveframe scalar field cosmology, extending to redshift z ≈ 1500 to support CMB-era diagnostics.

## Included Files
- `waveframe_Hz_full.csv`: Physical Hubble parameter H(z) vs redshift computed using the scalar potential V(φ) = Λ⁴[1 - cos(φ/f)]
- `waveframe_Hz_plot.png`: Log-log plot of the computed H(z) from z ≈ 10⁻⁴ to 1500
- Computed comoving distance to recombination (z ≈ 1089): **26,211.55 Mpc**
- CMB Shift Parameter (R): **3.352**

## Notes
- Parameters: Λ = 0.3 Mₚ, f = 1.0 Mₚ, φ₀ = 1.0, φ̇₀ = 0.0
- Uses Radau scalar field integration and Planck-rescaled units.
- For full model details, see the [main manuscript](./waveframe_manuscript_draft.md) or project README.

## License
Licensed under the MIT License.

---

Built using Python, NumPy, SciPy, Matplotlib, and Pandas.
