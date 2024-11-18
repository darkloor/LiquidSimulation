
from LiquidType import LiquidType
from ThermalExpansion import ThermalExpansion


class Liquid:
    def __init__(self, liquid_type: LiquidType, emissivity, heat_capacity_func, density_func, thermal_expansion_coefficient_func):
        """
        Initialize a generic liquid object with thermodynamic and radiative properties.
        
        :param liquid_type: Type of the liquid (e.g., "WATER").
        :param emissivity: Emissivity of the liquid surface.
        
        """
        self.liquid_type = liquid_type
        self.emissivity = emissivity
        self.heat_capacity_func = heat_capacity_func
        self.density_func = density_func
        self.thermal_expansion_coefficient_func = thermal_expansion_coefficient_func
        
    # def get_density(self, temperature_c):
    #     """
    #     Calculate the density of the liquid based on its type and temperature.

    #     :param temperature: Temperature in degrees Celsius.
    #     :return: Density of the liquid in kg/m^3.
    #     """
    #     if not (0 <= temperature_c <= 100):
    #             raise ValueError("Temperature must be between 0°C and 100°C for accurate density calculation.")
            
    #     if self.liquid_type == LiquidType.WATER:
    #         return (999.87 + 0.0679 * temperature_c - 0.0097 * temperature_c**2 +
    #                 0.0001 * temperature_c**3 - 0.000001 * temperature_c**4)
    #     elif self.liquid_type == LiquidType.ISOPROPANOL:
    #         #thermal_expansion_coefficient = 0.001016
    #         return 803.69 - 0.543 * temperature_c
    #     else:
    #         raise ValueError(f"Density calculation is not implemented for this liquid \"{self.liquid_type}\".")
        
        
    # # def heat_transfer_rate(self, volume, temp_change):
    # #     """
    # #     Calculate the heat required to change the temperature of the liquid.
        
    # #     :param volume: Volume of the liquid (m^3).
    # #     :param temp_change: Temperature change (K).
    # #     :return: Heat required (Joules).
    # #     """
    # #     mass = self.density * volume  # Mass (kg)
    # #     return mass * self.specific_heat_capacity * temp_change
    
    # # def solar_heat_gain(self, solar_flux, surface_area, exposure_time):
    # #     """
    # #     Calculate heat gained from solar radiation.
        
    # #     :param solar_flux: Solar energy incident on the surface (W/m^2).
    # #     :param surface_area: Surface area exposed to solar radiation (m^2).
    # #     :param exposure_time: Duration of exposure (seconds).
    # #     :return: Heat gained (Joules).
    # #     """
    # #     return self.absorptivity * solar_flux * surface_area * exposure_time
    
    # # def radiative_loss(self, surface_area, temperature):
    # #     """
    # #     Calculate radiative heat loss from the liquid surface.
        
    # #     :param surface_area: Surface area exposed to radiation (m^2).
    # #     :param temperature: Temperature of the liquid surface (K).
    # #     :return: Radiative loss (W).
    # #     """
    # #     stefan_boltzmann_const = 5.67e-8  # Stefan-Boltzmann constant (W/m^2*K^4)
    # #     return self.emissivity * stefan_boltzmann_const * surface_area * (temperature ** 4)
    
    # # def conduction_heat_transfer(self, thickness, temp_difference, surface_area):
    # #     """
    # #     Estimate heat transfer through conduction.
    # #     :param thickness: Thickness of the layer (m).
    # #     :param temp_difference: Temperature difference across the layer (K).
    # #                             (Positive if heat flows into the liquid, negative if out.)
    # #     :param surface_area: Area for conduction (m^2).
    # #     :return: Heat transfer due to conduction (W).
    # #             (Positive for heat gain, negative for heat loss.)
    # #     """
    # #     if not self.thermal_conductivity:
    # #         raise ValueError("Thermal conductivity is required for this calculation.")
    # #     return (self.thermal_conductivity * surface_area * temp_difference) / thickness

    # def __repr__(self):
    #     return (f"Liquid(name={self.name}, specific_heat_capacity={self.specific_heat_capacity} J/(kg*K), "
    #             f"density={self.density} kg/m^3, absorptivity={self.absorptivity}, "
    #             f"emissivity={self.emissivity})")
