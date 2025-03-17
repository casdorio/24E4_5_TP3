import multiprocessing
import time
import tracemalloc

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes_in_range(start, end):
    return sum(1 for n in range(start, end) if is_prime(n))

def parallel_prime_count(start, end, num_processes):
    step = (end - start) // num_processes
    ranges = [(start + i * step, start + (i + 1) * step) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], end)

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(count_primes_in_range, ranges)

    return sum(results)

start = 1
end = 100_000
num_processes = multiprocessing.cpu_count()

tracemalloc.start()
start_seq = time.time()

prime_count_seq = count_primes_in_range(start, end)

end_seq = time.time()
current_seq, peak_seq = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start_par = time.time()

prime_count_par = parallel_prime_count(start, end, num_processes)

end_par = time.time()
current_par, peak_par = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Números primos encontrados (Sequencial): {prime_count_seq}")
print(f"Tempo de execução (sequencial): {end_seq - start_seq:.6f} segundos")
print(f"Memória usada (sequencial): {current_seq / 1024:.2f} KB")
print(f"Pico de memória (sequencial): {peak_seq / 1024:.2f} KB")

print(f"\nNúmeros primos encontrados (Paralela): {prime_count_par}")
print(f"Tempo de execução (paralela): {end_par - start_par:.6f} segundos")
print(f"Memória usada (paralela): {current_par / 1024:.2f} KB")
print(f"Pico de memória (paralela): {peak_par / 1024:.2f} KB")
