# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48 


import random

def main():
    secret_number = random.randint(0, 99)  # Random number between 0 and 99
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))  # User input
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  # Exit loop when correct
        except ValueError:
            print("Please enter a valid number!")  # Handle non-integer inputs

# Required to call the main function
if __name__ == '__main__':
    main()