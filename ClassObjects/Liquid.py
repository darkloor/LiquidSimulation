
from ClassObjects.LiquidType import LiquidType

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