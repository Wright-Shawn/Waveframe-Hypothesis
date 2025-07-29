
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint
from scipy.interpolate import interp1d

# Constants
H0 = 70.0  # Hubble constant in km/s/Mpc
Omega_m = 0.3

# Scale factor range
a_vals = np.logspace(-3, 0, 300)
ln_a_vals = np.log(a_vals)

# Synthetic Waveframe-inspired H(a)
H_waveframe = H0 * np.sqrt(Omega_m * a_vals**-3 + (1 - Omega_m)) * (1 + 0.02 * np.cos(5 * np.log(a_vals)))
ln_H_waveframe = np.log(H_waveframe)
dlnH_dlna_waveframe = np.gradient(ln_H_waveframe, ln_a_vals)
H0_SI = H0 * 1e3 / (3.086e22)
H_waveframe_SI = H_waveframe * 1e3 / (3.086e22)
Omega_m_a_waveframe = Omega_m * (H0_SI / H_waveframe_SI)**2 * a_vals**-3

# Growth factor ODE for Waveframe
def growth_eq_waveframe(ln_a, y):
    D, D_prime = y
    idx = np.searchsorted(ln_a_vals, ln_a)
    idx = np.clip(idx, 0, len(dlnH_dlna_waveframe) - 1)
    dlnH = dlnH_dlna_waveframe[idx]
    omega_m = Omega_m_a_waveframe[idx]
    return [D_prime, -(dlnH + 2) * D_prime + 1.5 * omega_m * D]

# Initial conditions
D0 = a_vals[0]
D_prime0 = D0
sol_waveframe = solve_ivp(
    growth_eq_waveframe,
    (ln_a_vals[0], ln_a_vals[-1]),
    [D0, D_prime0],
    t_eval=ln_a_vals,
    method='RK45',
    rtol=1e-6,
    atol=1e-8
)
D_waveframe = sol_waveframe.y[0]
D_waveframe /= D_waveframe[-1]
z_vals = 1 / np.exp(ln_a_vals) - 1

# LCDM baseline
H_LCDM = H0 * np.sqrt(Omega_m * a_vals**-3 + (1 - Omega_m))
ln_H_LCDM = np.log(H_LCDM)
dlnH_dlna_LCDM = np.gradient(ln_H_LCDM, ln_a_vals)
Omega_m_a_LCDM = Omega_m * (H0 / H_LCDM)**2 * a_vals**-3

def growth_eq_LCDM(y, ln_a):
    D, D_prime = y
    idx = np.searchsorted(ln_a_vals, ln_a)
    idx = np.clip(idx, 0, len(dlnH_dlna_LCDM) - 1)
    dlnH = dlnH_dlna_LCDM[idx]
    omega_m = Omega_m_a_LCDM[idx]
    return [D_prime, -(dlnH + 2) * D_prime + 1.5 * omega_m * D]

sol_LCDM = odeint(growth_eq_LCDM, [a_vals[0], a_vals[0]], ln_a_vals)
D_LCDM = sol_LCDM[:, 0]
D_LCDM /= D_LCDM[-1]

# Interpolate LCDM to match z values
D_LCDM_interp = interp1d(1 / a_vals - 1, D_LCDM, kind='cubic', fill_value="extrapolate")
D_LCDM_at_z = D_LCDM_interp(z_vals)
percent_diff = 100 * (D_waveframe - D_LCDM_at_z) / D_LCDM_at_z

# Plot D(z)
def plot_growth_factors():
    plt.figure(figsize=(8, 5))
    plt.plot(z_vals, D_waveframe, label='Waveframe Model', linewidth=2)
    plt.plot(z_vals, D_LCDM_at_z, '--', label='ΛCDM', linewidth=2)
    plt.xlabel('Redshift z')
    plt.ylabel('Linear Growth Factor D(z)')
    plt.title('Growth Factor D(z) vs Redshift')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Plot percent deviation
def plot_percent_deviation():
    plt.figure(figsize=(8, 5))
    plt.plot(z_vals, percent_diff, color='firebrick', linewidth=2)
    plt.xlabel('Redshift z')
    plt.ylabel('Percent Deviation (%)')
    plt.title('Percent Deviation of D(z): Waveframe vs ΛCDM')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
