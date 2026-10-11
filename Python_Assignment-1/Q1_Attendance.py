# Q1. Employee Attendance Analyzer
# Calculate present days, absent days, attendance percentage
# and determine bonus eligibility.

total_days = int(input("Enter total working days: ")) 
present_days = int(input("Enter number of present days: ")) 
absent_days = total_days - present_days
attendance_percentage = (present_days / total_days) * 100
print("\n--- Employee Attendance Report ---")
print("Present Days:", present_days)
print("Absent Days:", absent_days)
print("Attendance Percentage:", attendance_percentage, "%")
if attendance_percentage >= 75:
    print("Bonus Eligibility: Eligible for bonus")
else:
    print("Bonus Eligibility: Not eligible for bonus")