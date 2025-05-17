# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5,6,7,8]  # Make a list of numbers
    sum_of_numbers: int = sum_list(numbers)  # Find the sum of the list
    print("List:",numbers)  # Print out the list
    print( "Sum of list:",sum_of_numbers)  # Print out the sum above
    
if __name__ == '__main__':
    main()