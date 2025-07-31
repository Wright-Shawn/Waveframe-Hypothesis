# waveframe_scalar_field_solver.py

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Constants (Planck units unless stated otherwise)
Mpl = 1.0                      # Reduced Planck mass (set to 1 in natural units)
Lambda = 0.3                  # Potential scale (Mpl units)
f = 1.0                       # Decay constant (Mpl units)
Omega_m0 = 0.3                # Present-day matter density
H0_km_s_Mpc = 70.0            # Present-day Hubble in km/s/Mpc
conversion_factor = 7.891e7   # Convert H_natural to km/s/Mpc

# Potential and derivatives
def V(phi):
    return Lambda**4 * (1 - np.cos(phi / f))

def dV_dphi(phi):
    return Lambda**4 * np.sin(phi / f) / f

# Friedmann equation: H^2 = (1/3 Mpl^2)(rho_m + rho_phi)
def Hubble(phi, phidot, a):
    rho_phi = 0.5 * phidot**2 + V(phi)
    rho_m = Omega_m0 * a**-3
    return np.sqrt((rho_phi + rho_m) / (3 * Mpl**2))

# System of equations
def scalar_field_system(t, y):
    phi, phidot, a = y
    H = Hubble(phi, phidot, a)
    dphi_dt = phidot
    dphidot_dt = -3 * H * phidot - dV_dphi(phi)
    da_dt = a * H
    return [dphi_dt, dphidot_dt, da_dt]

# Initial conditions
phi0 = 1.0
phidot0 = 0.0
a0 = 1e-5

# Time span
t_span = (0, 2e4)
y0 = [phi0, phidot0, a0]

# Solve ODE system
sol = solve_ivp(scalar_field_system, t_span, y0, method='RK45', dense_output=True, rtol=1e-8, atol=1e-10)

# Extract results
t = sol.t
phi = sol.y[0]
phidot = sol.y[1]
a = sol.y[2]
z = 1 / a - 1

# Compute H(z) in physical units
H_natural = Hubble(phi, phidot, a)
H_km_s_Mpc = H_natural * conversion_factor

# Sort by redshift descending
sorted_indices = np.argsort(z)[::-1]
z_sorted = z[sorted_indices]
H_sorted = H_km_s_Mpc[sorted_indices]

# Save results
import pandas as pd
df = pd.DataFrame({'z': z_sorted, 'H_km_s_Mpc': H_sorted})
df.to_csv('waveframe_Hz_predictions.csv', index=False)

# Plot
plt.figure(figsize=(8,5))
plt.plot(z_sorted, H_sorted, label='Waveframe H(z)', color='darkorange')
plt.xlabel('Redshift z')
plt.ylabel('H(z) [km/s/Mpc]')
plt.title('Waveframe Model Hubble Prediction')
plt.grid(True)
plt.legend()
plt.gca().invert_xaxis()
plt.savefig('waveframe_Hz_plot.png')
plt.show()
