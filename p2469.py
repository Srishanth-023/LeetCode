class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        temp_conversions = []

        kelvin = celsius + 273.15
        fahrenheit = (celsius * (9.0 / 5.0)) + 32

        temp_conversions.append(kelvin)
        temp_conversions.append(fahrenheit)

        return temp_conversions