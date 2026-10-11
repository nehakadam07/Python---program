# Q8: Check palindrome using recursion

def is_palindrome(text, left, right):

    # Base case: all character pairs matched
    if left >= right:
        return True

    # If the characters differ, it is not a palindrome
    if text[left] != text[right]:
        return False

    # Check the next inner pair recursively
    return is_palindrome(text, left + 1, right - 1)


# Test the function
text = "racecar"

result = is_palindrome(text, 0, len(text) - 1)

print(result)