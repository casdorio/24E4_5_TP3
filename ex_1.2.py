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

    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return node

        if key < node.value:
            node.left = self._remove_recursive(node.left, key)
        elif key > node.value:
            node.right = self._remove_recursive(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.value = self._min_value_node(node.right).value
            node.right = self._remove_recursive(node.right, node.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.value)
            self._inorder_recursive(node.right, elements)

def measure_time_and_memory(func, *args):
    tracemalloc.start()
    start_time = time.time()

    result = func(*args)
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    memory_usage = peak / 1024

    return result, elapsed_time, memory_usage

bst = BST()

elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    bst.insert(elem)

print("Árvore In-order antes da remoção:", bst.inorder())

nodes_to_remove = [20, 30, 50]
for node in nodes_to_remove:
    print(f"\nRemovendo o nó {node}...")
    result, elapsed_time, memory_usage = measure_time_and_memory(bst.remove, node)
    
    print(f"Árvore In-order após a remoção de {node}: {bst.inorder()}")
    print(f"Tempo de execução: {elapsed_time:.6f} segundos")
    print(f"Memória usada: {memory_usage:.6f} KB")
