1class Solution:
2    def convertTemperature(self, celsius: float) -> List[float]:
3       
4        Kelvin = celsius + 273.15
5        Fahrenheit = celsius * 1.80 + 32.00 
6        return [Kelvin,Fahrenheit]