import multiprocessing
import time
import tracemalloc

def partial_sum(numbers):
    return sum(numbers)

def parallel_sum(lst, num_processes=None):
    if num_processes is None:
        num_processes = multiprocessing.cpu_count() 

    chunk_size = len(lst) // num_processes
    chunks = [lst[i * chunk_size:(i + 1) * chunk_size] for i in range(num_processes)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(partial_sum, chunks)

    return sum(results)

N = 10_000_000
large_list = list(range(1, N + 1))

tracemalloc.start()
start_seq = time.time()

sequential_sum = sum(large_list)

end_seq = time.time()
current_seq, peak_seq = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start_par = time.time()

parallel_result = parallel_sum(large_list)

end_par = time.time()
current_par, peak_par = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Soma Sequencial:", sequential_sum)
print(f"Tempo de execução (sequencial): {end_seq - start_seq:.6f} segundos")
print(f"Memória usada (sequencial): {current_seq / 1024:.2f} KB")
print(f"Pico de memória (sequencial): {peak_seq / 1024:.2f} KB")

print("\nSoma Paralela:", parallel_result)
print(f"Tempo de execução (paralela): {end_par - start_par:.6f} segundos")
print(f"Memória usada (paralela): {current_par / 1024:.2f} KB")
print(f"Pico de memória (paralela): {peak_par / 1024:.2f} KB")
