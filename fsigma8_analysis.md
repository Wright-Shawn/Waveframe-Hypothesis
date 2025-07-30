# Section: Growth Rate Analysis — fσ₈(z)

## Observable Definition

The observable quantity fσ₈(z) connects cosmic structure growth to redshift-dependent clustering statistics. It is defined as:

 fσ₈(z) = f(z) · σ₈(z)

Where:
- f(z) ≡ dlnD/dlna : logarithmic growth rate
- σ₈(z) = D(z) · σ₈₀ : linear fluctuation amplitude on 8 Mpc/h scales
- σ₈₀ : the present-day normalization, often taken from Planck or marginalized in fits

Hence:

 fσ₈(z) = (dlnD/dlna) · D(z) · σ₈₀

Or equivalently, in terms of redshift:

 fσ₈(z) = [−(1 + z) · dlnD/dz] · D(z) · σ₈₀

## Growth Factor Evolution

The linear growth factor D(z) evolves under the second-order differential equation:

 d²D/d(ln a)² + [dlnH/dln a + 2] · dD/dln a − (3/2) · Ωₘ(a) · D = 0

Where the matter density fraction at scale factor a is given by:

 Ωₘ(a) = [Ωₘ₀ · a⁻³ · H₀²] / H(a)²

## Background Cosmology: Waveframe H(z)

The Hubble rate H(z) is determined dynamically from a real scalar field φ(t) evolving in a periodic potential:

 V(φ) = Λ⁴ · [1 − cos(φ / f)]

The Friedmann equation is:

 H²(t) = (1 / 3Mₚ²) · [½·(φ̇)² + V(φ)]

And the scalar field equation of motion is:

 φ̈ + 3Hφ̇ + dV/dφ = 0

The scale factor is obtained by integrating the definition of H(t):

 ȧ/a = H(t) → a(t) = a₀ · exp( ∫₀ᵗ H(t′) dt′ )

## Numerical Implementation

1. Solve scalar field background:
   - Integrate φ(t), φ̇(t)
   - Compute H(t) → H(a) and z(t)

2. Interpolate H(z) and compute:

 dlnH/dln a = −(1 + z) · dlnH/dz

3. Solve the growth equation with early matter-dominated conditions:

 D(aᵢ) = aᵢ, dD/dln a (aᵢ) = D(aᵢ)

4. Normalize so D(z = 0) = 1, then compute:

 fσ₈(z) = f(z) · D(z) · σ₈₀

## Parameter Choices (Best Fit)

The best-fitting model parameters were obtained by minimizing the χ² deviation from redshift-space distortion (RSD) data:

 f = 0.5 Mₚ, Λ = 0.35 Mₚ (implying Λ⁴ ≈ 0.015 Mₚ⁴), φ₀ = 1.2 Mₚ

## Fit Results

- Waveframe Model: χ²(fσ₈) = 47.0
- Previous Untuned Model: χ²(fσ₈) ≈ 394
- Improvement: Δχ² ≈ −347 (≈88% reduction)

This places the model well within the range of empirical viability when fit solely to growth data.