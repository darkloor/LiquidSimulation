class ThermalExpansion:
    """
    A class to calculate and manage thermal expansion properties of a material.
    """

    def __init__(self, reference_temp, reference_density):
        """
        Initializes the ThermalExpansion class with reference temperature and density.
        
        :param reference_temp: Reference temperature in Celsius
        :param reference_density: Reference density at the reference temperature in kg/m³
        """
        self.reference_temp = reference_temp
        self.reference_density = reference_density

    def __repr__(self):
        """
        Returns a string representation of the ThermalExpansion object.
        """
        return (
            f"ThermalExpansion(reference_temp={self.reference_temp}, "
            f"reference_density={self.reference_density})"
        )
