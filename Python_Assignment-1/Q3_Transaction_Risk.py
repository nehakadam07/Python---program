# Q3 - Customer Transaction Risk Detector

#| Transaction amount | Risk        |
#| ------------------ | ----------- |
#| Less than ₹10,000  | Low Risk    |
#| ₹10,000 to ₹50,000 | Medium Risk |
#| Above ₹50,000      | High Risk   |

low_risk = 0
medium_risk = 0
high_risk = 0

print("Enter 10 transaction amounts:")

for i in range(1, 11):
    amount = float(input("Enter transaction amount " + str(i) + ": "))

    if amount < 10000:
        print("Low Risk")
        low_risk = low_risk + 1

    elif amount <= 50000:
        print("Medium Risk")
        medium_risk = medium_risk + 1

    else:
        print("High Risk")
        high_risk = high_risk + 1

print("\n----- Transaction Risk Report -----")
print("Low Risk Transactions:", low_risk)
print("Medium Risk Transactions:", medium_risk)
print("High Risk Transactions:", high_risk)