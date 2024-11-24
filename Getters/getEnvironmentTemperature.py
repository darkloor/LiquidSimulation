import time
import numpy as np
import pandas as pd

from Computers.TimeDependent.TransmittedIrradiance import compute_transmitted_irradiance, compute_transmitted_irradiance_for_day
from Converters.TemperatureConverter import TemperatureConverter
from ClassObjects.SimulationConfig import SimulationConfig

from datetime import datetime, timedelta
from meteostat import Point, Hourly
import pandas as pd
import pytz

# Retrieve and interpolate temperature data using Meteostat
def get_temperature_data(config: SimulationConfig):
    # Define location using latitude and longitude
    location = Point(config.latitude, config.longitude)

    
    start = config.start_date
    start_naive = start.tz_localize(None)
    end_naive = start_naive + timedelta(seconds=config.simulation_time)

    # Fetch hourly temperature data from Meteostat
    data = Hourly(location, start_naive, end_naive)
    data = data.fetch()
    print(data)
    # Ensure the DataFrame contains a 'temp' column
    if 'temp' not in data:
        raise ValueError("Temperature data not available for the given location and date range.")
    
    # Convert index to datetime and sort
    data.index = pd.to_datetime(data.index)
    data = data.sort_index()

    # Resample to simulation timestep and interpolate
    timestep = f"{config.simulation_timestep}S"  # E.g., '60S' for 60 seconds
    resampled_data = data.resample(timestep).interpolate(method='time')

    return resampled_data

