import random  # Random number generate karne ke liye

def main():
    # Random number generate
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # User input
        guess = int(input("Enter a guess: "))

        # Check the guess
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit loop when correct

# Call the main function
if __name__ == '__main__':
    main()
