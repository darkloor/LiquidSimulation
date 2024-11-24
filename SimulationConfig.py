import pandas as pd

from Converters.TemperatureConverter import TemperatureConverter

class SimulationConfig:
    def __init__(
        self,
        latitude,
        longitude,
        timezone='US/Eastern',
        start_date=pd.to_datetime('2024-11-23 00:00'),
        simulation_time=86400,  # seconds (default: 1 day)
        simulation_timestep=60,  # seconds
        initial_liquid_temperature = 20, # CELCIUS
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.start_date = pd.to_datetime(start_date).tz_localize(timezone)
        self.simulation_time = simulation_time
        self.simulation_timestep = simulation_timestep
        self.initial_liquid_temperature = initial_liquid_temperature

        # Automatically compute the date_range based on start_date and timezone
        self.date_range = pd.date_range(
            start=self.start_date,
            end=self.start_date + pd.Timedelta(seconds=self.simulation_time),
            freq=f'{self.simulation_timestep}S',
            tz=self.timezone
        )

    def __repr__(self):
        return (f"SimulationConfig("
                f"latitude={self.latitude}, "
                f"longitude={self.longitude}, "
                f"timezone='{self.timezone}', "
                f"start_date={self.start_date}, "
                f"simulation_time={self.simulation_time}, "
                f"simulation_timestep={self.simulation_timestep}, "
                f"date_range=[{self.date_range[0]} to {self.date_range[-1]}])"
               )
