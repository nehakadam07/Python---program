def linear_search(account_ids, target):
    for index, account_id in enumerate(account_ids):
        if account_id == target:
            return index
    return -1


def binary_search(sorted_account_ids, target):
    low = 0
    high = len(sorted_account_ids) - 1

    while low <= high:
        middle = (low + high) // 2

        if sorted_account_ids[middle] == target:
            return middle
        elif sorted_account_ids[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


# Customer account IDs
account_ids = [1052, 1014, 1098, 1031, 1076]
target_id = 1031

# Linear Search uses the original list
linear_index = linear_search(account_ids, target_id)

# Binary Search uses a sorted copy of the list
sorted_account_ids = sorted(account_ids)
binary_index = binary_search(sorted_account_ids, target_id)

if linear_index != -1:
    print(f"Linear Search: ID {target_id} found at index {linear_index}.")
else:
    print(f"Linear Search: ID {target_id} was not found.")

if binary_index != -1:
    print(
        f"Binary Search: ID {target_id} found at index "
        f"{binary_index} in the sorted list."
    )
else:
    print(f"Binary Search: ID {target_id} was not found.")