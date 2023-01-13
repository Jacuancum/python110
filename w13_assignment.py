temperature = float(input('What is the temperature? '))
degree_type = input('Fahrenheit or Celsius (F/C)? ').lower()

def wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215*temperature - 35.75*(wind_speed**0.16) + 0.4275*(wind_speed**0.16)
    return wind_chill

def transfer(temperature):
    transfer = (temperature*9/5) + 32
    return transfer

if degree_type == 'c':
    temperature = transfer(temperature)

wind_speed = 5
for i in range(12):
    print(f'At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill(temperature, wind_speed):.2f}F')
    wind_speed += 5
