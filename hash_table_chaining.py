class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        # Update the value if the key already exists
        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                print(f"Updated key {key} with value '{value}'.")
                return

        bucket.append((key, value))
        print(f"Inserted key {key} with value '{value}' at index {index}.")

    def search(self, key):
        index = self._hash(key)

        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value

        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[i]
                print(f"Deleted key {key}.")
                return

        print(f"Key {key} was not found.")

    def display(self):
        print("\nHash table:")
        for index, bucket in enumerate(self.table):
            print(f"{index}: {bucket}")


# Demonstration
hash_table = HashTable()

hash_table.insert(15, "Alice")
hash_table.insert(25, "Bob")       # Collision: both keys map to index 5
hash_table.insert(12, "Charlie")

print("Search key 25:", hash_table.search(25))

hash_table.delete(15)
hash_table.display()