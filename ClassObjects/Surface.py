class Surface:
    def __init__(self, length, width, height, absorption_coefficient=0.1, transmittance=0.9, reflectance=0.0, orientation="horizontal", tilt=0, azimuth=180):
        """
        Initialize the Surface object with its physical and material properties.
        
        Parameters:
        - length (float): Length of the surface in meters.
        - width (float): Width of the surface in meters.
        - height (float): Height in meters. Default is 0.
        - absorption_coefficient (float): Fraction of energy absorbed by the surface. Default is 0.1 (10%).
        - transmittance (float): Fraction of energy transmitted through the surface. Default is 0.9 (90%).
        - reflectance (float): Fraction of energy reflected by the surface. Default is 0.0 (no reflection).
        - orientation (str): Orientation of the surface ("horizontal", "vertical", "custom"). Default is "horizontal".
        - tilt (float): Tilt angle of the surface in degrees (0 = flat, 90 = vertical). Default is 0.
        - azimuth (float): Azimuth angle of the surface in degrees (e.g., 180 = south). Default is 180.
        """
        self.length = length
        self.width = width
        self.height = height
        self.absorption_coefficient = absorption_coefficient
        self.transmittance = transmittance
        self.reflectance = reflectance
        self.orientation = orientation
        self.tilt = tilt
        self.azimuth = azimuth
    
    @property
    def area(self):
        """Calculate the surface area in square meters."""
        return self.length * self.width
    
    @property
    def volume(self):
        """Calculate the volume (for 3D surfaces) in cubic meters."""
        return self.length * self.width * self.height
    
    def effective_irradiance(self, incident_irradiance):
        """
        Calculate the effective irradiance absorbed or transmitted through the surface.
        
        Parameters:
        - incident_irradiance (float): Irradiance (W/m^2) incident on the surface.
        
        Returns:
        - dict: A dictionary containing:
            - absorbed (float): Irradiance absorbed by the surface (W/m^2).
            - transmitted (float): Irradiance transmitted through the surface (W/m^2).
            - reflected (float): Irradiance reflected by the surface (W/m^2).
        """
        absorbed = incident_irradiance * self.absorption_coefficient
        transmitted = incident_irradiance * self.transmittance
        reflected = incident_irradiance * self.reflectance
        return {
            "absorbed": absorbed,
            "transmitted": transmitted,
            "reflected": reflected
        }

    def describe(self):
        """Provide a summary of the surface's properties."""
        description = (
            f"Surface Properties:\n"
            f"Dimensions: {self.length}m x {self.width}m x {self.height}m\n"
            f"Area: {self.area:.2f} m^2\n"
            f"Volume: {self.volume:.2f} m^3\n"
            f"Absorption Coefficient: {self.absorption_coefficient}\n"
            f"Transmittance: {self.transmittance}\n"
            f"Reflectance: {self.reflectance}\n"
            f"Orientation: {self.orientation}\n"
            f"Tilt: {self.tilt}°\n"
            f"Azimuth: {self.azimuth}°\n"
        )
        return description