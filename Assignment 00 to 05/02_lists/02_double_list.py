# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def main():
    # create a list of numbers

    numbers = [1, 2, 3, 4]

    #Loop through the list and get each element
    
    for i in range(len(numbers)):
        numbers[i] *= 2  

    # Print out the list with each element doubled

    print("Doubled List:", numbers)


if __name__ == '__main__':
    main()