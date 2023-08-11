def find_largest_number(numbers):
    if not numbers:
        return None  # Return None for an empty list

    largest = numbers[0]  # Initialize largest with the first element
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if a larger number is found

    return largest

# Example usage
num_list = [25, 100, 45, 950, 1.5, 600]
largest_number = find_largest_number(num_list)

if largest_number is not None:
    print("The largest number in the list is:", largest_number)
else:
    print("The list is empty.")