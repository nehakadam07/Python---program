# Q8 - Prime Number Detector

print("Prime numbers between 1 and 50 are:")
for num in range(2, 51):
    is_prime = 1
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = 0
            break
    if is_prime == 1:
        print(num)