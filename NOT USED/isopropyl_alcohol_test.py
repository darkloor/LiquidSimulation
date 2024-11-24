import numpy as np
import matplotlib.pyplot as plt
from Converters.LengthConverter import LengthConverter

# Constants for Isopropyl Alcohol
specific_heat_ipa = 2400  # J/(kg*K), specific heat capacity of isopropyl alcohol
density_ipa = 786         # kg/m^3, density of isopropyl alcohol
transmissivity_glass = 0.9  # Fraction of solar radiation passing through glass
absorptivity_ipa = 0.85   # Fraction of solar radiation absorbed by IPA
emissivity_ipa = 0.80     # Emissivity of IPA surface
stefan_boltzmann_const = 5.67e-8  # W/m^2*K^4, Stefan-Boltzmann constant
h_convection = 10         # W/m^2*K, heat transfer coefficient for convection
solar_constant = 1000     # W/m^2, average solar radiation intensity
time_step = 60            # Seconds
simulation_time = 86400 * 1.2  # In seconds, 86400 = 1 day

# Container dimensions
length = LengthConverter.inch_to_meters(6)  # meters
width = LengthConverter.inch_to_meters(6)   # meters
height = LengthConverter.inch_to_meters(24)  # meters

volume_ipa = length * width * height  # Cubic meters
mass_ipa = volume_ipa * density_ipa   # Kilograms

# Surface area calculations
A_top = 0  # Top surface exposed to solar radiation
A_sidewalls = 2 * (length * height) + 2 * (width * height)  # Four vertical walls
surface_area = A_top + A_sidewalls  # Total surface area exposed to environment

# Constants for container walls
thermal_conductivity_wall = 1  # W/(m*K), typical for insulated walls
wall_area = 2 * (length * height + width * height)  # m^2, sidewalls only
wall_thickness = 0.0254  # In meters

# Initialize simulation variables
temperature_ipa = 293  # Initial temperature in Kelvin (20°C)
time_series = np.arange(0, simulation_time, time_step)
temperature_series = []

# Sinusoidal ambient temperature variation
T_avg = 300  # Average ambient temperature in Kelvin (27°C)
T_amplitude = 11  # Amplitude of variation (in Kelvin)
phi = np.pi / 2  # Phase shift to align peak temperature with noon

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
               absorptivity_ipa * surface_area)
    
    # Heat loss by convection and radiation
    q_convection = h_convection * surface_area * (temperature_ipa - T_env)
    q_radiation = emissivity_ipa * stefan_boltzmann_const * surface_area * (
        temperature_ipa**4 - T_env**4)
    
    # Heat loss by conduction through container walls
    q_conductive = (thermal_conductivity_wall * wall_area *
                    (temperature_ipa - T_env) / wall_thickness)
    
    # Net heat energy change
    q_loss = q_convection + q_radiation + q_conductive
    q_net = q_solar - q_loss
    
    # Temperature change
    delta_temp = q_net / (mass_ipa * specific_heat_ipa) * time_step
    temperature_ipa += delta_temp
    temperature_series.append(temperature_ipa)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(time_series / 3600, np.array(temperature_series) - 273.15, label='IPA Temperature (°C)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Isopropyl Alcohol Temperature Over a Day')
plt.legend()
plt.grid()
plt.show()
