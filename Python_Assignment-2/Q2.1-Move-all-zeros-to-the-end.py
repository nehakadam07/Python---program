# Q2.1: Move zeros to the end using a new list

numbers = [0, 1, 0, 3, 12, 0, 5]
result = []
# Add all non-zero elements
for num in numbers:
    if num != 0:
        result.append(num)
# Add zeros at the end
for num in numbers:
    if num == 0:
        result.append(num)

print(result)