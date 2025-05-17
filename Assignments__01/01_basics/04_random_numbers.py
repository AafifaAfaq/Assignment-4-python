import random

N_NUMBERS: int = 10  # Number of random numbers
MIN_VALUE: int = 1    # Minimum value
MAX_VALUE: int = 100  # Maximum value 

def main():
    # Generate and print random numbers
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

    print()  # Print new line

if __name__ == '__main__':
    main()
