class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value == current.value:
                print(f"{value} already exists; duplicates are not inserted.")
                return
            elif value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def search(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def _delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Case 1 and 2: no child or one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: two children
            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return node

    def delete(self, value):
        if not self.search(value):
            print(f"{value} was not found; nothing to delete.")
            return

        self.root = self._delete(self.root, value)
        print(f"Deleted {value}.")

    def _inorder(self, node, values):
        if node is not None:
            self._inorder(node.left, values)
            values.append(node.value)
            self._inorder(node.right, values)

    def display(self):
        values = []
        self._inorder(self.root, values)

        if values:
            print("BST values (inorder):", " ".join(map(str, values)))
        else:
            print("The BST is empty.")


def main():
    bst = BinarySearchTree()

    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in ("1", "2", "3"):
            try:
                value = int(input("Enter an integer value: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if choice == "1":
                bst.insert(value)
                print(f"Inserted {value} (if it was not already present).")
            elif choice == "2":
                bst.delete(value)
            else:
                if bst.search(value):
                    print(f"{value} was found in the BST.")
                else:
                    print(f"{value} was not found in the BST.")

        elif choice == "4":
            bst.display()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()