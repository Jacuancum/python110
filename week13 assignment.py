def wind_cill(t,v):
    wind_cill = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
    return wind_cill 

def change_tp(t):
    change_tp = (t*9/5)+32
    return change_tp

temperature = float(input("What is the temperature?"))
unit = input("Fahrenheit or Celsius (F/C)?")

if unit == "C":
    temperature = change_tp(temperature)

speed=5
for i in range(12):
    print(f"At temperature {temperature} F, and wind speed {speed}mph, the windchill is: {wind_cill(temperature,speed):.2f}F")
    speed+=5
    
    

    