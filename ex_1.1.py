class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.value)
            self._inorder_recursive(node.right, elements)

    def preorder(self):
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements

    def _preorder_recursive(self, node, elements):
        if node:
            elements.append(node.value)
            self._preorder_recursive(node.left, elements)
            self._preorder_recursive(node.right, elements)

    def postorder(self):
        elements = []
        self._postorder_recursive(self.root, elements)
        return elements

    def _postorder_recursive(self, node, elements):
        if node:
            self._postorder_recursive(node.left, elements)
            self._postorder_recursive(node.right, elements)
            elements.append(node.value)


bst = BST()
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    bst.insert(elem)

print("In-order:", bst.inorder())
print("Pre-order:", bst.preorder())
print("Post-order:", bst.postorder())
