# Q3: Find the missing number using the sum formula

numbers = [1, 2, 4, 6, 3, 7, 8]
n = 8
# Calculate the expected sum of numbers from 1 to n
expected_sum = n * (n + 1) // 2
# Calculate the actual sum using a loop
actual_sum = 0
for num in numbers:
    actual_sum = actual_sum + num
# The difference gives the missing number
missing = expected_sum - actual_sum
print(missing)