# Problem Statement
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

def main():
    while True:
        # User input
        height = input("How tall are you? ")

        # Check if user does not enter anything
        if height == "":
            print("Exiting the program. Have a great day!") # Exit the program
            break

        # convert height to integer
        height = int(height)

        # Check if height is greater than or equal to 50
        if height >= 50: 
            print("You're tall enough to ride!\n") # if height is greater than or equal to 50 then print "You're tall enough to ride!"
        else:
            print("You're not tall enough to ride, but maybe next year!\n") # if height is less than 50 then print "You're not tall enough to ride, but maybe next year!"

# Yeh line program ko run karne ke liye zaroori hai
if __name__ == '__main__':
    main()