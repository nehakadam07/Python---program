# Q5: Check whether two strings are anagrams

first = "listen"
second = "silent"

# Convert both strings to lowercase and remove spaces
first = first.lower().replace(" ", "")
second = second.lower().replace(" ", "")

# If lengths differ, they cannot be anagrams
if len(first) != len(second):
    print(False)

else:
    frequency = {}

    # Count characters in the first string
    for char in first:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1

    # Subtract character counts using the second string
    for char in second:
        if char in frequency:
            frequency[char] = frequency[char] - 1
        else:
            frequency[char] = -1

    # Check whether every character count is zero
    anagram = True

    for count in frequency.values():
        if count != 0:
            anagram = False
            break

    print(anagram)