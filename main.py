
from Computers.Density import isopropanol_density_at_temperature, water_density_at_temperature
from Computers.HeatCapacity import water_specific_heat_capacity_at_temperature
from Computers.ThermalExpansionCoefficient import water_thermal_expansion_coefficient_at_temperature
from Liquid import Liquid
from LiquidType import LiquidType
from ThermalExpansion import ThermalExpansion

if __name__ == "__main__":
    # WIP THIS CODE IS NOT AT ALL FINISHED, NO FUNCTIONALITY YET
    water = Liquid(
        liquid_type=LiquidType.WATER,
        emissivity=0.955, # Basically Constant (0.95 to 0.963 over 0 C to 100 C)
        heat_capacity_func=water_specific_heat_capacity_at_temperature,
        density_func=water_density_at_temperature,
        thermal_expansion_coefficient_func=water_thermal_expansion_coefficient_at_temperature
    )
    
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
    
    water_thermal_expansion = ThermalExpansion(reference_temp=20, reference_density=998)

    target_temp = 66  # Target temperature in Celsius
    density_at_target_temp = water_density_at_temperature(
        target_temp,
    )

    print(f"Density of LIQUID at {target_temp}°C: {density_at_target_temp:.2f} kg/m^3")
    
    target_temp = 36  # Target temperature in Celsius
    density_at_target_temp = isopropanol_density_at_temperature(
        target_temp,
    )

    print(f"Density of LIQUID at {target_temp}°C: {density_at_target_temp:.2f} kg/m^3")