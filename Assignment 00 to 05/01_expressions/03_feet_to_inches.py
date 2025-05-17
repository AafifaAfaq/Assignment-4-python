# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Define a constant: Number of inches in one foot
INCHES_IN_FOOT: int = 12  

def main():
    # Prompt the user to enter a length in feet and convert the input to a float
    feet: float = float(input("Enter number of feet: "))
    
    # Convert the length from feet to inches using the defined constant
    inches: float = feet * INCHES_IN_FOOT
    
    # Display the result to the user
    print(str(feet) + " feet is equivalent to " + str(inches) + " inches.")
    
    
# Entry point of the program: ensures main() runs when the script is executed directly
if __name__ == '__main__':
    main()
