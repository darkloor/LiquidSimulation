import pandas as pd
from Computers.TemperatureDependent.Density import water_density_at_temperature, isopropanol_density_at_temperature
from Computers.TemperatureDependent.HeatCapacity import water_specific_heat_capacity_at_temperature, isopropanol_specific_heat_capacity_at_temperature
from Computers.TemperatureDependent.ThermalExpansionCoefficient import water_thermal_expansion_coefficient_at_temperature, isopropanol_thermal_expansion_coefficient_at_temperature
from ClassObjects.Liquid import Liquid
from ClassObjects.LiquidType import LiquidType


def get_water():
    return Liquid(
        liquid_type=LiquidType.WATER,
        emissivity=0.955, # Basically Constant (0.95 to 0.963 over 0 C to 100 C)
        heat_capacity_func=water_specific_heat_capacity_at_temperature,
        density_func=water_density_at_temperature,
        thermal_expansion_coefficient_func=water_thermal_expansion_coefficient_at_temperature
    )
    
def get_isopropanol():
    return Liquid(
        liquid_type=LiquidType.ISOPROPANOL,
        emissivity=0.965, # Around 0.95-0.98, unknown.
        heat_capacity_func=isopropanol_specific_heat_capacity_at_temperature,
        density_func=isopropanol_density_at_temperature,
        thermal_expansion_coefficient_func=isopropanol_thermal_expansion_coefficient_at_temperature
    )