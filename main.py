
import pandas as pd
from Computers.TemperatureDependent.Density import isopropanol_density_at_temperature, water_density_at_temperature
from Computers.TemperatureDependent.HeatCapacity import water_specific_heat_capacity_at_temperature
from Computers.TemperatureDependent.ThermalExpansionCoefficient import water_thermal_expansion_coefficient_at_temperature
from Converters.LengthConverter import LengthConverter
from Getters.getLiquid import get_water, get_isopropanol
from ClassObjects.Liquid import Liquid
from ClassObjects.LiquidType import LiquidType
from Simulation import simulate_temperature
from ClassObjects.SimulationConfig import SimulationConfig
from ClassObjects.Surface import Surface
import matplotlib.pyplot as plt

if __name__ == "__main__":
    liquid = get_water()
    ''' Uncomment to use isopropanol instead '''
    #liquid = get_isopropanol()
    
    '''
    YORK PA:
    latitude=39.9626,
    longitude=-76.7277,
    
    Atacame Desert (IDEAL TEMP RANGES, BUT NO RECORDED TEMP DATA UNFORTUNATELY...):
    latitude=23.8634,
    longitude=69.1328,
    '''

    config = SimulationConfig(
        latitude=39.9626,
        longitude=-76.7277,
        timezone='US/Eastern',
        start_date=pd.to_datetime('2024-7-05 00:00'),
        simulation_time=86400 * 3,  # seconds (default: 1 day)
        simulation_timestep=60,  # seconds
        initial_liquid_temperature=25
    )

    
    east_glass_wall = Surface(
        length=LengthConverter.inch_to_meters(12),               
        width=LengthConverter.inch_to_meters(1),                
        height=LengthConverter.inch_to_meters(24),
        absorption_coefficient=0.06, # How much light is absorbed by the wall.
        transmittance=0.9,        # How much light transmits through.
        reflectance=0.04,         # How much light is reflected.
        orientation="vertical",
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
        orientation="vertical", 
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
        orientation="vertical",
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
        orientation="vertical",
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
        orientation="horizontal",
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
        orientation="horizontal",
        tilt=0,                  # Tilt is 90° for a vertical surface
        azimuth=0                # Azimuth is 90° for east-facing
    )
    
    surfaces = [east_glass_wall, south_glass_wall, west_glass_wall, north_glass_wall, container_top, container_bottom]
    
    volume_liquid = LengthConverter.inch_to_meters(12) * LengthConverter.inch_to_meters(12) * LengthConverter.inch_to_meters(22)
    liquid_mass = volume_liquid * liquid.density_func(config.initial_liquid_temperature)
    print(liquid_mass)
    # Run the simulation
    timeseries, temperature_series, solar_heat_series, environment_temperature_series = simulate_temperature(liquid=liquid, liquid_mass=liquid_mass, surfaces=surfaces, config=config)

    timeseries = timeseries.tz_localize(config.timezone)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(timeseries, solar_heat_series, label='Heat Transfer (W)')
    plt.xlabel('Time')
    plt.ylabel('Total Solar Power (W)')
    plt.title(f'{liquid.liquid_type.name} Total Solar Heat Transfer Over Time')
    plt.legend()
    plt.grid()
    plt.show(block=False)
    
    plt.figure(figsize=(10, 6))
    plt.plot(timeseries, environment_temperature_series, label='Environment Temperature (°C)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Environment Temperature (°C)')
    plt.legend()
    plt.grid()
    plt.show(block=False)
    
    plt.figure(figsize=(10, 6))
    plt.plot(timeseries, temperature_series - 273.15, label='Liquid Temperature (°C)')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title(f'{liquid.liquid_type.name} Temperature Over Time')
    plt.legend()
    plt.grid()
    plt.show(block=True)