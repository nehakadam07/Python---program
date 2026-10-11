# write a function using *args to count how many even numbers pass.

def count_even(*args):
    count = 0
    for num in args:
        if num % 2 == 0:
            count += 1
    return count

print("count of even numbers:", count_even(1, 2, 3, 4, 5, 6))