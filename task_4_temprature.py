def convertToCelsius(celsius : float):
  far= (celsius * 1.8) + 32
  kelvin = celsius +273.15
  return[kelvin, far]

celsius = float(input("enter celsius: "))
print(convertToCelsius(celsius))