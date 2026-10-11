# Q7 - ATM Withdrawal Analysis

successful = 0
rejected = 0
print("Enter 10 withdrawal requests:")
for i in range(1, 11):
    amount = int(input("Enter withdrawal amount " + str(i) + ": "))

    # Check whether amount is valid
    if amount <= 0:
        print("Rejected - Invalid amount")
        rejected = rejected + 1

    # Check whether amount is a multiple of 500
    elif amount % 500 != 0:
        print("Rejected - Amount must be a multiple of 500")
        rejected = rejected + 1

    # Check maximum withdrawal limit
    elif amount > 20000:
        print("Rejected - Maximum withdrawal limit is Rs. 20000")
        rejected = rejected + 1

    else:
        print("Withdrawal Successful")
        successful = successful + 1

print("\n----- ATM Withdrawal Report -----")
print("Successful Transactions:", successful)
print("Rejected Transactions:", rejected)