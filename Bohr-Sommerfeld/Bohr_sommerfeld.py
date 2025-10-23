import numpy as np
import matplotlib.pyplot as plt

# Fine structure constant (dimensionless)
alpha = 1/137.035999

# Rydberg constant energy in eV
Rydberg_E = 13.6

# Function to calculate energy levels using Bohr model
def Bohr_E(n):
    return -Rydberg_E / n**2

# Function to calculate energy levels using Sommerfeld model (relativistic correction)
def Sommerfeld_E(n, k):
    return Bohr_E(n) * ((1 + alpha**2 / n**2) * (n / k - 3/4))

# Range of principal quantum numbers (n = 1 to 6)
n_value = np.arange(1, 7)

# Calculate Bohr energy levels
bohr_energies = [Bohr_E(n) for n in n_value]

# Lists to store Sommerfeld energies and their labels
sommerfeld_energies = []
sommerfeld_labels = []

# Loop over each n and k to calculate Sommerfeld energies
for n in n_value:
    for k in range(1, n + 1):
        sommerfeld_energies.append(Sommerfeld_E(n, k))
        sommerfeld_labels.append(f"n={n}, k={k}")

# Plot setup
plt.figure(figsize=(10, 6))

# Plot Bohr model energy levels
plt.plot(n_value, bohr_energies, 'o-', label='Bohr Model', color='blue')

# Plot Sommerfeld model energy levels as red points
plt.scatter(np.repeat(n_value, n_value), sommerfeld_energies, color='red', label='Sommerfeld Model')

# Draw a horizontal line at 0 eV for reference
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')

# Add title and labels
plt.title("Hydrogen Energy Levels: Bohr vs Sommerfeld Model")
plt.xlabel("Principal Quantum Number n")
plt.ylabel("Energy (eV)")

# Add legend and grid for clarity
plt.legend()
plt.grid(True)

# Show the final plot
plt.show()
