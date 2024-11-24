import numpy as np
import pandas as pd
from pvlib.location import Location
from pvlib.irradiance import get_total_irradiance
from pvlib.solarposition import get_solarposition


# Constants
latitude = 39.9626  # York, PA
longitude = -76.7277
timezone = 'US/Eastern'

# Glass properties
glass_transmittance = 0.9  # Transmissivity of glass (90%)

# Tilt and azimuth of glass (e.g., vertical wall facing south)
tilt = 90  # Vertical
surface_azimuth = 180  # Facing south

# Date and time range
date_range = pd.date_range('2024-11-23 06:00', '2024-11-23 18:00', freq='5min', tz=timezone)

# Location object
location = Location(latitude, longitude, tz=timezone)

# Get solar position
solar_position = get_solarposition(date_range, latitude, longitude)

# Clear sky model to estimate solar irradiance (W/m^2)
clearsky = location.get_clearsky(date_range)
dni = clearsky['dni']
dhi = clearsky['dhi']
ghi = clearsky['ghi']

# Calculate incidence angle modifiers and total solar radiation on glass
results = []
for time, sp in solar_position.iterrows():
    total_irradiance = get_total_irradiance(
        surface_tilt=tilt,
        surface_azimuth=surface_azimuth,
        dni=dni.loc[time],
        ghi=ghi.loc[time],
        dhi=dhi.loc[time],
        solar_zenith=sp['apparent_zenith'],
        solar_azimuth=sp['azimuth']
    )
    # Adjust for glass transmittance
    transmitted_irradiance = total_irradiance['poa_global'] * glass_transmittance
    results.append({'time': time, 'poa_global': total_irradiance['poa_global'], 'transmitted': transmitted_irradiance})

# Convert results to DataFrame
df_results = pd.DataFrame(results)

# Save results to a CSV file or display in console
output_file = "solar_radiation_york_pa.csv"
df_results.to_csv(output_file, index=False)
print(f"Results saved to {output_file}")
