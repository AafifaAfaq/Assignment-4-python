# Problem Statement
# Print 10 random numbers in the range 1 to 100.

import random  

def main():
    # Create a list of 10 random numbers
    random_numbers = [random.randint(1, 100) for _ in range(10)] # Use list comprehension
    print(*random_numbers)

# Call the main function
if __name__ == '__main__':
    main()