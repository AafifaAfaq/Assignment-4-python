# Function to add three copies of 'data' to the given list 'my_list'
def add_three_copies(my_list, data):
    for i in range(3):  # Repeat 3 times
        my_list.append(data)  # Add the data to the list

def main():
    # Ask the user to enter a message
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Show the list before adding anything
    print("List before:", my_list)

    # Call the function to add the message 3 times to the list
    add_three_copies(my_list, message)

    # Show the list after adding the message
    print("List after:", my_list)


if __name__ == "__main__":
    main()
