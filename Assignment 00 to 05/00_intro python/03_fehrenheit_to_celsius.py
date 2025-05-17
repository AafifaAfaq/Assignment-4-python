# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit and outputs the temperature converted to Celsius.
# The equation you should use for converting from Fahrenheit to Celsius is the following:
# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

def main():
    print("This program converts Fahrenheit to Celsius.")
    fahrenheit : str = input("Enter temperature in Fahrenheit: ")
    fahrenheit : float = float(fahrenheit)
    celsius : float = (fahrenheit - 32) * 5.0/9.0
    print("The temperature in Celsius is " + str(celsius) + "C.")

if __name__ == "__main__":
    main()