# Q5 - Fraudulent Transaction Detector

suspicious_count = 0
suspicious_total = 0
for i in range(1, 9):
    amount = float(input("Enter transaction amount " + str(i) + ": "))

    if amount > 100000:
        print("Suspicious Transaction")
        suspicious_count = suspicious_count + 1
        suspicious_total = suspicious_total + amount
    else:
        print("Normal Transaction")

print("\n----- Fraudulent Transaction Report -----")
print("Number of Suspicious Transactions:", suspicious_count)
print("Total Value of Suspicious Transactions:", suspicious_total)