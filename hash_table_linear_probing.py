class LinearProbingHashTable:
    EMPTY = None
    DELETED = object()

    def __init__(self, size=10):
        self.size = size
        self.table = [self.EMPTY] * size

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        start = self._hash(key)
        first_deleted = None

        for step in range(self.size):
            index = (start + step) % self.size
            slot = self.table[index]

            if slot == key:
                print(f"Key {key} already exists.")
                return

            if slot is self.DELETED and first_deleted is None:
                first_deleted = index
            elif slot is self.EMPTY:
                target = first_deleted if first_deleted is not None else index
                self.table[target] = key
                print(f"Inserted key {key} at index {target}.")
                return

        if first_deleted is not None:
            self.table[first_deleted] = key
            print(f"Inserted key {key} at index {first_deleted}.")
        else:
            print("Hash table is full. Cannot insert.")

    def search(self, key):
        start = self._hash(key)

        for step in range(self.size):
            index = (start + step) % self.size
            slot = self.table[index]

            if slot is self.EMPTY:
                return -1
            if slot == key:
                return index

        return -1

    def delete(self, key):
        index = self.search(key)

        if index == -1:
            print(f"Key {key} was not found.")
        else:
            self.table[index] = self.DELETED
            print(f"Deleted key {key} from index {index}.")

    def display(self):
        print("\nHash table:")
        for index, slot in enumerate(self.table):
            if slot is self.EMPTY:
                value = "Empty"
            elif slot is self.DELETED:
                value = "Deleted"
            else:
                value = str(slot)
            print(f"{index}: {value}")


def main():
    hash_table = LinearProbingHashTable(size=10)

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                key = int(input("Enter key to insert: "))
                hash_table.insert(key)
            except ValueError:
                print("Please enter an integer key.")

        elif choice == "2":
            try:
                key = int(input("Enter key to search: "))
                index = hash_table.search(key)
                if index == -1:
                    print(f"Key {key} was not found.")
                else:
                    print(f"Key {key} found at index {index}.")
            except ValueError:
                print("Please enter an integer key.")

        elif choice == "3":
            try:
                key = int(input("Enter key to delete: "))
                hash_table.delete(key)
            except ValueError:
                print("Please enter an integer key.")

        elif choice == "4":
            hash_table.display()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()