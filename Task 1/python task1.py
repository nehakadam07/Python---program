# write a function usings *args to find the largest number without using 

def find_largest(*numbers):
#assume the first number is the largest
    largest_num = numbers[0]
    # assume the first number is the largest
    for num in numbers:
        if num >= largest_num:
            # fixed: added a missing colon 
            largest_num = num
    return largest_num

print(find_largest(1, 5, 3, 9, 2))