import time
import tracemalloc

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


def measure_performance(method, *args):
    tracemalloc.start()
    start_time = time.time()

    result = method(*args)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, end_time - start_time, current / 1024, peak / 1024


bst = BST()
elements = [50, 30, 70, 20, 40, 60, 80]

for elem in elements:
    bst.insert(elem)

inorder_result, inorder_time, inorder_memory, inorder_peak_memory = measure_performance(bst.inorder)
preorder_result, preorder_time, preorder_memory, preorder_peak_memory = measure_performance(bst.preorder)
postorder_result, postorder_time, postorder_memory, postorder_peak_memory = measure_performance(bst.postorder)

print("\n==== Resultados ====")
print(f"In-order traversal: {inorder_result}")
print(f"Tempo (in-order): {inorder_time:.6f} segundos | Memória: {inorder_memory:.2f} KB | Pico: {inorder_peak_memory:.2f} KB")

print(f"\nPre-order traversal: {preorder_result}")
print(f"Tempo (pre-order): {preorder_time:.6f} segundos | Memória: {preorder_memory:.2f} KB | Pico: {preorder_peak_memory:.2f} KB")

print(f"\nPost-order traversal: {postorder_result}")
print(f"Tempo (post-order): {postorder_time:.6f} segundos | Memória: {postorder_memory:.2f} KB | Pico: {postorder_peak_memory:.2f} KB")

print("\n=== FIM ===\n")
