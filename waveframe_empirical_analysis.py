
# Waveframe Model Empirical Analysis
# ===================================
# This script performs empirical analysis and visualization of the Waveframe model
# using observational cosmological data such as H(z), fσ₈(z), and scalar field evolution.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps

# Load data
df_waveframe_Hz = pd.read_csv("Waveframe_Model_H_z_.csv")
df_scalar_field = pd.read_csv("Waveframe_Scalar_Field_Evolution_H_z_.csv")
df_shift_R_scan = pd.read_csv("Shift_Parameter_R_Scan_Results.csv")
df_fsig8 = pd.read_csv("updated_fsig8_waveframe.csv")
df_modified_Hz = pd.read_csv("Modified_H_z__Dataset.csv")
df_log_z = pd.read_csv("log_z_array_1_to_10000.csv")

# Plot H(z)
plt.figure()
plt.plot(df_waveframe_Hz['z'], df_waveframe_Hz['H_physical'], label='Waveframe H(z)')
plt.xlabel('Redshift z')
plt.ylabel('H(z) [km/s/Mpc]')
plt.title('Waveframe H(z) vs Redshift')
plt.legend()
plt.grid(True)
plt.savefig("waveframe_Hz_plot.png")

# Plot Scalar Field Evolution
plt.figure()
plt.plot(df_scalar_field['z'], df_scalar_field['phi'], label='phi(z)')
plt.xlabel('Redshift z')
plt.ylabel('Scalar Field φ(z)')
plt.title('Scalar Field Evolution')
plt.legend()
plt.grid(True)
plt.savefig("scalar_field_phi_plot.png")

# Plot fσ₈(z)
plt.figure()
plt.errorbar(df_fsig8['z'], df_fsig8['fsigma8'], yerr=df_fsig8['fsigma8_err'], fmt='o', label='Waveframe fσ₈(z)')
plt.xlabel('Redshift z')
plt.ylabel('fσ₈(z)')
plt.title('Structure Growth: fσ₈(z)')
plt.legend()
plt.grid(True)
plt.savefig("fsig8_plot.png")

# Plot Shift Parameter R Scan
plt.figure()
plt.plot(df_shift_R_scan['Lambda'], df_shift_R_scan['R'], 'o-')
plt.xlabel('Lambda')
plt.ylabel('Shift Parameter R')
plt.title('R vs Lambda Parameter Scan')
plt.grid(True)
plt.savefig("shift_R_scan_plot.png")

print("All plots saved and data loaded.")
