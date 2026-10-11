# Q10: Process positive even numbers

def process_numbers(numbers):

    total = 0
    count = 0
    largest = None

    # Check every number
    for num in numbers:

        # Ignore negative numbers
        if num < 0:
            continue

        # Keep only even numbers
        if num % 2 == 0:

            # Square the number
            square = num * num

            # Add the square to the total
            total = total + square

            # Count the squared values
            count = count + 1

            # Find the largest squared value
            if largest is None or square > largest:
                largest = square

    # Return the results
    return total, count, largest


# Test the function
numbers = [-2, 1, 2, 3, 4, 6, -8]

total, count, largest = process_numbers(numbers)

print("Total:", total)
print("Count:", count)
print("Largest squared value:", largest)