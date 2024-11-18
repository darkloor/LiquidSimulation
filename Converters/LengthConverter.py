class LengthConverter:
    """
    A utility class for converting various units of length to meters.
    """
    
    @staticmethod
    def inch_to_meters(inches: float) -> float:
        """
        Convert inches to meters.
        :param inches: Length in inches.
        :return: Length in meters.
        """
        return inches * 0.0254
    
    @staticmethod
    def cm_to_meters(cm: float) -> float:
        """
        Convert centimeters to meters.
        :param cm: Length in centimeters.
        :return: Length in meters.
        """
        return cm / 100.0
    
    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """
        Convert feet to meters.
        :param feet: Length in feet.
        :return: Length in meters.
        """
        return feet * 0.3048
    
    @staticmethod
    def yards_to_meters(yards: float) -> float:
        """
        Convert yards to meters.
        :param yards: Length in yards.
        :return: Length in meters.
        """
        return yards * 0.9144
    
    @staticmethod
    def miles_to_meters(miles: float) -> float:
        """
        Convert miles to meters.
        :param miles: Length in miles.
        :return: Length in meters.
        """
        return miles * 1609.344
    
    @staticmethod
    def mm_to_meters(mm: float) -> float:
        """
        Convert millimeters to meters.
        :param mm: Length in millimeters.
        :return: Length in meters.
        """
        return mm / 1000.0
    
    @staticmethod
    def km_to_meters(km: float) -> float:
        """
        Convert kilometers to meters.
        :param km: Length in kilometers.
        :return: Length in meters.
        """
        return km * 1000.0
