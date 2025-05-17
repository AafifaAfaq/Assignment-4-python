# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH = 3  # Define the maximum length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # If list length is greater than 3
        removed_item = lst.pop()  # Remove last item
        print("Removed:", removed_item)  # Print removed item

def main():
    lst = []  #
    
    # User input
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("Original list:", lst)  # print original list
    shorten(lst)  # Function call
    print("Shortened list:", lst)  # print shortened list


if __name__ == '__main__':
    main()