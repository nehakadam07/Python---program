# Concept used: Recursion

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_number(n // 10, rev)
n = int(input("enter a number: "))
reverse = reverse_number(n)
if n == reverse:
    print("number is palindrome")
else:
    print("number is not palindrome")