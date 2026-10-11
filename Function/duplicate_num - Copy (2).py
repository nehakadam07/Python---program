# Function to check for duplicates in a list

def has_duplicates(my_list):
    # set() removes all duplicate items from the list
    if len(my_list) == len(set(my_list)):
        return False  # No duplicates found
    else:
        return True   # Duplicates exist
# Test list with duplicates (10 appears twice)
numbers_list = [10, 20, 30, 40, 10, 50]
# Call the function
result = has_duplicates(numbers_list)
# Print the result based on the return value
if result:
    print("The list contains duplicates.")
else:
    print("The list does not contain duplicates.")