import numpy as np
from scipy.interpolate import interp1d

# Table of specific heat capacity (c) data in J/(g·°C) for water at different temperatures
# Temperature in °C
water_temperatures = isopropanol_temperatures = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])
# Specific heat capacities in J/(kg·°C)
water_specific_heats = np.array([4217, 4192, 4182, 4178, 4179, 4181, 4185, 4190, 4196, 4205, 4216, 4228, 4244, 4258, 4282, 4307])
water_interpolation_function = interp1d(water_temperatures, water_specific_heats, kind='cubic')

''' NOTE TEMPS 110 to 150 were LINEARLY INTERPOLATED. 0 to 100 is the REAL DATA.'''
isopropanol_specific_heats = np.array([
    2301.88, 2411.60, 2521.31, 2626.87, 2732.68, 
    2838.50, 2944.31, 3050.13, 3155.94, 3261.76, 
    3367.57, 3473.39, 3579.20, 3685.02, 3790.83, 3896.65
])
# Create an interpolation function for isopropanol
isopropanol_interpolation_function = interp1d(isopropanol_temperatures, isopropanol_specific_heats, kind='cubic')

def water_specific_heat_capacity_at_temperature(temp):
    """
    Computes the specific heat capacity of water at a given temperature using interpolation.
    
    Parameters:
        temp (float): The temperature in °C (between 0 and 150).
        
    Returns:
        float: The specific heat capacity in J/(g·°C).
    """
    if temp < 0 or temp > 150:
        raise ValueError("Temperature must be between 0 and 150 °C.")
    return water_interpolation_function(temp)

def isopropanol_specific_heat_capacity_at_temperature(temp):
    """
    Computes the specific heat capacity of isopropanol at a given temperature using interpolation.
    
    Parameters:
        temp (float): The temperature in °C (between 0 and 100).
        
    Returns:
        float: The specific heat capacity in J/(kg·°C).
    """
    if temp < 0 or temp > 100:
        raise ValueError("Temperature must be between 0 and 100 °C.")
    return isopropanol_interpolation_function(temp)
