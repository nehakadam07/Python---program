class StudentNode:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def find_node(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                return current
            current = current.next
        return None

    def add_student(self, roll_no, name, marks):
        if self.find_node(roll_no):
            print(f"Roll number {roll_no} already exists.")
            return

        new_node = StudentNode(roll_no, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        print(f"Added student: {name}")

    def delete_student(self, roll_no):
        current = self.head
        previous = None

        while current:
            if current.roll_no == roll_no:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print(f"Deleted student with roll number {roll_no}.")
                return
            previous = current
            current = current.next

        print(f"Roll number {roll_no} not found.")

    def update_student(self, roll_no, new_name, new_marks):
        student = self.find_node(roll_no)
        if student is None:
            print(f"Roll number {roll_no} not found.")
            return

        student.name = new_name
        student.marks = new_marks
        print(f"Updated student with roll number {roll_no}.")

    def search_student(self, roll_no):
        student = self.find_node(roll_no)
        if student is None:
            print(f"Roll number {roll_no} not found.")
        else:
            print(
                f"Found: Roll No: {student.roll_no}, "
                f"Name: {student.name}, Marks: {student.marks}"
            )

    def display_sorted(self, sort_by="roll_no", descending=False):
        if sort_by not in ("roll_no", "marks"):
            print("Sort field must be 'roll_no' or 'marks'.")
            return

        students = []
        current = self.head

        while current:
            students.append(current)
            current = current.next

        students.sort(
            key=lambda student: getattr(student, sort_by),
            reverse=descending
        )

        order = "descending" if descending else "ascending"
        print(f"\nRecords by {sort_by}, {order}:")

        if not students:
            print("No student records.")
            return

        for student in students:
            print(
                f"Roll No: {student.roll_no}, "
                f"Name: {student.name}, Marks: {student.marks}"
            )


# Demonstration
records = StudentLinkedList()

records.add_student(103, "Asha", 85)
records.add_student(101, "Ravi", 92)
records.add_student(102, "Meena", 78)

records.search_student(102)
records.update_student(102, "Meena", 88)
records.delete_student(103)

records.display_sorted(sort_by="roll_no", descending=False)
records.display_sorted(sort_by="marks", descending=True)