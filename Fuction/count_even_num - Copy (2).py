# Function to count even numbers in a list

def count_even_numbers(numbers_list):
    count = 0
    for number in numbers_list:
        if number % 2 == 0:
            count += 1
    return count
# Given list of numbers
numbers = [10, 20, 15, 17, 18]
# Call the function and get the total count
even_count = count_even_numbers(numbers)
# Print the result
print(f"Total even numbers in the list: {even_count}")