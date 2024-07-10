def calculate_wind_chill(temp_f, wind_speed):
    """
    Calculate the wind chill based on the temperature in Fahrenheit and wind speed in mph.
    """
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp_f * (wind_speed ** 0.16)
    return wind_chill

def celsius_to_fahrenheit(temp_c):
    """
    Convert a temperature from Celsius to Fahrenheit.
    """
    return temp_c * (9/5) + 32

def main():
    
    temp = float(input("What is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    
    if scale == 'C':
        temp = celsius_to_fahrenheit(temp)
    
    print(f"At temperature {temp:.1f}F:")
    
    
    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temp, wind_speed)
        print(f"At wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")


if __name__ == "__main__":
    main()