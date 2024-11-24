import time
import numpy as np
import pandas as pd

from Computers.TimeDependent.TransmittedIrradiance import compute_transmitted_irradiance, compute_transmitted_irradiance_for_day
from Converters.TemperatureConverter import TemperatureConverter
from SimulationConfig import SimulationConfig

# Constants
stefan_boltzmann_const = 5.67e-8  # W/m^2*K^4
h_convection = 10                 # W/m^2*K, convective heat transfer coefficient

def simulate_temperature(liquid, liquid_mass, surfaces, config: SimulationConfig):
    """
    Simulate the temperature of the liquid in the container using transmitted irradiance.
    
    Args:
        liquid (Liquid): The liquid object with thermal properties.
        surfaces (list of Surface): List of surfaces defining the container.
        config (SimulationConfig): Simulation configuration.
    
    Returns:
        tuple: Time series (seconds) and temperature series (Kelvin).
    """
    start = time.time()
    # Precompute irradiance for all surfaces
    irradiance_data = {surface: compute_transmitted_irradiance_for_day(config, surface) for surface in surfaces}
    print(f'Took {time.time() - start} seconds to compute surfaces')
    # Extract simulation parameters
    timeseries = config.date_range
    
    # Initialize simulation variables
    solar_heat_series = [0]
    temperature_series = [TemperatureConverter.c_to_k(config.initial_liquid_temperature)]

    # Sinusoidal ambient temperature variation (example)
    def ambient_temperature(timestamp):
        day_fraction = ((timestamp - config.start_date).total_seconds() % 86400) / 86400
        return 300 + 7.5 * np.sin(2 * np.pi * day_fraction - np.pi / 2)

    # Simulation loop
    for timestamp in timeseries[1:]:
        start = time.time()
        # Convert the last temperature value to a scalar (Kelvin to Celsius conversion)
        T_env = ambient_temperature(timestamp)
        q_solar_total = 0
        
        # Compute transmitted irradiance for each surface
        for surface in surfaces:
            transmitted_irradiance = irradiance_data[surface][timestamp]
            q_solar = transmitted_irradiance * surface.length * surface.height
            q_solar_total += q_solar
        
        # Calculate convection and radiation losses
        surface_area = sum(surface.length * surface.height for surface in surfaces)
        q_convection = h_convection * surface_area * (temperature_series[-1] - T_env)
        q_radiation = (liquid.emissivity *
                       stefan_boltzmann_const *
                       surface_area *
                       (temperature_series[-1]**4 - T_env**4))

        
        # Net heat change
        q_net = q_solar_total - q_convection - q_radiation
        
        delta_temp = q_net / (liquid_mass * liquid.heat_capacity_func(TemperatureConverter.k_to_c(temperature_series[-1]))) * config.simulation_timestep
        
        temperature_series.append(temperature_series[-1] + delta_temp)
        solar_heat_series.append(q_solar_total)
        
        print(f"Total Solar Benefit: {q_solar_total:.2f}")
        print(f"Current Liquid Temperature: {TemperatureConverter.k_to_c(temperature_series[-1]):.2f}")

    return timeseries, np.array(temperature_series), np.array(solar_heat_series)
