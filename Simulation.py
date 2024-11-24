import time
import numpy as np
import pandas as pd

from Computers.TimeDependent.TransmittedIrradiance import compute_transmitted_irradiance, compute_transmitted_irradiance_for_day
from Converters.TemperatureConverter import TemperatureConverter
from ClassObjects.SimulationConfig import SimulationConfig
from Getters.getEnvironmentTemperature import get_temperature_data

# Constants
stefan_boltzmann_const = 5.67e-8  # W/m^2*K^4
h_convection = 12                 # W/m^2*K, convective heat transfer coefficient

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
    
    start = time.time()
    # Get the temperature data
    temp_data = get_temperature_data(config)
    print(f'Took {time.time() - start} seconds to get temperature data')
    
    print(temp_data)
    
    # Extract simulation parameters
    timeseries = config.date_range
    
    # MAKING TIMESERIES NAIVE TO MATCH TEMPERATURE DATA
    timeseries = timeseries.tz_localize(None)

    
    # Initialize simulation variables
    solar_heat_series = [0]
    liquid_temperature_series = [TemperatureConverter.c_to_k(config.initial_liquid_temperature)]
    environment_temperature_series = [temp_data.loc[timeseries[0], 'temp']]
    
    # Simulation loop
    for timestamp in timeseries[1:]:
        #print(timestamp)
        data_val = temp_data.loc[timestamp, 'temp']
        #print(data_val)
        
        T_env = TemperatureConverter.c_to_k(data_val)

        # print(T_env)
        # input()
        q_solar_total = 0
        
        # Compute transmitted irradiance for each surface
        for surface in surfaces:
            transmitted_irradiance = irradiance_data[surface][timestamp]
            q_solar = transmitted_irradiance * surface.length * surface.height
            q_solar_total += q_solar
        
        # Calculate convection and radiation losses
        surface_area = sum(surface.length * surface.height for surface in surfaces)
        q_convection = h_convection * surface_area * (liquid_temperature_series[-1] - T_env)
        q_radiation = (liquid.emissivity *
                       stefan_boltzmann_const *
                       surface_area *
                       (liquid_temperature_series[-1]**4 - T_env**4))

        
        # Net heat change
        q_net = q_solar_total - q_convection - q_radiation
        
        delta_temp = q_net / (liquid_mass * liquid.heat_capacity_func(TemperatureConverter.k_to_c(liquid_temperature_series[-1]))) * config.simulation_timestep
        
        liquid_temperature_series.append(liquid_temperature_series[-1] + delta_temp)
        solar_heat_series.append(q_solar_total)
        environment_temperature_series.append(TemperatureConverter.k_to_c(T_env))
                
        print(f"Total Solar Benefit: {q_solar_total:.2f}")
        print(f"Current Liquid Temperature: {TemperatureConverter.k_to_c(liquid_temperature_series[-1]):.2f}")

    return timeseries, np.array(liquid_temperature_series), np.array(solar_heat_series), np.array(environment_temperature_series)
