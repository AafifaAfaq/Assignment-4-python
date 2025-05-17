def main():
    # Initialize a dictionary to store the count of each number
    num_counts = {}

    while True:
        user_input = input("Enter a number: ") 
        
        # Stop input if user presses Enter without typing anything
        if user_input == "":
            break
        
        # Convert input to an integer
        number = int(user_input)
        
        # Increase count in dictionary
        if number in num_counts:
            num_counts[number] += 1
        else:
            num_counts[number] = 1

    # Print the count of each number
    print("\nNumber occurrences:")
    for num, count in num_counts.items():
        print(f"{num} appears {count} times.")

# Required line to run the main() function
if __name__ == '__main__':
    main()