import threading
import time
import tracemalloc

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def sequential_search(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    return sequential_search(root.left, target) or sequential_search(root.right, target)

def parallel_search(root, target, result):
    if root is None:
        return
    if root.value == target:
        result.append(True)
        return

    left_result = []
    right_result = []

    left_thread = threading.Thread(target=parallel_search, args=(root.left, target, left_result))
    right_thread = threading.Thread(target=parallel_search, args=(root.right, target, right_result))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    if left_result or right_result:
        result.append(True)

def measure_search_performance(root, target, parallel=False):
    tracemalloc.start()
    start_time = time.time()

    result = []
    if parallel:
        parallel_search(root, target, result)
        found = bool(result)
    else:
        found = sequential_search(root, target)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return found, end_time - start_time, current / 1024, peak / 1024

values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
root = None
for v in values:
    root = insert(root, v)

target_value = 60

found_seq, time_seq, mem_seq, peak_seq = measure_search_performance(root, target_value, parallel=False)

found_par, time_par, mem_par, peak_par = measure_search_performance(root, target_value, parallel=True)

print("\n==== Comparação Sequencial vs Paralela ====")
print(f"Valor {target_value} encontrado: {'Sim' if found_seq else 'Não'}")
print(f"Tempo (Sequencial): {time_seq:.6f} segundos")
print(f"Memória usada (Sequencial): {mem_seq:.2f} KB | Pico: {peak_seq:.2f} KB")

print("\nExecução Paralela:")
print(f"Valor {target_value} encontrado: {'Sim' if found_par else 'Não'}")
print(f"Tempo (Paralela): {time_par:.6f} segundos")
print(f"Memória usada (Paralela): {mem_par:.2f} KB | Pico: {peak_par:.2f} KB")

print("\n=== FIM DA COMPARAÇÃO ===\n")
