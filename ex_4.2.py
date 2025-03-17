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
        network = ipaddress.ip_network(prefix, strict=False)
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
        return [int(bit) for bit in format(int(ipaddress.ip_address(ip)), '032b')]

def measure_trie_performance(trie, ip, prefixes):
    tracemalloc.start()
    start_time = time.time()

    for prefix in prefixes:
        trie.insert(prefix)

    result = trie.longest_prefix_match(ip)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, end_time - start_time, current / 1024, peak / 1024

prefixes = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]
ip_to_check = "192.168.1.100"

trie = Trie()

result, time_taken, memory_used, peak_memory = measure_trie_performance(trie, ip_to_check, prefixes)

print("\n==== Resultados da Busca de Prefixo com Trie ====")
print(f"Prefixos: {prefixes}")
print(f"IP a verificar: {ip_to_check}")
print(f"Prefixo mais longo encontrado: {result}")
print(f"Tempo: {time_taken:.6f} segundos | Memória: {memory_used:.2f} KB | Pico: {peak_memory:.2f} KB")
print("\n=== FIM ===\n")
