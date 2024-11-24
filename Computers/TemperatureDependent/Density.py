import numpy as np
from scipy.interpolate import CubicSpline

def water_density_at_temperature(temperature_c):
    """
    Interpolates water density at a given temperature using cubic spline interpolation.

    Parameters:
        temperature_c (float): Temperature in degrees Celsius (0 <= temperature_c <= 100).

    Returns:
        float: Density of water in kg/m^3 at the specified temperature.
    """
    if not (0 <= temperature_c <= 100):
        raise ValueError("Temperature must be between 0 and 100 degrees Celsius.")
    
    # Empirical data for water density (kg/m^3) from 0°C to 100°C
    temperatures = np.array([0, 4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    densities = np.array([999.84, 999.97, 999.7, 998.2, 995.65, 992.22, 
                          988.04, 983.2, 977.76, 971.8, 965.3, 958.4])

    # Spline interpolation for density
    spline = CubicSpline(temperatures, densities)

    # Interpolated density at the specified temperature
    return spline(temperature_c)

def isopropanol_density_at_temperature(temperature_c):
    """
    Interpolates isopropanol density at a given temperature using cubic spline interpolation.

    Parameters:
        temperature_c (float): Temperature in degrees Celsius (0 <= temperature_c <= 100).

    Returns:
        float: Density of isopropanol in kg/m^3 at the specified temperature.
    """
    if not (0 <= temperature_c <= 100):
        raise ValueError("Temperature must be between 0 and 100 degrees Celsius.")
    
    # Empirical data for isopropanol density (kg/m^3) from 0°C to 100°C
    temperatures = np.array([0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    densities = np.array([804, 803, 795, 786, 777, 767, 758, 748, 737, 727, 716, 704])

    # Spline interpolation for density
    spline = CubicSpline(temperatures, densities)

    # Interpolated density at the specified temperature
    return spline(temperature_c)