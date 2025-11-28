# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    try:
        # Ask user for the temperature
        user_temp = input("Enter the temperature to convert: ")

        # Validate numeric input
        if not user_temp.replace(".", "", 1).lstrip("-").isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp_value = float(user_temp)

        # Ask for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Conversion logic
        if unit == "F":
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted}°C")

        elif unit == "C":
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted}°F")

        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as error:
        print(error)


# Run the program
if __name__ == "__main__":
    main()
