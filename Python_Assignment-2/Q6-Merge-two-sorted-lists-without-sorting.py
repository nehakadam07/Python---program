# Q6: Merge two sorted lists without sorting

a = [1, 4, 7, 10]
b = [2, 3, 8, 11, 15]

result = []

i = 0
j = 0

# Compare elements from both lists
while i < len(a) and j < len(b):

    if a[i] <= b[j]:
        result.append(a[i])
        i = i + 1
    else:
        result.append(b[j])
        j = j + 1

# Add remaining elements from the first list
while i < len(a):
    result.append(a[i])
    i = i + 1

# Add remaining elements from the second list
while j < len(b):
    result.append(b[j])
    j = j + 1

print(result)