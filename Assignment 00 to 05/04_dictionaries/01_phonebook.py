# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# Function to read phone numbers from the user and store them in a dictionary
def read_phone_numbers():
    phonebook = {}  # Initialize an empty dictionary to store name-number pairs

    while True:
        name = input("Name: ")  # Prompt the user to enter a name
        if name == "":          # Exit the loop if the user enters an empty string
            break
        number = input("Number: ")  # Prompt the user to enter a number
        phonebook[name] = number    # Store the name and number in the dictionary

    return phonebook  # Return the filled phonebook

# Function to print all entries in the phonebook
def print_phonebook(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))  # Print each name and corresponding number

# Function to look up phone numbers by name
def lookup_number(phonebook):
    while True:
        name = input("Enter name to lookup: ")  # Prompt the user to enter a name to look up
        if name == "":                          # Exit the loop if the user enters an empty string
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")  # Inform the user if the name is not found
        else:
            print(phonebook[name])  # Print the corresponding number if found

# Main function to control the flow of the program
def main():
    phonebook = read_phone_numbers()  # Read and store phonebook entries
    print_phonebook(phonebook)        # Print all entries in the phonebook
    lookup_number(phonebook)          # Allow user to look up numbers by name

# Ensure the main function runs only if the script is executed directly
if __name__ == '__main__':
    main()
