# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2
#  You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.


# Define the speed of light in meters per second (a constant value)
C: int = 299792458  # The speed of light in m/s

# Define the main function that performs the energy calculation
def main():
    # Ask the user to input mass in kilograms and convert it to a float
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's formula: E = m * c^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display the formula being used
    print("e = m * C^2...")

    # Display the mass entered by the user
    print("m = " + str(mass_in_kg) + " kg")

    # Display the constant speed of light
    print("C = " + str(C) + " m/s")
    
    # Display the calculated energy in joules
    print(str(energy_in_joules) + " joules of energy!")

# This ensures the main() function runs only when this file is executed directly
if __name__ == '__main__':
    main()


