# Q2.2: Move zeros by modifying the original list

numbers = [0, 1, 0, 3, 12, 0, 5]
position = 0
# Place non-zero elements at the beginning
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[position] = numbers[i]
        position = position + 1
# Fill all remaining positions with zeros
while position < len(numbers):
    numbers[position] = 0
    position = position + 1
print(numbers)