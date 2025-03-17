import multiprocessing
import time
import tracemalloc
import numpy as np

def multiply_row(args):
    row_index, row, B = args
    return row_index, np.dot(row, B)

def parallel_matrix_multiplication(A, B):
    num_processes = min(len(A), multiprocessing.cpu_count())
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(multiply_row, [(i, A[i], B) for i in range(len(A))])

    results.sort()
    return np.array([row for _, row in results])

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

tracemalloc.start()
start_seq = time.time()

C_seq = np.dot(A, B)

end_seq = time.time()
current_seq, peak_seq = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start_par = time.time()

C_par = parallel_matrix_multiplication(A, B)

end_par = time.time()
current_par, peak_par = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Matriz Resultante (Sequencial):\n", C_seq)
print(f"Tempo de execução (sequencial): {end_seq - start_seq:.6f} segundos")
print(f"Memória usada (sequencial): {current_seq / 1024:.2f} KB")
print(f"Pico de memória (sequencial): {peak_seq / 1024:.2f} KB")

print("\nMatriz Resultante (Paralela):\n", C_par)
print(f"Tempo de execução (paralela): {end_par - start_par:.6f} segundos")
print(f"Memória usada (paralela): {current_par / 1024:.2f} KB")
print(f"Pico de memória (paralela): {peak_par / 1024:.2f} KB")
