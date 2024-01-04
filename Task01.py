def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def print_conversion_result(value, from_unit, to_unit, result):
    print(f"{value} {from_unit.capitalize()} is approximately {result:.2f} {to_unit.capitalize()}")

def main():
    print("Welcome to the Temperature Conversion Program!")
    print("--------------------------------------------")

    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit (Celsius, Fahrenheit, or Kelvin): ").lower()

    if original_unit in ['celsius', 'fahrenheit', 'kelvin']:
        # Convert to the other two units
        if original_unit == 'celsius':
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
        elif original_unit == 'fahrenheit':
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
        else:
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)

        # Print the results
        print_conversion_result(temperature, original_unit, 'fahrenheit', fahrenheit)
        print_conversion_result(temperature, original_unit, 'kelvin', kelvin)
    else:
        print("Oops! Please enter a valid temperature unit: Celsius, Fahrenheit, or Kelvin.")

if __name__ == "__main__":
    main()
