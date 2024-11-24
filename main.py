
import pandas as pd
from Computers.TemperatureDependent.Density import isopropanol_density_at_temperature, water_density_at_temperature
from Computers.TemperatureDependent.HeatCapacity import water_specific_heat_capacity_at_temperature
from Computers.TemperatureDependent.ThermalExpansionCoefficient import water_thermal_expansion_coefficient_at_temperature
from Converters.LengthConverter import LengthConverter
from getLiquid import get_water
from Liquid import Liquid
from LiquidType import LiquidType
from Simulation import simulate_temperature
from SimulationConfig import SimulationConfig
from Surface import Surface
from ThermalExpansion import ThermalExpansion
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # WIP THIS CODE IS NOT AT ALL FINISHED, NO FUNCTIONALITY YET
    liquid = get_water()
    
    config = SimulationConfig(
        latitude=39.9626,
        longitude=-76.7277,
        timezone='US/Eastern',
        start_date=pd.to_datetime('2024-6-23 06:00'),
        simulation_time=86400 * 3,  # seconds (default: 1 day)
        simulation_timestep=60,  # seconds
        initial_liquid_temperature=20
    )
    
    east_glass_wall = Surface(
        length=LengthConverter.inch_to_meters(12),               
        width=LengthConverter.inch_to_meters(1),                
        height=LengthConverter.inch_to_meters(24),
        absorption_coefficient=0.06,  
        transmittance=0.9,        # Absorption, Transmittance, and Reflectance must add to 1
        reflectance=0.04,          
        orientation="vertical",   # Orientation is vertical
        tilt=90,                  # Tilt is 90° for a vertical surface
        azimuth=90                # Azimuth is 90° for east-facing
    )
    
    south_glass_wall = Surface(
        length=LengthConverter.inch_to_meters(12),               
        width=LengthConverter.inch_to_meters(1),                
        height=LengthConverter.inch_to_meters(24),
        absorption_coefficient=0.06,  
        transmittance=0.9,        # Absorption, Transmittance, and Reflectance must add to 1
        reflectance=0.04,          
        orientation="vertical",   # Orientation is vertical
        tilt=90,                  # Tilt is 90° for a vertical surface
        azimuth=180                # Azimuth is 90° for east-facing
    )
    
    west_glass_wall = Surface(
        length=LengthConverter.inch_to_meters(12),               
        width=LengthConverter.inch_to_meters(1),                
        height=LengthConverter.inch_to_meters(24),
        absorption_coefficient=0.06,  
        transmittance=0.9,        # Absorption, Transmittance, and Reflectance must add to 1
        reflectance=0.04,          
        orientation="vertical",   # Orientation is vertical
        tilt=90,                  # Tilt is 90° for a vertical surface
        azimuth=270                # Azimuth is 90° for east-facing
    )
    
    north_glass_wall = Surface(
        length=LengthConverter.inch_to_meters(12),               
        width=LengthConverter.inch_to_meters(1),                
        height=LengthConverter.inch_to_meters(24),
        absorption_coefficient=0.06,  
        transmittance=0.9,        # Absorption, Transmittance, and Reflectance must add to 1
        reflectance=0.04,          
        orientation="vertical",   # Orientation is vertical
        tilt=90,                  # Tilt is 90° for a vertical surface
        azimuth=0                # Azimuth is 90° for east-facing
    )
    
    container_top = Surface(
        length=LengthConverter.inch_to_meters(12),               
        width=LengthConverter.inch_to_meters(1),                
        height=LengthConverter.inch_to_meters(12),
        absorption_coefficient=0.9,  
        transmittance=0,        # Absorption, Transmittance, and Reflectance must add to 1
        reflectance=0.1,          
        orientation="horizontal",   # Orientation is vertical
        tilt=0,                  # Tilt is 90° for a vertical surface
        azimuth=0                # Azimuth is 90° for east-facing
    )
    
    container_bottom = Surface(
        length=LengthConverter.inch_to_meters(12),               
        width=LengthConverter.inch_to_meters(1),                
        height=LengthConverter.inch_to_meters(12),
        absorption_coefficient=0.9,  
        transmittance=0,        # Absorption, Transmittance, and Reflectance must add to 1
        reflectance=0.1,          
        orientation="horizontal",   # Orientation is vertical
        tilt=0,                  # Tilt is 90° for a vertical surface
        azimuth=0                # Azimuth is 90° for east-facing
    )
    
    surfaces = [east_glass_wall, south_glass_wall, west_glass_wall, north_glass_wall, container_top, container_bottom]
    
    volume_liquid = LengthConverter.inch_to_meters(12) * LengthConverter.inch_to_meters(12) * LengthConverter.inch_to_meters(22)
    liquid_mass = volume_liquid * liquid.density_func(config.initial_liquid_temperature)
    print(liquid_mass)
    # Run the simulation
    timeseries, temperature_series, solar_heat_series = simulate_temperature(liquid=liquid, liquid_mass=liquid_mass, surfaces=surfaces, config=config)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(timeseries, temperature_series - 273.15, label='Liquid Temperature (°C)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title(f'{liquid.liquid_type.name} Temperature Over Time')
    plt.legend()
    plt.grid()
    plt.show(block=False)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(timeseries, solar_heat_series, label='Heat Transfer (W)')
    plt.xlabel('Time')
    plt.ylabel('Total Solar Power (W)')
    plt.title(f'{liquid.liquid_type.name} Total Solar Heat Transfer Over Time')
    plt.legend()
    plt.grid()
    plt.show()

    # water = Liquid(
    #     name="water",
    #     specific_heat_capacity=4184,
    #     density=1000,
    #     absorptivity=0.95,
    #     emissivity=0.95,
    #     thermal_expansion=ThermalExpansion(coefficient=0.000207, reference_temperature=20)
    # )
    
    

    
    # isoproponal_thermal_expansion = ThermalExpansion(reference_temp=20, reference_density=785.40)

    # target_temp = 15  # Target temperature in Celsius
    # density_at_target_temp = compute_density_at_temperature(
    #     target_temp,
    #     isoproponal_thermal_expansion.reference_temp,
    #     isoproponal_thermal_expansion.reference_density,
    #     isopropanol_thermal_expansion_coefficient
    # )

    # print(f"Density of LIQUID at {target_temp}°C: {density_at_target_temp:.2f} kg/m^3")
    
    # water_thermal_expansion = ThermalExpansion(reference_temp=20, reference_density=998)

    # target_temp = 66  # Target temperature in Celsius
    # density_at_target_temp = water_density_at_temperature(
    #     target_temp,
    # )

    # print(f"Density of LIQUID at {target_temp}°C: {density_at_target_temp:.2f} kg/m^3")
    
    # target_temp = 36  # Target temperature in Celsius
    # density_at_target_temp = isopropanol_density_at_temperature(
    #     target_temp,
    # )

    # print(f"Density of LIQUID at {target_temp}°C: {density_at_target_temp:.2f} kg/m^3")