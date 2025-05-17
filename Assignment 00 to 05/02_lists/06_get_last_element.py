# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_first_element(lst):
    """ Prints the last element of a given non-empty list. """
    print("The Last element in the list is:", lst[-1])

def main():
    # User input
    n = int(input("Enter the number of elements in the list: "))
    lst = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)  # Add the element to the list

    # Function call to print the first element
    get_first_element(lst)

# Required line to run the program
if __name__ == '__main__':
    main()