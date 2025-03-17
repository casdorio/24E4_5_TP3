import ipaddress
import time
import tracemalloc

def check_ipv4_prefix(ip, prefix):
    try:
        network = ipaddress.ip_network(prefix, strict=False)
        ip_addr = ipaddress.ip_address(ip)
        return ip_addr in network
    except ValueError:
        return False

def measure_ipv4_performance(ip, prefix):
    tracemalloc.start()
    start_time = time.time()

    result = check_ipv4_prefix(ip, prefix)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, end_time - start_time, current / 1024, peak / 1024

ip1 = "192.168.1.5"
prefix1 = "192.168.1.0/24"

ip2 = "192.168.2.5"
prefix2 = "192.168.1.0/24"

result1, time1, mem1, peak1 = measure_ipv4_performance(ip1, prefix1)
result2, time2, mem2, peak2 = measure_ipv4_performance(ip2, prefix2)

print("\n==== Validação de Prefixo IPv4 ====")
print(f"IP: {ip1} | Prefixo: {prefix1} | Dentro? {result1}")
print(f"Tempo: {time1:.6f} segundos | Memória: {mem1:.2f} KB | Pico: {peak1:.2f} KB")

print(f"\nIP: {ip2} | Prefixo: {prefix2} | Dentro? {result2}")
print(f"Tempo: {time2:.6f} segundos | Memória: {mem2:.2f} KB | Pico: {peak2:.2f} KB")

print("\n=== FIM ===\n")
