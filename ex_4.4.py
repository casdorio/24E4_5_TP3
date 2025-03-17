import ipaddress
import time
import tracemalloc

class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix):
        try:
            network = ipaddress.ip_network(prefix, strict=False)
        except ValueError:
            print(f"Prefixo inválido: {prefix}")
            return
        current_node = self.root
        for bit in self._ip_to_bits(network.network_address):
            if bit not in current_node.children:
                current_node.children[bit] = TrieNode()
            current_node = current_node.children[bit]
        current_node.prefix = prefix

    def longest_prefix_match(self, ip):
        current_node = self.root
        longest_match = None

        for bit in self._ip_to_bits(ip):
            if bit in current_node.children:
                current_node = current_node.children[bit]
                if current_node.prefix:
                    longest_match = current_node.prefix
            else:
                break

        return longest_match

    def _ip_to_bits(self, ip):
        return [int(bit) for bit in format(int(ipaddress.IPv4Address(ip)), '032b')]

def linear_search(prefixes, ip):
    for prefix in prefixes:
        try:
            network = ipaddress.ip_network(prefix, strict=False)
        except ValueError:
            continue
        if ipaddress.IPv4Address(ip) in network:
            return prefix
    return None

def measure_performance(method, *args):
    tracemalloc.start()
    start_time = time.time()

    result = method(*args)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, end_time - start_time, current / 1024, peak / 1024

prefixes = [f"192.168.{i}.0/24" for i in range(1, 1001)]
prefixes.append("192.168.256.0/24")
ip_to_check = "192.168.1.55"

result_linear, time_linear, memory_linear, peak_memory_linear = measure_performance(linear_search, prefixes, ip_to_check)

trie = Trie()
for prefix in prefixes:
    trie.insert(prefix)

result_trie, time_trie, memory_trie, peak_memory_trie = measure_performance(trie.longest_prefix_match, ip_to_check)

print("\n==== Resultados da Comparação de Desempenho ====")
print(f"Prefixos: {len(prefixes)}")
print(f"IP a verificar: {ip_to_check}")

print(f"\nBusca Linear:")
print(f"Prefixo encontrado: {result_linear}")
print(f"Tempo: {time_linear:.6f} segundos | Memória: {memory_linear:.2f} KB | Pico: {peak_memory_linear:.2f} KB")

print(f"\nBusca com Trie:")
print(f"Prefixo encontrado: {result_trie}")
print(f"Tempo: {time_trie:.6f} segundos | Memória: {memory_trie:.2f} KB | Pico: {peak_memory_trie:.2f} KB")

print("\n=== FIM ===\n")
