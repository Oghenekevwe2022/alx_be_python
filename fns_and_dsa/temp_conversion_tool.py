# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return(fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:
    try:
        temperature = int(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()


        match unit:
            case "F":
                converted_temperature = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temperature}°C")
            case "C":
                converted_temperature = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temperature}°F")
                
            case _:
                print("Enter temperature in Celsius or Fahrenheit? (C/F)")
        new_temperature = input("Would you like to check another temperature? (Y/N) ").upper()
        if new_temperature != "Y":
            break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")