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

def find_max_sequential(root):
    if root is None:
        return float('-inf')
    
    left_max = find_max_sequential(root.left)
    right_max = find_max_sequential(root.right)

    return max(root.value, left_max, right_max)

def find_max_parallel(root, result):
    if root is None:
        return
    
    left_result = {"max": float('-inf')}
    right_result = {"max": float('-inf')}

    left_thread = threading.Thread(target=find_max_parallel, args=(root.left, left_result))
    right_thread = threading.Thread(target=find_max_parallel, args=(root.right, right_result))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    result["max"] = max(root.value, left_result["max"], right_result["max"])

def measure_max_performance(root, parallel=False):
    tracemalloc.start()
    start_time = time.time()

    if parallel:
        result = {"max": float('-inf')}
        find_max_parallel(root, result)
        max_value = result["max"]
    else:
        max_value = find_max_sequential(root)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return max_value, end_time - start_time, current / 1024, peak / 1024

values = [15, 10, 20, 8, 12, 17, 25]
root = None
for v in values:
    root = insert(root, v)

max_seq, time_seq, mem_seq, peak_seq = measure_max_performance(root, parallel=False)

max_par, time_par, mem_par, peak_par = measure_max_performance(root, parallel=True)

print("\n==== Comparação de Busca Máxima: Sequencial vs Paralela ====")
print(f"Valor máximo encontrado (Sequencial): {max_seq}")
print(f"Tempo (Sequencial): {time_seq:.6f} segundos")
print(f"Memória usada (Sequencial): {mem_seq:.2f} KB | Pico: {peak_seq:.2f} KB")

print("\nExecução Paralela:")
print(f"Valor máximo encontrado (Paralela): {max_par}")
print(f"Tempo (Paralela): {time_par:.6f} segundos")
print(f"Memória usada (Paralela): {mem_par:.2f} KB | Pico: {peak_par:.2f} KB")

print("\n=== FIM DA COMPARAÇÃO ===\n")
