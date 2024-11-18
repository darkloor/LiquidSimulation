class TemperatureConverter:
    """
    A utility class for converting temperatures between Fahrenheit, Celsius, and Kelvin.
    """

    @staticmethod
    def f_to_c(fahrenheit: float) -> float:
        """
        Convert Fahrenheit to Celsius.
        :param fahrenheit: Temperature in Fahrenheit.
        :return: Temperature in Celsius.
        """
        return (fahrenheit - 32) * 5.0 / 9.0

    @staticmethod
    def c_to_f(celsius: float) -> float:
        """
        Convert Celsius to Fahrenheit.
        :param celsius: Temperature in Celsius.
        :return: Temperature in Fahrenheit.
        """
        return (celsius * 9.0 / 5.0) + 32

    @staticmethod
    def f_to_k(fahrenheit: float) -> float:
        """
        Convert Fahrenheit to Kelvin.
        :param fahrenheit: Temperature in Fahrenheit.
        :return: Temperature in Kelvin.
        """
        return (fahrenheit - 32) * 5.0 / 9.0 + 273.15

    @staticmethod
    def k_to_f(kelvin: float) -> float:
        """
        Convert Kelvin to Fahrenheit.
        :param kelvin: Temperature in Kelvin.
        :return: Temperature in Fahrenheit.
        """
        return (kelvin - 273.15) * 9.0 / 5.0 + 32

    @staticmethod
    def c_to_k(celsius: float) -> float:
        """
        Convert Celsius to Kelvin.
        :param celsius: Temperature in Celsius.
        :return: Temperature in Kelvin.
        """
        return celsius + 273.15

    @staticmethod
    def k_to_c(kelvin: float) -> float:
        """
        Convert Kelvin to Celsius.
        :param kelvin: Temperature in Kelvin.
        :return: Temperature in Celsius.
        """
        return kelvin - 273.15
