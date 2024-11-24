from ClassObjects.SimulationConfig import SimulationConfig
import pandas as pd
from ClassObjects.Surface import Surface
from pvlib.location import Location
from pvlib.irradiance import get_total_irradiance
from pvlib.solarposition import get_solarposition

def compute_transmitted_irradiance(config: SimulationConfig, timestamp: pd.Timestamp, surface: Surface):
    """
    Compute the transmitted irradiance through the given surface at a specific timestamp.

    Args:
        config (SimulationConfig): Configuration object containing location and simulation parameters.
        timestamp (pd.Timestamp): Specific time for which to calculate the irradiance.
        surface (Surface): Surface object defining the physical and optical properties.

    Returns:
        float: The transmitted irradiance (W/m^2) through the surface at the given time.
    """
    # Validate that the timestamp is within the simulation time range
    if not config.date_range[0] <= timestamp <= config.date_range[-1]:
        raise ValueError("Timestamp is outside the simulation range.")

    # Location object
    location = Location(config.latitude, config.longitude, tz=config.timezone)

    # Get solar position at the given timestamp
    solar_position = get_solarposition(timestamp, config.latitude, config.longitude)

    # Clear sky model to estimate solar irradiance
    clearsky = location.get_clearsky(pd.DatetimeIndex([timestamp]))
    dni = clearsky['dni']
    dhi = clearsky['dhi']
    ghi = clearsky['ghi']

    # Compute total irradiance for the given surface
    total_irradiance = get_total_irradiance(
        surface_tilt=surface.tilt,
        surface_azimuth=surface.azimuth,
        dni=dni,
        ghi=ghi,
        dhi=dhi,
        solar_zenith=solar_position['apparent_zenith'],
        solar_azimuth=solar_position['azimuth']
    )

    # Calculate transmitted irradiance
    transmitted_irradiance = total_irradiance['poa_global'] * surface.transmittance
    return transmitted_irradiance.iloc[0]

def compute_transmitted_irradiance_for_day(config: SimulationConfig, surface: Surface):
    """
    Precompute the transmitted irradiance through the given surface for all timestamps in the simulation.

    Args:
        config (SimulationConfig): Configuration object containing location and simulation parameters.
        surface (Surface): Surface object defining the physical and optical properties.

    Returns:
        pd.Series: Transmitted irradiance (W/m^2) indexed by timestamps.
    """
    # Location object
    location = Location(config.latitude, config.longitude, tz=config.timezone)

    # Get solar positions for all timestamps
    solar_position = get_solarposition(config.date_range, config.latitude, config.longitude)

    # Clear sky model to estimate solar irradiance
    clearsky = location.get_clearsky(config.date_range)

    dni = clearsky['dni']
    dhi = clearsky['dhi']
    ghi = clearsky['ghi']

    # Compute total irradiance for the given surface for all timestamps
    total_irradiance = get_total_irradiance(
        surface_tilt=surface.tilt,
        surface_azimuth=surface.azimuth,
        dni=dni,
        ghi=ghi,
        dhi=dhi,
        solar_zenith=solar_position['apparent_zenith'],
        solar_azimuth=solar_position['azimuth']
    )

    # Calculate transmitted irradiance for all timestamps
    transmitted_irradiance = total_irradiance['poa_global'] * surface.transmittance

    return transmitted_irradiance
