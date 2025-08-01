# waveframe_pipeline.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, simps
import pandas as pd
from scipy.interpolate import interp1d

# -------- Constants (Planck Units unless stated) --------
Mpl = 1.0                       # Reduced Planck mass
Lambda = 0.3                   # Potential scale
f = 1.0                        # Decay constant
Omega_m0 = 0.3                 # Matter density
Omega_r0 = 8.5e-5              # Radiation density
H0_km_s_Mpc = 70.0             # Hubble constant today
conversion_factor = H0_km_s_Mpc / 1.0  # Planck H0 = 1 => scaling

# -------- Scalar Field Potential --------
def V(phi):
    return Lambda**4 * (1 - np.cos(phi / f))

def dV_dphi(phi):
    return Lambda**4 * np.sin(phi / f) / f

# -------- Friedmann Equation --------
def Hubble(phi, phidot, a):
    rho_phi = 0.5 * phidot**2 + V(phi)
    rho_m = Omega_m0 * a**-3
    rho_r = Omega_r0 * a**-4
    return np.sqrt((rho_phi + rho_m + rho_r) / (3 * Mpl**2))

# -------- Dynamical System --------
def scalar_field_system(t, y):
    phi, phidot, a = y
    H = Hubble(phi, phidot, a)
    return [phidot, -3 * H * phidot - dV_dphi(phi), a * H]

# -------- Initial Conditions --------
phi0 = 1.0
phidot0 = 0.0
a0 = 1e-8
t_span = (0, 5e4)
y0 = [phi0, phidot0, a0]

# -------- Solve the System --------
sol = solve_ivp(scalar_field_system, t_span, y0, method='RK45',
                rtol=1e-8, atol=1e-10, dense_output=True)

# Extract data
t = sol.t
phi, phidot, a = sol.y
z = 1 / a - 1

# Sort by redshift descending
sorted_idx = np.argsort(z)[::-1]
z = z[sorted_idx]
a = a[sorted_idx]
phi = phi[sorted_idx]
phidot = phidot[sorted_idx]

# H(z) in natural units, then rescale to km/s/Mpc
H_natural = Hubble(phi, phidot, a)
H_physical = H_natural * conversion_factor

# -------- Interpolate & Integrate for D_C(z) --------
z_uniform = np.logspace(-4, np.log10(1500), 1000)
Hz_interp = interp1d(z, H_physical, bounds_error=False, fill_value="extrapolate")
Hz_uniform = Hz_interp(z_uniform)
inv_Hz = 1 / Hz_uniform
Dc = simps(inv_Hz, z_uniform) * 299792.458  # Convert to Mpc

# -------- Compute CMB Shift Parameter --------
R = np.sqrt(Omega_m0) * Dc * H0_km_s_Mpc / 299792.458

# -------- Output Results --------
print(f"✅ Comoving distance to z ≈ 1089: D_C ≈ {Dc:.2f} Mpc")
print(f"✅ CMB Shift Parameter: R ≈ {R:.3f}")

# -------- Save H(z) vs z --------
df = pd.DataFrame({'z': z, 'H_km_s_Mpc': H_physical})
df.sort_values(by='z', ascending=True).to_csv('waveframe_Hz_full.csv', index=False)

# -------- Plot --------
plt.figure(figsize=(8,5))
plt.loglog(z, H_physical, label='Waveframe H(z)', color='orange')
plt.axvline(x=1089, linestyle='--', color='gray', label='CMB Decoupling')
plt.xlabel('Redshift z')
plt.ylabel('H(z) [km/s/Mpc]')
plt.title('Hubble Parameter from Waveframe Model')
plt.grid(True, which='both')
plt.legend()
plt.savefig('waveframe_Hz_plot.png')
plt.show()
