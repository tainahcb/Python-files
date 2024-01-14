"""
Author: Tainah Correia Barreto
Project 07: Windchill Calculator
"""

def calculate_wind_chill(temperature, wind_speed):
    """
    Calculates the wind temperature index.

    Parameters:
    temperature (float): The temperature in degrees Fahrenheit.
    wind_speed (float): The wind speed in miles per hour.

    Returns:
    float: The wind temperature index in degrees Fahrenheit, rounded to two decimal places.
    """
    wind_speed_squared = wind_speed ** 2
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed_squared ** 0.16 + 0.4275 * temperature * wind_speed_squared ** 0.16
    return round(wind_chill, 2)

def convert_celsius_to_fahrenheit(celsius):
    """
    Converts the temperature from degrees Celsius to degrees Fahrenheit.

    Parameters:
    celsius (float): The temperature in degrees Celsius.

    Returns:
    float: The temperature in degrees Fahrenheit, rounded to two decimal places.
    """
    return round((celsius * (9/5)) + 32, 2)

def calculate_and_display_wind_chill():
    """
    Asks the user for the temperature and wind speed, calculates the wind temperature index for various wind speeds and displays the results.
    """
    temperature = float(input("What is the temperature? "))
    temperature_unit = input("Fahrenheit or Celsius (F/C)? ").upper()

    if temperature_unit == "C":
        temperature = convert_celsius_to_fahrenheit(temperature)

    print(f"At temperature {temperature}F, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temperature, 5)}F")
    print(f"At temperature {temperature}F, and wind speed 10 mph, the windchill is: {calculate_wind_chill(temperature, 10)}F")
    print(f"At temperature {temperature}F, and wind speed 15 mph, the windchill is: {calculate_wind_chill(temperature, 15)}F")
    print(f"At temperature {temperature}F, and wind speed 20 mph, the windchill is: {calculate_wind_chill(temperature, 20)}F")
    print(f"At temperature {temperature}F, and wind speed 25 mph, the windchill is: {calculate_wind_chill(temperature, 25)}F")
    print(f"At temperature {temperature}F, and wind speed 30 mph, the windchill is: {calculate_wind_chill(temperature, 30)}F")
    print(f"At temperature {temperature}F, and wind speed 35 mph, the windchill is: {calculate_wind_chill(temperature, 35)}F")
    print(f"At temperature {temperature}F, and wind speed 40 mph, the windchill is: {calculate_wind_chill(temperature, 40)}F")
    print(f"At temperature {temperature}F, and wind speed 45 mph, the windchill is: {calculate_wind_chill(temperature, 45)}F")
    print(f"At temperature {temperature}F, and wind speed 50 mph, the windchill is: {calculate_wind_chill(temperature, 50)}F")
    print(f"At temperature {temperature}F, and wind speed 55 mph, the windchill is: {calculate_wind_chill(temperature, 55)}F")
    print(f"At temperature {temperature}F, and wind speed 60 mph, the windchill is: {calculate_wind_chill(temperature, 60)}F")

calculate_and_display_wind_chill()