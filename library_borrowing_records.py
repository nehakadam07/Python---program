from collections import Counter

# Number of books borrowed by each member
borrow_counts = [3, 0, 2, 3, 5, 0, 3, 1, 5, 3]

if not borrow_counts:
    print("No borrowing records are available.")
else:
    average = sum(borrow_counts) / len(borrow_counts)
    highest = max(borrow_counts)
    lowest = min(borrow_counts)
    zero_borrowers = borrow_counts.count(0)

    frequencies = Counter(borrow_counts)
    highest_frequency = max(frequencies.values())
    modes = [
        count for count, frequency in frequencies.items()
        if frequency == highest_frequency
    ]

    print(f"Average books borrowed: {average:.2f}")
    print(f"Highest borrowing count: {highest}")
    print(f"Lowest borrowing count: {lowest}")
    print(f"Members who borrowed no books: {zero_borrowers}")
    print(f"Most frequent borrowing count(s): {modes}")
    print(f"Frequency of mode: {highest_frequency}")