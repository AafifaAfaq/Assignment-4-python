def main():
    #Take input from user
    current_value = int(input("Enter a number: "))  
    
    # Loop until current_value is 100 or greater
    while current_value < 100:
        current_value = current_value * 2  # Double the value
        print(current_value, end=" ")  # Print the current value in the same line

# Call the main function
if __name__ == '__main__':
    main()
