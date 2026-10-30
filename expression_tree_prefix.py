class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


OPERATORS = {"+", "-", "*", "/"}


def build_expression_tree(prefix):
    tokens = prefix.replace(" ", "")
    stack = []

    for token in reversed(tokens):
        node = Node(token)

        if token in OPERATORS:
            if len(stack) < 2:
                raise ValueError("Invalid prefix expression.")

            node.left = stack.pop()
            node.right = stack.pop()

        stack.append(node)

    if len(stack) != 1:
        raise ValueError("Invalid prefix expression.")

    return stack[0]


def postorder_non_recursive(root):
    if root is None:
        return []

    first_stack = [root]
    second_stack = []

    while first_stack:
        node = first_stack.pop()
        second_stack.append(node)

        if node.left:
            first_stack.append(node.left)
        if node.right:
            first_stack.append(node.right)

    return [node.value for node in reversed(second_stack)]


def delete_tree(root):
    if root is None:
        return None

    stack = [root]
    nodes = []

    # Collect nodes iteratively
    while stack:
        node = stack.pop()
        nodes.append(node)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Clear references from children upward
    for node in reversed(nodes):
        node.left = None
        node.right = None

    return None


prefix_expression = "+--a*bc/def"

try:
    root = build_expression_tree(prefix_expression)

    print("Prefix expression:", prefix_expression)
    print("Postorder traversal:", "".join(postorder_non_recursive(root)))

    root = delete_tree(root)
    print("Expression tree deleted.")
except ValueError as error:
    print("Error:", error)