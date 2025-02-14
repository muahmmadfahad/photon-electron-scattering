# Python script to calculate photon energy after scattering
from math import cos, radians

def calculate_photon_energy(E, gamma, gamma_prime, v, v_prime, theta_phi, theta_prime_phi_prime):
    term1 = gamma / gamma_prime
    term2 = (1 - (v / 3e8) * cos(radians(theta_phi))) / (1 - (v_prime / 3e8) * cos(radians(theta_prime_phi_prime)))
    return E * term1 * term2

# Example usage
E_initial = 5e-16  # Initial photon energy in Joules
gamma = 10         # Lorentz factor before scattering
gamma_prime = 9    # Lorentz factor after scattering
v = 2.5e8          # Electron velocity before scattering (m/s)
v_prime = 2.4e8    # Electron velocity after scattering (m/s)
theta_phi = 30     # Scattering angle before interaction (degrees)
theta_prime_phi_prime = 45  # Scattering angle after interaction (degrees)

E_final = calculate_photon_energy(E_initial, gamma, gamma_prime, v, v_prime, theta_phi, theta_prime_phi_prime)
print("Final Photon Energy:", E_final)