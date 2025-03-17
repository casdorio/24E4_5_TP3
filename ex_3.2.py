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

def dfs_sequential(root, target, path=None):
    if root is None:
        return None
    if path is None:
        path = []
    
    path.append(root.value)

    if root.value == target:
        return path

    left_path = dfs_sequential(root.left, target, path.copy())
    if left_path:
        return left_path

    right_path = dfs_sequential(root.right, target, path.copy())
    if right_path:
        return right_path

    return None

def dfs_parallel(root, target, result, path=None):
    if root is None or result["found"]:
        return
    if path is None:
        path = []

    path.append(root.value)

    if root.value == target:
        result["found"] = True
        result["path"] = path
        return

    left_result = {"found": False, "path": []}
    right_result = {"found": False, "path": []}

    left_thread = threading.Thread(target=dfs_parallel, args=(root.left, target, left_result, path.copy()))
    right_thread = threading.Thread(target=dfs_parallel, args=(root.right, target, right_result, path.copy()))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    if left_result["found"]:
        result["found"] = True
        result["path"] = left_result["path"]
    elif right_result["found"]:
        result["found"] = True
        result["path"] = right_result["path"]

def measure_dfs_performance(root, target, parallel=False):
    tracemalloc.start()
    start_time = time.time()

    if parallel:
        result = {"found": False, "path": []}
        dfs_parallel(root, target, result)
        path = result["path"] if result["found"] else None
    else:
        path = dfs_sequential(root, target)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return path, end_time - start_time, current / 1024, peak / 1024

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = None
for v in values:
    root = insert(root, v)

target_value = 5

path_seq, time_seq, mem_seq, peak_seq = measure_dfs_performance(root, target_value, parallel=False)

path_par, time_par, mem_par, peak_par = measure_dfs_performance(root, target_value, parallel=True)

print("\n==== Comparação DFS Sequencial vs Paralela ====")
print(f"Valor {target_value} encontrado: {'Sim' if path_seq else 'Não'}")
print(f"Caminho (Sequencial): {path_seq}")
print(f"Tempo (Sequencial): {time_seq:.6f} segundos")
print(f"Memória usada (Sequencial): {mem_seq:.2f} KB | Pico: {peak_seq:.2f} KB")

print("\nExecução Paralela:")
print(f"Valor {target_value} encontrado: {'Sim' if path_par else 'Não'}")
print(f"Caminho (Paralela): {path_par}")
print(f"Tempo (Paralela): {time_par:.6f} segundos")
print(f"Memória usada (Paralela): {mem_par:.2f} KB | Pico: {peak_par:.2f} KB")

print("\n=== FIM DA COMPARAÇÃO ===\n")
