import time
import sys

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

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.value == key:
            return True
        elif key < node.value:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

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
    start_time = time.time()
    start_memory = sys.getsizeof(args)

    result = func(*args)
    
    end_time = time.time()
    end_memory = sys.getsizeof(args)

    elapsed_time = end_time - start_time
    memory_usage = end_memory - start_memory
    
    return result, elapsed_time, memory_usage

bst = BST()

elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    bst.insert(elem)

search_value = 40

print(f"Buscando o valor {search_value} na árvore...")
result, elapsed_time, memory_usage = measure_time_and_memory(bst.search, search_value)

if result:
    print(f"O valor {search_value} foi encontrado na árvore.")
else:
    print(f"O valor {search_value} não foi encontrado na árvore.")

print(f"Tempo de execução: {elapsed_time:.6f} segundos")
print(f"Memória usada: {memory_usage} bytes")

print("\nIn-order:", bst.inorder())
