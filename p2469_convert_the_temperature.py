class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        temperature = []

        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.80) + 32

        temperature.append(kelvin)
        temperature.append(fahrenheit)

        return temperature          # return [kelvin, fahrenheit]