#Take a number from the user and calculate sum. (Recursion)
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)
n = int(input("Enter n : "))
result = sum_n(n)
print("Sum = ", result)