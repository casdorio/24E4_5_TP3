class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:
    def __init__(self):
        self.root = None

    # Método de inserção
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

    # Método de remoção de nó
    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, node, key):
        if node is None:
            return node

        # Caso 1: Se o valor a ser removido é menor que o valor do nó atual, vá para a subárvore da esquerda
        if key < node.value:
            node.left = self._remove_recursive(node.left, key)

        # Caso 2: Se o valor a ser removido é maior que o valor do nó atual, vá para a subárvore da direita
        elif key > node.value:
            node.right = self._remove_recursive(node.right, key)

        # Caso 3: Se o valor do nó atual é igual ao valor a ser removido
        else:
            # Caso 1: Nó sem filhos (nó folha)
            if node.left is None and node.right is None:
                return None

            # Caso 2: Nó com um filho
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Caso 3: Nó com dois filhos
            else:
                # Encontrar o sucessor in-order (menor valor na subárvore à direita)
                min_larger_node = self._find_min(node.right)
                # Substituir o valor do nó pelo sucessor
                node.value = min_larger_node.value
                # Remover o sucessor
                node.right = self._remove_recursive(node.right, min_larger_node.value)

        return node

    # Encontrar o nó com o valor mínimo (sucessor in-order)
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Percurso In-order
    def inorder(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.value)
            self._inorder_recursive(node.right, elements)

    # Percurso Pre-order
    def preorder(self):
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements

    def _preorder_recursive(self, node, elements):
        if node:
            elements.append(node.value)
            self._preorder_recursive(node.left, elements)
            self._preorder_recursive(node.right, elements)

    # Percurso Post-order
    def postorder(self):
        elements = []
        self._postorder_recursive(self.root, elements)
        return elements

    def _postorder_recursive(self, node, elements):
        if node:
            self._postorder_recursive(node.left, elements)
            self._postorder_recursive(node.right, elements)
            elements.append(node.value)


# Testando a implementação
bst = BST()
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    bst.insert(elem)

# Imprimindo o percurso in-order antes de remover nós
print("In-order antes da remoção:", bst.inorder())  # Saída esperada: [20, 30, 40, 50, 60, 70, 80]

# Remover os nós 20, 30 e 50
bst.remove(20)
print("In-order após remoção de 20:", bst.inorder())  # Saída esperada: [30, 40, 50, 60, 70, 80]

bst.remove(30)
print("In-order após remoção de 30:", bst.inorder())  # Saída esperada: [40, 50, 60, 70, 80]

bst.remove(50)
print("In-order após remoção de 50:", bst.inorder())  # Saída esperada: [40, 60, 70, 80]
