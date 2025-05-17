# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.


def main():
    # Dictionary storing fruit prices (per unit)
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 20.0,
        "kiwi": 2.5,
        "rambutan": 5.0,
        "mango": 7.0
    }

    total_cost = 0  # Initialize total cost

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))  # User input
        total_cost += quantity * price  # Multiply quantity with price

    # Print total cost
    print(f"\nYour total is ${total_cost:.2f}")  # Display in 2 decimal places

# Required line to run the main() function
if __name__ == '__main__':
    main()