# Q10 - Monthly Sales Analysis

print("Enter sales data for 12 months:")
# Get sales for the first month
sales = float(input("Enter sales for month 1: "))
total_sales = sales
highest = sales
lowest = sales
high_sales_count = 0
if sales > 100000:
    high_sales_count = high_sales_count + 1
# Get sales for remaining 11 months
for i in range(2, 13):
    sales = float(input("Enter sales for month " + str(i) + ": "))
    total_sales = total_sales + sales
    # Find highest sales
    if sales > highest:
        highest = sales
    # Find lowest sales
    if sales < lowest:
        lowest = sales
    # Count high-sales months
    if sales > 100000:
        high_sales_count = high_sales_count + 1

# Calculate average sales
average_sales = total_sales / 12

# Calculate percentage of high-sales months
high_sales_percentage = (high_sales_count / 12) * 100

print("\n----- Monthly Sales Report -----")
print("Total Annual Sales:", total_sales)
print("Average Monthly Sales:", average_sales)
print("Highest Monthly Sales:", highest)
print("Lowest Monthly Sales:", lowest)
print("Months with Sales Above Rs. 100000:", high_sales_count)
print("Percentage of High-Sales Months:", high_sales_percentage, "%")