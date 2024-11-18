import numpy as np
import matplotlib.pyplot as plt
from Converters.LengthConverter import LengthConverter

# Constants
specific_heat_water = 4186  # J/(kg*K), specific heat capacity of water
density_water = 1000        # kg/m^3, density of water
transmissivity_glass = 0.9  # fraction of solar radiation passing through glass
absorptivity_water = 0.95   # fraction of solar radiation absorbed by water
emissivity_water = 0.95     # emissivity of water surface
stefan_boltzmann_const = 5.67e-8  # W/m^2*K^4, Stefan-Boltzmann constant
h_convection = 10           # W/m^2*K, heat transfer coefficient for convection
solar_constant = 1000       # W/m^2, average solar radiation intensity
time_step = 60              # seconds
simulation_time = 86400 * 1.2     # In seconds, 86400 = 1 day

# # Container dimensions
# length = 1.0  # meters
# width = 1.0   # meters
# height = 0.5  # meters

# Container dimensions
length = LengthConverter.inch_to_meters(6)  # meters
width = LengthConverter.inch_to_meters(6)   # meters
height = LengthConverter.inch_to_meters(24)  # meters

volume_water = length * width * height  # cubic meters
mass_water = volume_water * density_water  # kilograms

# Surface area calculations
A_top = 0  # Top surface exposed to solar radiation
A_sidewalls = 2 * (length * height) + 2 * (width * height)  # Four vertical walls
surface_area = A_top + A_sidewalls  # Total surface area exposed to environment

# Constants for container walls
thermal_conductivity_wall = 1  # W/(m*K), typical for insulated walls
wall_area = 2 * (length * height + width * height)  # m^2, sidewalls only
wall_thickness = 0.0254  # in meters

# Initialize simulation variables
temperature_water = 293  # Initial temperature in Kelvin (20°C)
time_series = np.arange(0, simulation_time, time_step)
temperature_series = []

# Sinusoidal ambient temperature variation
T_avg = 300  # Average ambient temperature in Kelvin (27°C)
T_amplitude = 7.5  # Amplitude of variation (in Kelvin)
phi = np.pi / 2  # Phase shift to align peak temperature with noon

# Thermal Mass Properties
specific_heat_concrete = 880  # J/(kg*K), specific heat capacity of concrete
density_concrete = 2400       # kg/m^3, density of concrete

# Thermal mass dimensions (6x6x6 inches converted to meters)
thermal_mass_length = LengthConverter.inch_to_meters(6)
thermal_mass_width = LengthConverter.inch_to_meters(6)
thermal_mass_height = LengthConverter.inch_to_meters(6)

# Volume, mass, and thermal properties of the thermal mass
volume_concrete = (thermal_mass_length *
                   thermal_mass_width * thermal_mass_height)  # m^3
mass_concrete = volume_concrete * density_concrete  # kg

# Increase the size or number of thermal mass blocks
num_blocks = 1  # Number of thermal mass blocks
thermal_mass_total_volume = volume_concrete * num_blocks
mass_concrete_total = mass_concrete * num_blocks

# Initialize the temperature for all thermal mass blocks (average temperature)
thermal_mass_temperature = 293  # Initial temperature in Kelvin (20°C)

def ambient_temperature(t):
    day_fraction = (t % 86400) / 86400  # Fraction of the day
    return T_avg + T_amplitude * np.sin(2 * np.pi * day_fraction - phi)

# Solar radiation as a function of time (sinusoidal approximation)
def solar_radiation(t):
    day_fraction = (t % 86400) / 86400  # Fraction of the day
    if 0.25 <= day_fraction <= 0.75:  # Sunlight hours (6 AM to 6 PM)
        return solar_constant * np.sin((day_fraction - 0.25) * np.pi / 0.5)
    return 0

for t in time_series:
    T_env = ambient_temperature(t)
    # Solar heat gain
    q_solar = (solar_radiation(t) * transmissivity_glass *
               absorptivity_water * surface_area)
    
    # Heat loss by convection and radiation
    q_convection = h_convection * surface_area * (temperature_water - T_env)
    q_radiation = emissivity_water * stefan_boltzmann_const * surface_area * (
        temperature_water**4 - T_env**4)
    
    # Heat loss by conduction through container walls
    q_conductive = (thermal_conductivity_wall * wall_area *
                    (temperature_water - T_env) / wall_thickness)
    
    # Heat exchange between water and all thermal mass blocks
    delta_T_thermal_mass = temperature_water - thermal_mass_temperature
    q_water_to_mass = (delta_T_thermal_mass * mass_concrete_total *
                       specific_heat_concrete) / time_step
    
    # Adjust temperatures of water and thermal mass
    q_net_water = q_solar - (q_convection + q_radiation + q_conductive + q_water_to_mass)
    delta_temp_water = q_net_water / (mass_water * specific_heat_water) * time_step
    temperature_water += delta_temp_water
    
    delta_temp_mass = q_water_to_mass / (mass_concrete_total * specific_heat_concrete) * time_step
    thermal_mass_temperature += delta_temp_mass
    
    # Store results
    temperature_series.append(temperature_water)


# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time_series / 3600, np.array(temperature_series) - 273.15, label='Water Temperature (°C)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Water Temperature Over a Day')
plt.legend()
plt.grid()
plt.show()


# time_series_hours = time_series / 3600  # Convert time to hours
# T_env_series = [ambient_temperature(t) - 273.15 for t in time_series]  # Convert to °C

# plt.figure(figsize=(10, 6))
# plt.plot(time_series_hours, T_env_series, label='Ambient Temperature (°C)')
# plt.xlabel('Time (hours)')
# plt.ylabel('Ambient Temperature (°C)')
# plt.title('Day-Night Ambient Temperature Variation')
# plt.grid()
# plt.legend()
# plt.show()
