import numpy as np
import matplotlib.pyplot as plt

# Define parameters with initial values
thermal_conductivity_init = 200  # Initial thermal conductivity (W/mK)
fin_length_init = 0.01  # Initial length of the fin (m)
base_temperature_init = 100  # Initial base temperature of the fin (°C)
ambient_temperature_init = 25  # Initial ambient temperature (°C)
convective_coefficient_init = 100  # Initial convective heat transfer coefficient (W/m^2K)
fin_thickness_init = 0.001  # Initial thickness of the fin (m)
fin_width_square_init = 0.002  # Initial width of the square pin-fin (m)
fin_width_circular_init = 0.003  # Initial width of the circular pin-fin (m)

# Function to calculate temperature distribution along a fin
def calculate_temperature_distribution(x, fin_width, thermal_conductivity, fin_length, base_temperature, ambient_temperature, convective_coefficient, fin_thickness):
    perimeter = 2 * (fin_width + fin_thickness)  # Perimeter of the fin
    area = fin_width * fin_thickness  # Cross-sectional area of the fin
    m = np.sqrt((convective_coefficient * perimeter) / (thermal_conductivity * area))
    temperature_distribution = base_temperature - (base_temperature - ambient_temperature) * np.exp(-m * x)
    return temperature_distribution

# Define sliders
# Define interactive plot function
def interactive_plot(thermal_conductivity, fin_length, base_temperature, ambient_temperature, convective_coefficient, fin_thickness, fin_width_square, fin_width_circular):
    # Generate array of positions along the fins
    x_values = np.linspace(0, fin_length, 100)

    # Calculate temperature distributions for square and circular pin-fin configurations
    temperature_distribution_square = calculate_temperature_distribution(x_values, fin_width_square, thermal_conductivity, fin_length, base_temperature, ambient_temperature, convective_coefficient, fin_thickness)
    temperature_distribution_circular = calculate_temperature_distribution(x_values, fin_width_circular, thermal_conductivity, fin_length, base_temperature, ambient_temperature, convective_coefficient, fin_thickness)

    # Plot temperature distributions
    plt.plot(x_values, temperature_distribution_square, label='2 mm Square Pin-fin')
    plt.plot(x_values, temperature_distribution_circular, label='3 mm Circular Pin-fin')
    plt.xlabel('Distance along the fin (m)')
    plt.ylabel('Temperature (°C)')
    plt.title('Comparison of Temperature Distribution along Fins')
    plt.legend()
    plt.grid(True)
    plt.show()

interactive_plot(thermal_conductivity_init, fin_length_init, base_temperature_init, ambient_temperature_init, convective_coefficient_init, fin_thickness_init, fin_width_square_init, fin_width_circular_init)