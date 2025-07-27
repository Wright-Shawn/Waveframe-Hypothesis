
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp, quad
from scipy.interpolate import interp1d

# Constants
H0 = 70.0  # Hubble constant in km/s/Mpc
h = H0 / 100
Mpc_to_km = 3.086e19  # Mpc to km
G = 6.67430e-11  # m^3 kg^-1 s^-2
c = 299792.458  # km/s
M_pl = 2.435e18  # Reduced Planck mass in GeV
M_pl_mks = 2.435e27  # Reduced Planck mass in kg

# Scalar field potential parameters
Lambda = 2.3e-3  # GeV
f = 0.5  # decay constant in Planck units

# Potential and its derivative
def V(phi):
    return Lambda**4 * (1 - np.cos(phi / f))

def dV_dphi(phi):
    return Lambda**4 / f * np.sin(phi / f)

# Friedmann equation to compute H from phi and phi_dot
def Hubble(phi, phi_dot):
    rho_phi = 0.5 * phi_dot**2 + V(phi)
    return np.sqrt(rho_phi / (3 * M_pl**2))

# Scalar field evolution equation
def scalar_field_eom(t, y):
    phi, phi_dot = y
    H = Hubble(phi, phi_dot)
    dphi_dt = phi_dot
    dphidot_dt = -3 * H * phi_dot - dV_dphi(phi)
    return [dphi_dt, dphidot_dt]

# Solve for phi(t)
def solve_scalar_field(phi0, phi_dot0, t_span, t_eval):
    y0 = [phi0, phi_dot0]
    sol = solve_ivp(scalar_field_eom, t_span, y0, t_eval=t_eval, method='Radau')
    return sol.t, sol.y[0], sol.y[1]

# Compute H(z) using redshift mapping
def dz_dt(t, phi, phi_dot):
    H = Hubble(phi, phi_dot)
    return -(1 + t) * H

# Load H(z) data
def load_chronometer_data(filename):
    df = pd.read_csv(filename)
    z = df['z'].values
    Hz = df['Hz'].values
    sigma = df['sigma'].values
    return z, Hz, sigma

# Chi-squared evaluation
def chi_squared(data, model, sigma):
    return np.sum(((data - model) / sigma)**2)

# Load Pantheon data
def load_pantheon_data(filename):
    df = pd.read_csv(filename)
    z = df['z'].values
    mu = df['mu'].values
    sigma = df['sigma'].values
    return z, mu, sigma

# Distance modulus calculation
def luminosity_distance(z, H_func):
    def integrand(zp):
        return 1.0 / H_func(zp)
    integral = np.array([quad(integrand, 0, zi)[0] for zi in z])
    dL = (1 + z) * c * integral
    return 5 * np.log10(dL) + 25
