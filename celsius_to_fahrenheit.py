# Ask the user for a temperature in Celsius (string input). Convert it to a float, then calculate and print the temperature in Fahrenheit. Conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32

celsius_temp_str = input("Enter the temperature in Celsius: ")
celsius_temp = float(celsius_temp_str)
fahrenheit_temp = (celsius_temp * (9/5)) + 32
print("The temperature in Fahrenheit is:", fahrenheit_temp)